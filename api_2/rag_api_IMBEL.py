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

# Importar do módulo RAG específico da IMBEL
from rag_2.rag_cria_bd_IMBEL import ( # ATENÇÃO: Verifique se o nome do módulo está correto
    create_vectorstore,
    load_processed_files,
    save_processed_files,
    calculate_file_hash,
    DEFAULT_BASE_PATHS_IMBEL
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
CHROMA_DB_DIR_IMBEL = "./chroma_db_semantic_IMBEL"
EMBEDDING_MODEL = "intfloat/multilingual-e5-base" # Modelo de embedding

async def initialize_vectorstore():
    try:
        # ATENÇÃO: Estas funções devem ser específicas da IMBEL se necessário
        processed_files_record = load_processed_files() # Assume que esta função é apropriada para IMBEL

        if os.path.exists(CHROMA_DB_DIR_IMBEL) and os.path.isdir(CHROMA_DB_DIR_IMBEL):
            print(f"Carregando base de dados vetorial existente de {CHROMA_DB_DIR_IMBEL}...")
            embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
            vectorstore = Chroma(persist_directory=CHROMA_DB_DIR_IMBEL, embedding_function=embeddings)
            print(f"Base de dados vetorial existente carregada.")

            if len(processed_files_record) == 0:
                print("Registro de arquivos processados vazio ou inexistente. Criando novo registro...")
                novo_registro = {}
                for base_path in DEFAULT_BASE_PATHS_IMBEL:
                    if os.path.exists(base_path) and os.path.isdir(base_path):
                        print(f"Escaneando documentos em: {base_path}")
                        for root, _, files_in_dir in os.walk(base_path):
                            for file_item in files_in_dir: # Renomeado
                                if file_item.endswith('.md'):
                                    file_path = os.path.join(root, file_item)
                                    novo_registro[file_path] = calculate_file_hash(file_path)
                print(f"Salvando registro de {len(novo_registro)} arquivos existentes...")
                save_processed_files(novo_registro) # Assume que esta função é apropriada
                processed_files_record = novo_registro
            print(f"Base de dados vetorial existente carregada. Registro contém {len(processed_files_record)} arquivos.")
        else:
            print(f"Base de dados vetorial não encontrada em {CHROMA_DB_DIR_IMBEL}. Criando nova base...")
            # A função create_vectorstore também deve ser específica para IMBEL se necessário
            vectorstore = create_vectorstore(base_paths=DEFAULT_BASE_PATHS_IMBEL, chroma_db_dir=CHROMA_DB_DIR_IMBEL)
            print("Base de dados vetorial criada com sucesso.")
        return vectorstore
    except Exception as e:
        print(f"Erro ao inicializar base de dados vetorial para IMBEL: {e}")
        raise

def initialize_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 15, "fetch_k": 50, "lambda_mult": 0.7}
    )
    template = """
    Você é um assistente IA especializado em análise de documentos da empresa IMBEL. Sua função é fornecer informações precisas e contextualizadas com base nos documentos fornecidos.

    INSTRUÇÕES GERAIS:
    1. Analise cuidadosamente o contexto e a pergunta para identificar o tipo de informação solicitada.
    2. Use principalmente as informações fornecidas no contexto para responder à pergunta.
    3. Seja específico e cite fontes quando possível, incluindo referências a documentos específicos.
    4. Quando os documentos contiverem diferentes perspectivas sobre o mesmo assunto, apresente essas diferentes visões.

    Contexto: {context}
    Pergunta: {question}
    Resposta:
    """
    PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])
    llm = ChatDeepSeek(model="deepseek-chat", temperature=1.0, max_tokens=6000, timeout=None, max_retries=3)
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
    name="Base de Conhecimento IMBEL", # Traduzido
    lifespan=app_lifespan,
    instructions="Servidor de conhecimento sobre a empresa IMBEL e seus produtos de defesa e segurança.", # Já em PT
    cors_origins=["*"]
)

@mcp.tool()
async def query_imbel(query: str, max_results: int = 15, ctx: Context = None) -> dict:
    """
    Busca informações específicas sobre a empresa IMBEL na base de conhecimento.
    Args:
        query: A consulta ou pergunta sobre a IMBEL.
        max_results: Número máximo de documentos a retornar (opcional).
    Returns:
        dict: Contém a resposta e as fontes de informação.
    """
    if ctx: await ctx.info(f"Iniciando consulta IMBEL: {query}")

    if not hasattr(ctx.fastmcp.state, 'rag_chain') or ctx.fastmcp.state.rag_chain is None:
        error_msg = "Cadeia RAG (IMBEL) não inicializada. O lifespan pode ter falhado."
        if ctx: await ctx.error(error_msg)
        return {"error": error_msg, "answer": "Erro: Base de conhecimento IMBEL não disponível."}

    rag_chain = ctx.fastmcp.state.rag_chain
    start_time = time.time()
    response = await asyncio.to_thread(rag_chain, {"query": query})
    processing_time = time.time() - start_time

    result = {
        "answer": response["result"],
        "sources": [doc.metadata['source'] for doc in response["source_documents"][:max_results]],
        "processing_time": processing_time
    }
    if ctx: await ctx.info(f"Consulta IMBEL finalizada em {processing_time:.2f}s")
    return result

@mcp.tool()
async def list_document_categories(ctx: Context = None) -> dict: # Nome da tool pode ser mais específico
    """Lista as categorias de documentos disponíveis sobre a IMBEL."""
    if ctx: await ctx.info("Listando categorias de documentos da IMBEL")
    categories = [
        "Relatórios Técnicos", "Manuais de Produtos", "Documentos Institucionais",
        "Notícias", "Publicações Técnicas", "Catálogos de Produtos"
    ]
    return {"categories": categories}

@mcp.tool()
async def search_products(product_name: str, details: bool = False, ctx: Context = None) -> dict: # Nome da tool pode ser mais específico
    """
    Busca informações sobre produtos específicos da IMBEL.
    Args:
        product_name: Nome do produto a ser pesquisado.
        details: Se deve retornar detalhes técnicos completos (opcional).
    Returns:
        dict: Informações sobre o produto pesquisado.
    """
    if ctx: await ctx.info(f"Buscando informações sobre o produto IMBEL: {product_name}")

    if not hasattr(ctx.fastmcp.state, 'rag_chain') or ctx.fastmcp.state.rag_chain is None:
        error_msg = "Cadeia RAG (IMBEL) não inicializada. O lifespan pode ter falhado."
        if ctx: await ctx.error(error_msg)
        return {"error": error_msg, "description": "Erro: Base de conhecimento IMBEL não disponível."}

    rag_chain = ctx.fastmcp.state.rag_chain
    query_text = f"Informações detalhadas sobre o produto {product_name} da IMBEL"
    start_time = time.time()
    response = await asyncio.to_thread(rag_chain, {"query": query_text})
    processing_time = time.time() - start_time

    result = {
        "product_name": product_name,
        "description": response["result"],
        "sources": [doc.metadata['source'] for doc in response["source_documents"][:5]],
        "processing_time": processing_time
    }
    if details:
        result["technical_details"] = "Informações técnicas completas obtidas da base de conhecimento." # Detalhes técnicos
    else:
        result["technical_details"] = "Detalhes técnicos completos disponíveis mediante solicitação."

    if ctx: await ctx.info(f"Busca de produto IMBEL finalizada em {processing_time:.2f}s")
    return result

# Definir recursos MCP
@mcp.resource("imbel://overview")
def imbel_overview() -> dict:
    """Visão geral sobre a empresa IMBEL e suas áreas de atuação."""
    return {
        "name": "IMBEL",
        "full_name": "Indústria de Material Bélico do Brasil",
        "founded": "1975", # Fundada em
        "headquarters": "Brasília, DF, Brasil", # Sede
        "industry": "Defesa e Segurança", # Indústria
        "main_products": ["Armamentos", "Munições", "Explosivos", "Equipamentos militares"], # Principais produtos
        "description": "A IMBEL é uma empresa estatal brasileira vinculada ao Exército Brasileiro, focada no desenvolvimento e produção de material de defesa e segurança."
    }

@mcp.resource("imbel://document-count")
def document_count() -> dict: # Nome do resource pode ser imbel_document_count
    """Informações sobre a quantidade de documentos na base de conhecimento da IMBEL."""
    # Esta função load_processed_files deve ser a específica da IMBEL
    return {
        "total_documents": len(load_processed_files()), # Total de documentos
        "total_chunks": "Variável conforme processamento", # Total de pedaços (chunks)
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"), # Última atualização
    }

@mcp.resource("imbel://product-categories")
def product_categories() -> dict: # Nome do resource pode ser imbel_product_categories
    """Categorias de produtos da IMBEL."""
    return {
        "categories": [
            "Armas de pequeno porte", "Munições", "Explosivos",
            "Equipamentos de comunicação", "Sistemas de defesa"
        ]
    }

# Definir prompts MCP
@mcp.prompt()
def technical_response(summary: str, details: str, specs: str, sources: str) -> str: # Nome do prompt pode ser imbel_technical_response
    """Formato para respostas técnicas sobre produtos da IMBEL."""
    return f"""
    # Resposta Técnica sobre IMBEL
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
def general_response(main_content: str, additional_info: str, sources: str) -> str: # Nome do prompt pode ser imbel_general_response
    """Formato para respostas gerais sobre a IMBEL."""
    return f"""
    # Informações sobre IMBEL
    {main_content}
    ## Informações Adicionais
    {additional_info}
    ## Fontes
    {sources}
    """

@mcp.prompt()
def product_response(product_name: str, description: str, features: str, specs: str, sources: str) -> str: # Nome do prompt pode ser imbel_product_response
    """Formato para respostas sobre produtos específicos da IMBEL."""
    return f"""
    # Produto: {product_name}
    ## Descrição
    {description}
    ## Características
    {features}
    ## Especificações
    {specs}
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
    port = int(os.getenv("PORT", 8010)) # Porta padrão para IMBEL
    load_dotenv()
    print(f"Iniciando servidor MCP para IMBEL na porta {port}...")
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
        path="/mcp/"
    )