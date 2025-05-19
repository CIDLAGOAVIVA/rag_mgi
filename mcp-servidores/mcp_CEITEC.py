import os
import sys
import time
import asyncio
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from types import SimpleNamespace # Importar SimpleNamespace

# Adicionar o diretório raiz do projeto ao sys.path ANTES da importação local
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Importar do módulo RAG específico do CEITEC
from rag_2.rag_cria_bd_CEITEC import ( # ATENÇÃO: Verifique se o nome do módulo está correto
    create_vectorstore,
    load_processed_files,
    save_processed_files,
    calculate_file_hash,
    DEFAULT_BASE_PATHS_CEITEC
)
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek
from langchain.chains import RetrievalQA
from contextlib import asynccontextmanager

# Importar FastMCP v2
from fastmcp import FastMCP, Context

# Definir as constantes de configuração
CHROMA_DB_DIR_CEITEC = "./chroma_db_semantic_CEITEC"
EMBEDDING_MODEL = "intfloat/multilingual-e5-large" # Modelo de embedding

async def initialize_vectorstore():
    try:
        # Carregar o registro de arquivos já processados
        # ATENÇÃO: Esta função load_processed_files é genérica ou específica do CEITEC?
        # Se for específica, pode ser necessário ajustar o nome ou o módulo de onde é importada.
        # O mesmo vale para save_processed_files.
        processed_files_record = load_processed_files() # Assume que esta função é apropriada para CEITEC

        if os.path.exists(CHROMA_DB_DIR_CEITEC) and os.path.isdir(CHROMA_DB_DIR_CEITEC):
            print(f"Carregando base de dados vetorial existente de {CHROMA_DB_DIR_CEITEC}...")
            embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
            vectorstore = Chroma(persist_directory=CHROMA_DB_DIR_CEITEC, embedding_function=embeddings)
            print(f"Base de dados vetorial existente carregada.")

            if len(processed_files_record) == 0:
                print("Registro de arquivos processados vazio ou inexistente. Criando novo registro...")
                novo_registro = {}
                for base_path in DEFAULT_BASE_PATHS_CEITEC:
                    if os.path.exists(base_path) and os.path.isdir(base_path):
                        print(f"Escaneando documentos em: {base_path}")
                        for root, _, files_in_dir in os.walk(base_path):
                            for file_item in files_in_dir: # Renomeado para evitar conflito
                                if file_item.endswith('.md'):
                                    file_path = os.path.join(root, file_item)
                                    novo_registro[file_path] = calculate_file_hash(file_path)
                print(f"Salvando registro de {len(novo_registro)} arquivos existentes...")
                save_processed_files(novo_registro) # Assume que esta função é apropriada
                processed_files_record = novo_registro
            print(f"Base de dados vetorial existente carregada. Registro contém {len(processed_files_record)} arquivos.")
        else:
            print(f"Base de dados vetorial não encontrada em {CHROMA_DB_DIR_CEITEC}. Criando nova base...")
            # A função create_vectorstore também deve ser específica para CEITEC se necessário
            vectorstore = create_vectorstore(base_paths=DEFAULT_BASE_PATHS_CEITEC, chroma_db_dir=CHROMA_DB_DIR_CEITEC)
            print("Base de dados vetorial criada com sucesso.")
        return vectorstore
    except Exception as e:
        print(f"Erro ao inicializar base de dados vetorial para CEITEC: {e}")
        raise

def initialize_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 15, "fetch_k": 50, "lambda_mult": 0.7}
    )
    template = """
    Você é um assistente IA especializado em análise de documentos da empresa CEITEC. Sua função é fornecer informações precisas e contextualizadas com base nos documentos fornecidos.

    INSTRUÇÕES GERAIS:
    1. Analise cuidadosamente o contexto e a pergunta para identificar o tipo de informação solicitada.
    2. Use EXCLUSIVAMENTE as informações fornecidas no contexto para responder à pergunta.
    3. Seja específico e cite fontes quando possível, incluindo referências a documentos específicos.
    4. IMPORTANTE: Suas respostas devem se referir APENAS à empresa CEITEC. NÃO inclua informações sobre outras empresas (como IMBEL e Telebras) mesmo que a pergunta mencione essas empresas.
    5. Se a pergunta solicitar explicitamente uma comparação com outras empresas, informe que você só possui informações sobre CEITEC.
    6. Para perguntas sobre finanças, utilize terminologia financeira precisa e apresente dados quantitativos quando disponíveis.
    7. Para perguntas sobre projetos, estruture a resposta cronologicamente e inclua informações sobre status, orçamento e cronograma quando disponíveis.

    Contexto: {context}
    Pergunta: {question}
    Resposta:
    """
    PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])
    llm = ChatDeepSeek(model="deepseek-chat", temperature=1.0, max_tokens=5000, timeout=None, max_retries=3)
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever,
        return_source_documents=True, chain_type_kwargs={"prompt": PROMPT}
    )
    return rag_chain

@asynccontextmanager
async def app_lifespan(app: FastMCP):
    estado_app = SimpleNamespace()

    print(f"Lifespan: Inicializando recursos para {app.name}...")
    try:
        estado_app.vectorstore = await initialize_vectorstore()
        estado_app.rag_chain = initialize_rag_chain(estado_app.vectorstore)
        print(f"Lifespan: Recursos para {app.name} inicializados com sucesso.")
        
        # CORREÇÃO IMPORTANTE: Definir explicitamente app.state
        app.state = estado_app
        
        yield estado_app
    except Exception as e:
        error_type = type(e).__name__
        print(f"Lifespan ERRO CRÍTICO ({error_type}) durante a inicialização de recursos: {e}")
        raise
    finally:
        print(f"Lifespan: Encerrando servidor {app.name}, limpando recursos...")
        if hasattr(estado_app, 'vectorstore'):
            print("Lifespan: Limpando estado_app.vectorstore")
            del estado_app.vectorstore
        if hasattr(estado_app, 'rag_chain'):
            print("Lifespan: Limpando estado_app.rag_chain")
            del estado_app.rag_chain
        print(f"Lifespan: Recursos para {app.name} limpos.")

mcp = FastMCP(
    name="Base de Conhecimento CEITEC", # Traduzido
    lifespan=app_lifespan,
    instructions="Servidor de conhecimento sobre a empresa CEITEC e seus produtos de semicondutores.", # Já em PT
    cors_origins=["*"]
)

@mcp.tool()
async def query_ceitec(query: str, max_results: int = 15, ctx: Context = None) -> dict:
    """
    Busca informações específicas sobre a empresa CEITEC na base de conhecimento.
    Args:
        query: A consulta ou pergunta sobre a CEITEC.
        max_results: Número máximo de documentos a retornar (opcional).
    Returns:
        dict: Contém a resposta e as fontes de informação.
    """
    if ctx: await ctx.info(f"Iniciando consulta CEITEC: {query}")

    if not hasattr(ctx.fastmcp.state, 'rag_chain') or ctx.fastmcp.state.rag_chain is None:
        error_msg = "Cadeia RAG (CEITEC) não inicializada. O lifespan pode ter falhado."
        if ctx: await ctx.error(error_msg)
        return {"error": error_msg, "answer": "Erro: Base de conhecimento CEITEC não disponível."}

    rag_chain = ctx.fastmcp.state.rag_chain
    start_time = time.time()
    response = await asyncio.to_thread(rag_chain, {"query": query})
    processing_time = time.time() - start_time

    result = {
        "answer": response["result"],
        "sources": [doc.metadata['source'] for doc in response["source_documents"][:max_results]],
        "processing_time": processing_time
    }
    if ctx: await ctx.info(f"Consulta CEITEC finalizada em {processing_time:.2f}s")
    return result

@mcp.tool()
async def list_document_categories(ctx: Context = None) -> dict: # Nome da tool pode ser mais específico se necessário, e.g. list_ceitec_document_categories
    """Lista as categorias de documentos disponíveis sobre a CEITEC."""
    if ctx: await ctx.info("Listando categorias de documentos da CEITEC")
    categories = [
        "Relatórios Financeiros", "Especificações Técnicas", "Documentos Legais",
        "Notícias", "Artigos Científicos"
    ]
    return {"categories": categories}

# Definir recursos MCP
@mcp.resource("ceitec://overview")
def ceitec_overview() -> dict:
    """Visão geral sobre a empresa CEITEC e suas áreas de atuação."""
    return {
        "name": "CEITEC S.A.",
        "full_name": "Centro Nacional de Tecnologia Eletrônica Avançada S.A.",
        "founded": "2008", # Fundada em
        "headquarters": "Porto Alegre, RS, Brasil", # Sede
        "industry": "Semicondutores", # Indústria
        "main_products": ["Chips RFID", "Circuitos integrados para aplicações específicas"], # Principais produtos
        "description": "A CEITEC S.A. é uma empresa pública federal brasileira, vinculada ao Ministério da Ciência, Tecnologia e Inovações, focada no desenvolvimento e produção de componentes semicondutores."
    }

@mcp.resource("ceitec://document-count")
def document_count() -> dict: # Nome do resource pode ser mais específico, e.g. ceitec_document_count
    """Informações sobre a quantidade de documentos na base de conhecimento da CEITEC."""
    # Esta função load_processed_files deve ser a específica do CEITEC
    return {
        "total_documents": len(load_processed_files()), # Total de documentos
        "total_chunks": "Variável conforme processamento", # Total de pedaços (chunks)
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"), # Última atualização
    }

# Definir prompts MCP
@mcp.prompt()
def financial_response(company_name: str, financial_data: str, analysis: str, context: str, sources: str) -> str:
    """Formato para respostas sobre informações financeiras."""
    return f"""
    # Análise Financeira: {company_name}
    
    ## Dados Financeiros
    {financial_data}
    
    ## Análise
    {analysis}
    
    ## Contexto Econômico e Setorial
    {context}
    
    ## Fontes
    {sources}
    """

@mcp.prompt()
def project_detailed_response(company_name: str, project_name: str, description: str, timeline: str, budget: str, status: str, stakeholders: str, sources: str) -> str:
    """Formato para respostas detalhadas sobre projetos específicos."""
    return f"""
    # Projeto: {project_name} ({company_name})
    
    ## Descrição e Objetivos
    {description}
    
    ## Cronograma
    {timeline}
    
    ## Orçamento
    {budget}
    
    ## Status Atual
    {status}
    
    ## Partes Interessadas
    {stakeholders}
    
    ## Fontes
    {sources}
    """

@mcp.prompt()
def technical_response(summary: str, details: str, specs: str, sources: str) -> str: # Nome do prompt pode ser ceitec_technical_response
    """Formato para respostas técnicas sobre semicondutores e chips da CEITEC."""
    return f"""
    # Resposta Técnica sobre CEITEC
    ## Resumo Técnico
    {summary}
    ## Detalhamento
    {details}
    ## Especificações Técnicas
    {specs}
    ## Fontes
    {sources}
    """

@mcp.prompt()
def general_response(main_content: str, additional_info: str, sources: str) -> str: # Nome do prompt pode ser ceitec_general_response
    """Formato para respostas gerais sobre a CEITEC."""
    return f"""
    # Informações sobre CEITEC
    {main_content}
    ## Informações Adicionais
    {additional_info}
    ## Fontes
    {sources}
    """

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    from starlette.responses import JSONResponse
    healthy_status = {"status": "íntegro"}
    
    # Usar app.state diretamente agora que sabemos que está definido corretamente
    if not hasattr(mcp, 'state') or mcp.state is None or not hasattr(mcp.state, 'rag_chain'):
        healthy_status["status"] = "degradado"
        healthy_status["reason"] = "Cadeia RAG não inicializada"
    return JSONResponse(healthy_status)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8009)) # Porta padrão para CEITEC
    load_dotenv()
    print(f"Iniciando servidor MCP para CEITEC na porta {port}...")
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
        path="/mcp/"
    )