from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import dotenv
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_deepseek import ChatDeepSeek
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
import sys
import re
from datetime import datetime
from pydantic import BaseModel
from typing import List

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
    # Carregando documentos da pasta selecionada
    print("Carregando documentos...")
    loader = DirectoryLoader('./data/', glob="**/*.md",
                             loader_cls=lambda file_path: TextLoader(file_path, encoding='utf-8'), show_progress=True)
    documentos = loader.load()
    print(f"Carregados {len(documentos)} documentos")

    # Dividindo em chunks
    print("Dividindo documentos em chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documentos)
    print(f"Criados {len(chunks)} chunks")

    # Verificar se já existe um banco de dados persistente
    if os.path.exists("./chroma_db") and os.path.isdir("./chroma_db"):
        print("Carregando base de dados vetorial existente...")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = Chroma(persist_directory="./chroma_db",
                             embedding_function=embeddings)
    else:
        # Crie embeddings e armazene em uma base vetorial
        print("Criando nova base de dados vetorial...")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )
        vectorstore.persist()

    # Configure o retrievador
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    # Template de prompt personalizado para melhorar as respostas
    template = """
    Use as informações a seguir para responder à pergunta do usuário.
    Se você não sabe a resposta, apenas diga que não sabe, não tente inventar uma resposta.
    
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
        model="deepseek-chat",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
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

    @app.post("/query", response_model=QueryResponse)
    async def process_query(request: QueryRequest):
        try:
            response = rag_chain({"query": request.query})
            return QueryResponse(
                answer=response["result"],
                sources=[doc.metadata['source']
                         for doc in response["source_documents"]]
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    if __name__ == "__main__":
        import uvicorn
        print("Iniciando servidor RAG API...")
        print("Acesse a documentação em: http://localhost:8000/docs")
        uvicorn.run(app, host="0.0.0.0", port=8000)

except Exception as e:
    print(f"Ocorreu um erro: {e}")
