from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import sys
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek
from langchain.chains import RetrievalQA
from langchain_core.documents import Document
from typing import List
from pydantic import BaseModel
import time

# Adicionar o diretório raiz do projeto ao path ANTES da importação local
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Importar o chunker semântico (agora o path está correto)
from processing.semantic_chunker import E5SemanticChunker

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
    # Verificar se já existe um banco de dados persistente
    if os.path.exists("./chroma_db_semantic") and os.path.isdir("./chroma_db_semantic"):
        print("Carregando base de dados vetorial existente...")
        embeddings = HuggingFaceEmbeddings(
            model_name="intfloat/multilingual-e5-base")
        vectorstore = Chroma(persist_directory="./chroma_db_semantic",
                             embedding_function=embeddings)
        # Pulando processamento de documentos, pois já temos vetores persistidos
        print("Base de dados existente carregada. Pulando processamento de documentos.")
        
    else:
        # Carregando documentos da pasta selecionada
        print("Carregando documentos...")
        loader = DirectoryLoader('./data2/processed', glob="**/*.md",
                                 loader_cls=lambda file_path: TextLoader(file_path, encoding='utf-8'), show_progress=True)
        documentos = loader.load()
        print(f"Carregados {len(documentos)} documentos")

        # Processando documentos com o E5 Semantic Chunker
        print("Processando documentos com chunking semântico...")
        
        # Instanciar o chunker semântico
        chunker = E5SemanticChunker(
            model_name="intfloat/multilingual-e5-base",
            similarity_threshold=0.7,  # Ajuste conforme necessário para seu conteúdo
            max_tokens_per_chunk=700,
            min_tokens_per_chunk=100,
            print_logging=True
        )
        
        processed_chunks = []
        
        # Processar cada documento separadamente
        for i, documento in enumerate(documentos):
            print(f"Processando documento {i+1}/{len(documentos)}: {documento.metadata.get('source', 'unknown')}")
            
            # Chunk o conteúdo do documento
            doc_chunks = chunker.chunk_text(documento.page_content)
            
            # Converter os chunks em documentos LangChain
            for j, chunk_text in enumerate(doc_chunks):
                doc = Document(
                    page_content=chunk_text,
                    metadata={
                        'source': documento.metadata.get('source', 'unknown'),
                        'chunk_id': f"{i}_{j}",
                        'doc_id': i,
                        'chunk_idx': j,
                        'total_chunks': len(doc_chunks)
                    }
                )
                processed_chunks.append(doc)
        
        chunks = processed_chunks
        print(f"Processados {len(chunks)} chunks para indexação")
        
        # Crie embeddings e armazene em uma base vetorial
        print("Criando nova base de dados vetorial...")
        embeddings = HuggingFaceEmbeddings(
            model_name="intfloat/multilingual-e5-base")
        
        # Criar a base vetorial e persistir
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory="./chroma_db_semantic"
        )

    # Configure o retrievador usando MMR para buscar documentos relevantes e diversos
    retriever = vectorstore.as_retriever(
        search_type="mmr",  # Maximum Marginal Relevance
        search_kwargs={
            "k": 5,         # Número de documentos a recuperar
            "fetch_k": 20,  # Busca mais documentos inicialmente
            "lambda_mult": 0.7,  # Equilíbrio entre relevância (0) e diversidade (1)
        }
    )

    # Template de prompt personalizado
    template = """
    Você é um especialista em analisar e extrair informações de documentos. Trabalhe de forma detalhada
    com os documentos fornecidos como contexto para responder às perguntas.
    
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
        temperature=0.1,
        max_tokens=2048,
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

    if __name__ == "__main__":
        import uvicorn
        print("Iniciando servidor RAG API com Semantic Chunking...")
        print("Acesse a documentação em: http://localhost:8008/docs")
        uvicorn.run(app, host="0.0.0.0", port=8008)

except Exception as e:
    print(f"Ocorreu um erro: {e}")