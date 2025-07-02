from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import sys
import time
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek
from langchain.chains import RetrievalQA
from typing import List
from pydantic import BaseModel

# Adicionar o diretório raiz do projeto ao path ANTES da importação local
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Importar do módulo RAG
from rag.rag_cria_bd import (
    create_vectorstore, 
    load_processed_files, 
    save_processed_files,
    calculate_file_hash, 
    DEFAULT_BASE_PATHS
)

# Definir as constantes de configuração
CHROMA_DB_DIR = "./chroma_db_semantic"
EMBEDDING_MODEL = "intfloat/multilingual-e5-base"

app = FastAPI()

# Adicionar CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar variáveis de ambiente
load_dotenv()

# Verificar se a chave API está definida
if "DEEPSEEK_API_KEY" not in os.environ:
    print("Erro: Chave de API do DeepSeek não encontrada no arquivo .env")
    sys.exit(1)

try:
    # Carregar o registro de arquivos já processados
    processed_files_record = load_processed_files()
    
    # Verificar se já existe um banco de dados persistente
    if os.path.exists(CHROMA_DB_DIR) and os.path.isdir(CHROMA_DB_DIR):
        print(f"Carregando base de dados vetorial existente de {CHROMA_DB_DIR}...")
        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        vectorstore = Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embeddings)
        
        # Se o registro de arquivos estiver vazio ou não existir, procurar e registrar os arquivos existentes
        if len(processed_files_record) == 0:
            print("Registro de arquivos processados vazio ou inexistente. Criando registro...")
            novo_registro = {}
            
            # Verificar todos os arquivos existentes nas pastas
            for base_path in DEFAULT_BASE_PATHS:
                if os.path.exists(base_path) and os.path.isdir(base_path):
                    print(f"Escaneando documentos em: {base_path}")
                    # Usamos apenas o escaneamento sem carregar o conteúdo completo
                    for root, _, files in os.walk(base_path):
                        for file in files:
                            if file.endswith('.md'):
                                file_path = os.path.join(root, file)
                                novo_registro[file_path] = calculate_file_hash(file_path)
            
            # Salvar o registro de arquivos
            print(f"Salvando registro de {len(novo_registro)} arquivos existentes...")
            save_processed_files(novo_registro)
            processed_files_record = novo_registro  # Atualizar o registro em memória
        
        print(f"Base de dados existente carregada. Registro tem {len(processed_files_record)} arquivos.")
        
    else:
        # Base de dados não encontrada, chamar a função de criação do módulo rag_pergunta_resposta
        print(f"Base de dados vetorial não encontrada em {CHROMA_DB_DIR}. Criando nova base...")
        vectorstore = create_vectorstore(base_paths=DEFAULT_BASE_PATHS, chroma_db_dir=CHROMA_DB_DIR)
        print("Base de dados vetorial criada com sucesso.")

    # Configure o retrievador usando MMR para buscar documentos relevantes e diversos
    retriever = vectorstore.as_retriever(
        search_type="mmr",  # Maximum Marginal Relevance
        search_kwargs={
            "k": 15,         # Número de documentos a recuperar
            "fetch_k": 50,  # Busca mais documentos inicialmente
            "lambda_mult": 0.7,  # Equilíbrio entre relevância (0) e diversidade (1)
        }
    )

    # Template de prompt personalizado
    template = """
    Você é um assistente IA especializado em análise de documentos das empresas CEITEC, IMBEL e TELEBRAS. Sua função é fornecer informações precisas e contextualizadas com base nos documentos fornecidos.

INSTRUÇÕES GERAIS:
1. Analise cuidadosamente o contexto e a pergunta para identificar o tipo de informação solicitada e o provável perfil do usuário.
2. Use principalmente as informações fornecidas no contexto para responder à pergunta.
3. Seja específico e cite fontes quando possível, incluindo referências a documentos específicos.
4. Quando os documentos contiverem diferentes perspectivas sobre o mesmo assunto, apresente essas diferentes visões.

ADAPTAÇÃO POR PERFIL DE USUÁRIO:
- Para consultas técnicas sobre semicondutores, chips ou tecnologia: Use linguagem técnica específica do setor, mencione especificações precisas e padrões relevantes.
- Para consultas gerais: Use linguagem acessível e forneça explicações contextuais para termos técnicos.

FORMATO DA RESPOSTA:
- Para consultas informativas: Estruture a resposta em parágrafos organizados, começando pelos pontos mais relevantes.
- Para consultas numéricas ou financeiras: Use listas ou tabelas quando apropriado, destacando valores e métricas importantes.
- Para consultas comparativas: Organize a resposta em seções que contrastem os diferentes aspectos ou empresas.
- Para consultas técnicas: Inicie com um resumo conciso e depois detalhe os aspectos técnicos.
- Para consultas históricas: Apresente os eventos em ordem cronológica, destacando datas importantes.

REGRAS ESPECÍFICAS:
1. Se a informação não estiver explicitamente disponível no contexto, indique isso claramente e sugira onde o usuário poderia buscar mais informações.
2. Nunca invente informações ou extrapole além do que está disponível nos documentos fornecidos.
3. Se a pergunta for ambígua, esclareça quais aspectos você está abordando na resposta.
4. Para informações financeiras ou governamentais, especifique sempre a data ou período a que se referem os dados.
    
    Contexto: {context}
            
    Pergunta: {question}
            
    Resposta:
    """

    PROMPT = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    # Configure o modelo de linguagem
    llm = ChatDeepSeek(
        model="deepseek-chat",  # ou outro modelo disponível
        temperature=1.0,
        max_tokens=6000,
        timeout=None,
        max_retries=3,
    )

    # Configure a chain RAG
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )

    class QueryRequest(BaseModel):
        query: str

    class QueryResponse(BaseModel):
        answer: str
        sources: List[str]
        processing_time: float

    @app.post("/query", response_model=QueryResponse)
    async def process_query(request: QueryRequest):
        try:
            start_time = time.time()
            response = rag_chain({"query": request.query})
            processing_time = time.time() - start_time
            
            return QueryResponse(
                answer=response["result"],
                sources=[doc.metadata['source'] for doc in response["source_documents"]],
                processing_time=processing_time
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

except Exception as e:
    print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    import uvicorn
    print("Iniciando servidor RAG API com Semantic Chunking...")
    print("Acesse a documentação em: http://localhost:8010/docs")
    uvicorn.run(app, host="0.0.0.0", port=8010)