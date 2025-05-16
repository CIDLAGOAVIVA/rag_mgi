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

# Importar do módulo RAG
from rag_2.rag_cria_bd_Telebras import (
    create_vectorstore,
    load_processed_files,
    save_processed_files,
    calculate_file_hash,
    DEFAULT_BASE_PATHS_TELEBRAS
)
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek
from langchain.chains import RetrievalQA
from contextlib import asynccontextmanager

# Importar FastMCP v2
from fastmcp import FastMCP, Context

# NÃO precisamos mais de AppState ou USANDO_DICIONARIO_PARA_ESTADO
# A estrutura do FastMCP como fornecida não parece usar um 'AppState' nesse caminho de importação.
# Vamos gerenciar nosso próprio objeto de estado e passá-lo através do lifespan.

# Definir as constantes de configuração
CHROMA_DB_DIR_TELEBRAS = "./chroma_db_semantic_Telebras"
EMBEDDING_MODEL = "intfloat/multilingual-e5-base"

async def initialize_vectorstore():
    try:
        processed_files_record = load_processed_files()
        if os.path.exists(CHROMA_DB_DIR_TELEBRAS) and os.path.isdir(CHROMA_DB_DIR_TELEBRAS):
            print(f"Carregando base de dados vetorial existente de {CHROMA_DB_DIR_TELEBRAS}...")
            embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
            vectorstore = Chroma(persist_directory=CHROMA_DB_DIR_TELEBRAS, embedding_function=embeddings)
            print(f"Base de dados vetorial existente carregada.")
            if len(processed_files_record) == 0:
                print("Registro de arquivos processados vazio ou inexistente. Criando novo registro...")
                novo_registro = {}
                for base_path in DEFAULT_BASE_PATHS_TELEBRAS:
                    if os.path.exists(base_path) and os.path.isdir(base_path):
                        print(f"Escaneando documentos em: {base_path}")
                        for root, _, files in os.walk(base_path):
                            for file_in_dir in files: # Renomeado para evitar conflito com módulo 'files'
                                if file_in_dir.endswith('.md'):
                                    file_path = os.path.join(root, file_in_dir)
                                    novo_registro[file_path] = calculate_file_hash(file_path)
                print(f"Salvando registro de {len(novo_registro)} arquivos existentes...")
                save_processed_files(novo_registro)
                processed_files_record = novo_registro
            print(f"Base de dados vetorial existente carregada. Registro contém {len(processed_files_record)} arquivos.")
        else:
            print(f"Base de dados vetorial não encontrada em {CHROMA_DB_DIR_TELEBRAS}. Criando nova base...")
            vectorstore = create_vectorstore(base_paths=DEFAULT_BASE_PATHS_TELEBRAS, chroma_db_dir=CHROMA_DB_DIR_TELEBRAS)
            print("Base de dados vetorial criada com sucesso.")
        return vectorstore
    except Exception as e:
        print(f"Erro ao inicializar base de dados vetorial: {e}")
        raise

def initialize_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 15, "fetch_k": 50, "lambda_mult": 0.7}
    )
    template = """
    Você é um assistente IA especializado em análise de documentos da empresa TELEBRAS. Sua função é fornecer informações precisas e contextualizadas com base nos documentos fornecidos.
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
    # Criamos nosso próprio objeto de estado.
    # O FastMCP (via MCPServer) fará com que este objeto 'estado_app'
    # seja o que é acessado como 'app.state' ou 'ctx.fastmcp.state'
    # (o valor que é retornado/yielded pelo `lifespan`)
    estado_app = SimpleNamespace() # Usando SimpleNamespace para permitir atribuição de atributos

    print(f"Lifespan: Inicializando recursos para {app.name}...")
    try:
        estado_app.vectorstore = await initialize_vectorstore()
        estado_app.rag_chain = initialize_rag_chain(estado_app.vectorstore)
        print(f"Lifespan: Recursos para {app.name} inicializados com sucesso.")
        
        # Definir explicitamente app.state
        # Isso garante que o objeto estado_app seja acessível 
        # tanto via app.state quanto via ctx.fastmcp.state nas ferramentas
        app.state = estado_app
        
        yield estado_app # Importante: 'yield' o objeto de estado
    except Exception as e:
        error_type = type(e).__name__
        print(f"Lifespan ERRO CRÍTICO ({error_type}) durante a inicialização de recursos: {e}")
        raise
    finally:
        print(f"Lifespan: Encerrando servidor {app.name}, limpando recursos...")
        # A limpeza deve operar no objeto 'estado_app' que foi criado
        if hasattr(estado_app, 'vectorstore'):
            print("Lifespan: Limpando estado_app.vectorstore")
            del estado_app.vectorstore
        else:
            print("Lifespan: estado_app.vectorstore não encontrado para limpeza.")

        if hasattr(estado_app, 'rag_chain'):
            print("Lifespan: Limpando estado_app.rag_chain")
            del estado_app.rag_chain
        else:
            print("Lifespan: estado_app.rag_chain não encontrado para limpeza.")
        print(f"Lifespan: Recursos para {app.name} limpos.")

mcp = FastMCP(
    name="Base de Conhecimento TELEBRAS",
    lifespan=app_lifespan, # O FastMCP chamará esta função
    instructions="Servidor de conhecimento sobre a empresa TELEBRAS e seus serviços de telecomunicações.",
    cors_origins=["*"]
)

# Nos tools, ctx.fastmcp.state será o objeto 'estado_app' que foi yielded pelo lifespan.
@mcp.tool()
async def query_telebras(query: str, max_results: int = 15, ctx: Context = None) -> dict:
    """
    Busca informações específicas sobre a empresa TELEBRAS na base de conhecimento.
    Args:
        query: A consulta ou pergunta sobre a TELEBRAS.
        max_results: Número máximo de documentos a retornar (opcional).
    Returns:
        dict: Contém a resposta e as fontes de informação.
    """
    if ctx:
        await ctx.info(f"Iniciando consulta: {query}")

    # O objeto 'state' em ctx.fastmcp.state deve ser o 'estado_app' que yieldamos
    if not hasattr(ctx.fastmcp.state, 'rag_chain') or ctx.fastmcp.state.rag_chain is None:
        error_msg = "Cadeia RAG não inicializada no estado da aplicação. O lifespan pode ter falhado."
        if ctx: await ctx.error(error_msg)
        return {"error": error_msg, "answer": "Erro: Base de conhecimento não disponível."}

    rag_chain = ctx.fastmcp.state.rag_chain

    start_time = time.time()
    response = await asyncio.to_thread(rag_chain, {"query": query})
    processing_time = time.time() - start_time

    result = {
        "answer": response["result"],
        "sources": [doc.metadata['source'] for doc in response["source_documents"][:max_results]],
        "processing_time": processing_time
    }
    if ctx: await ctx.info(f"Consulta finalizada em {processing_time:.2f}s")
    return result

@mcp.tool()
async def list_document_categories(ctx: Context = None) -> dict:
    """Lista as categorias de documentos disponíveis sobre a TELEBRAS."""
    if ctx: await ctx.info("Listando categorias de documentos")
    categories = [
        "Relatórios Anuais", "Documentos Técnicos", "Releases de Imprensa",
        "Projetos de Conectividade", "Relatórios de Governança", "Documentos Regulatórios"
    ]
    return {"categories": categories}

@mcp.tool()
async def search_services(service_name: str, ctx: Context = None) -> dict:
    """
    Busca informações sobre serviços específicos da TELEBRAS.
    Args:
        service_name: Nome do serviço a ser pesquisado.
    Returns:
        dict: Informações sobre o serviço pesquisado.
    """
    if ctx: await ctx.info(f"Buscando informações sobre o serviço: {service_name}")

    if not hasattr(ctx.fastmcp.state, 'rag_chain') or ctx.fastmcp.state.rag_chain is None:
        error_msg = "Cadeia RAG não inicializada no estado da aplicação. O lifespan pode ter falhado."
        if ctx: await ctx.error(error_msg)
        return {"error": error_msg, "description": "Erro: Base de conhecimento não disponível."}

    rag_chain = ctx.fastmcp.state.rag_chain
    query_text = f"Informações detalhadas sobre o serviço {service_name} da TELEBRAS"
    start_time = time.time()
    response = await asyncio.to_thread(rag_chain, {"query": query_text})
    processing_time = time.time() - start_time

    result = {
        "service_name": service_name,
        "description": response["result"],
        "sources": [doc.metadata['source'] for doc in response["source_documents"][:5]],
        "processing_time": processing_time
    }
    if ctx: await ctx.info(f"Busca de serviço finalizada em {processing_time:.2f}s")
    return result

@mcp.tool()
async def search_projects(project_name: str = "", region: str = "", ctx: Context = None) -> dict:
    """
    Busca informações sobre projetos da TELEBRAS.
    Args:
        project_name: Nome do projeto a ser pesquisado (opcional).
        region: Região do Brasil onde o projeto está localizado (opcional).
    Returns:
        dict: Informações sobre projetos da TELEBRAS.
    """
    if ctx: await ctx.info(f"Buscando projetos - Nome: {project_name or 'todos'}, Região: {region or 'todas'}")

    if not hasattr(ctx.fastmcp.state, 'rag_chain') or ctx.fastmcp.state.rag_chain is None:
        error_msg = "Cadeia RAG não inicializada no estado da aplicação. O lifespan pode ter falhado."
        if ctx: await ctx.error(error_msg)
        return {"error": error_msg, "projects": "Erro: Base de conhecimento não disponível."}

    rag_chain = ctx.fastmcp.state.rag_chain

    if project_name and region:
        query_text = f"Informações sobre o projeto {project_name} da TELEBRAS na região {region}"
    elif project_name:
        query_text = f"Informações sobre o projeto {project_name} da TELEBRAS"
    elif region:
        query_text = f"Projetos da TELEBRAS na região {region}"
    else:
        query_text = "Principais projetos da TELEBRAS"

    start_time = time.time()
    response = await asyncio.to_thread(rag_chain, {"query": query_text})
    processing_time = time.time() - start_time

    result = {
        "query": query_text,
        "projects": response["result"],
        "sources": [doc.metadata['source'] for doc in response["source_documents"][:7]],
        "processing_time": processing_time
    }
    if ctx: await ctx.info(f"Busca de projetos finalizada em {processing_time:.2f}s")
    return result

# Definir recursos MCP
@mcp.resource("telebras://overview")
def telebras_overview() -> dict:
    """Visão geral sobre a empresa TELEBRAS e suas áreas de atuação."""
    return {
        "name": "TELEBRAS", "full_name": "Telecomunicações Brasileiras S.A.", "founded": "1972",
        "headquarters": "Brasília, DF, Brasil", "industry": "Telecomunicações",
        "main_services": ["Internet banda larga", "Satélite SGDC", "Backbone de fibra óptica", "Redes Governamentais"],
        "description": "A TELEBRAS é uma empresa estatal brasileira de telecomunicações vinculada ao Ministério das Comunicações, focada em implementar e operar redes de telecomunicações e prover serviços de internet."
    }

@mcp.resource("telebras://document-count")
def document_count() -> dict:
    """Informações sobre a quantidade de documentos na base de conhecimento."""
    return {
        "total_documents": len(load_processed_files()), "total_chunks": "Variável conforme processamento",
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

@mcp.resource("telebras://service-categories")
def service_categories() -> dict:
    """Categorias de serviços da TELEBRAS."""
    return {
        "categories": ["Internet banda larga", "Comunicação via satélite", "Redes corporativas", "Soluções governamentais", "Backbone nacional"]
    }

@mcp.resource("telebras://key-projects")
def key_projects() -> dict:
    """Principais projetos da TELEBRAS."""
    return {
        "projects": [
            {"name": "SGDC", "description": "Satélite Geoestacionário de Defesa e Comunicações Estratégicas", "year": "2017"},
            {"name": "PNBL", "description": "Programa Nacional de Banda Larga", "year": "2010"}
        ]
    }

# Definir prompts MCP (docstrings já em PT)
@mcp.prompt()
def technical_response(summary: str, details: str, specs: str, sources: str) -> str:
    """Formato para respostas técnicas sobre telecomunicações da TELEBRAS."""
    return f"""
    # Resposta Técnica sobre TELEBRAS
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
def general_response(main_content: str, additional_info: str, sources: str) -> str:
    """Formato para respostas gerais sobre a TELEBRAS."""
    return f"""
    # Informações sobre TELEBRAS
    {main_content}
    ## Informações Adicionais
    {additional_info}
    ## Fontes
    {sources}
    """
@mcp.prompt()
def project_response(project_name: str, description: str, goals: str, status: str, sources: str) -> str:
    """Formato para respostas sobre projetos específicos da TELEBRAS."""
    return f"""
    # Projeto: {project_name}
    ## Descrição
    {description}
    ## Objetivos
    {goals}
    ## Status e Cronograma
    {status}
    ## Fontes
    {sources}
    """
@mcp.prompt()
def comparison_response(topic: str, option1: str, details1: str, option2: str, details2: str, comparison: str, sources: str) -> str:
    """Formato para comparações de serviços ou tecnologias da TELEBRAS."""
    return f"""
    # Comparação: {topic}
    ## Opção 1: {option1}
    {details1}
    ## Opção 2: {option2}
    {details2}
    ## Análise Comparativa
    {comparison}
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
    port = int(os.getenv("PORT", 8011))
    load_dotenv()
    print(f"Iniciando servidor MCP para TELEBRAS na porta {port}...")
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
        path="/mcp/",
    )