from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import dotenv
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_deepseek import ChatDeepSeek
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
from sentence_transformers import SentenceTransformer
import sys
import re
from datetime import datetime
from pydantic import BaseModel
from typing import List

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
# Adicionar as importações necessárias para o agentic_chunker
from processing.agentic_chunker import DeepSeekPropositionizer, AgenticChunker
import uuid

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

text = """
Dense retrieval se tornou um método proeminente para obter contexto relevante ou conhecimento mundial em tarefas de PNL de domínio aberto. 
Quando usamos um recuperador denso aprendido em um corpus de recuperação no momento da inferência, uma escolha de design frequentemente 
negligenciada é a unidade de recuperação na qual o corpus é indexado, por exemplo, documento, passagem ou sentença. 
Descobrimos que a escolha da unidade de recuperação impacta significativamente o desempenho das tarefas de recuperação e downstream. 
Distinto da abordagem típica de usar passagens ou sentenças, introduzimos uma nova unidade de recuperação, proposição, para recuperação densa. 
Proposições são definidas como expressões atômicas dentro do texto, cada uma encapsulando um factóide distinto e apresentada em um formato 
de linguagem natural conciso e autocontido. Conduzimos uma comparação empírica de diferentes granularidades de recuperação. 
Nossos experimentos revelam que indexar um corpus por unidades de granulação fina, como proposições, supera significativamente as unidades 
de nível de passagem em tarefas de recuperação.
"""

# Verificar se a chave API está definida
if "DEEPSEEK_API_KEY" not in os.environ:
    print("Erro: Chave de API do DeepSeek não encontrada no arquivo .env")
    sys.exit(1)

try:
    # Carregando documentos da pasta selecionada
    print("Carregando documentos...")
    loader = DirectoryLoader('./data2/processed', glob="**/*.md",
                             loader_cls=lambda file_path: TextLoader(file_path, encoding='utf-8'), show_progress=True)
    documentos = loader.load()
    print(f"Carregados {len(documentos)} documentos")

    ### -- PROCESSAMENTO DE DOCUMENTOS USANDO O AGENTIC_CHUNKER -- ###

    # # Convertendo documentos em proposições e chunks semânticos
    # print("Processando documentos e criando proposições...")
    # propositionizer = DeepSeekPropositionizer()
    # chunker = AgenticChunker(print_logging=False)
    
    # chunks = []
    # for documento in documentos:
    #     # Extrair proposições do texto
    #     proposicoes = propositionizer.text_to_propositions(documento.page_content)
        
    #     # Adicionar proposições ao chunker
    #     for proposicao in proposicoes:
    #         chunker.add_proposition(proposicao)
    
    # # Obter os chunks processados
    # chunk_dict = chunker.get_chunks(get_type='dict')
    # print(f"Criados {len(chunk_dict)} chunks semânticos")
    
    # # Converter os chunks semanticamente agrupados para o formato Document do LangChain
    # from langchain_core.documents import Document
    # processed_chunks = []
    
    # for chunk_id, chunk_data in chunk_dict.items():
    #     # Juntar todas as proposições do chunk em um único texto
    #     chunk_text = " ".join(chunk_data['propositions'])
        
    #     # Criar um novo Document com metadados enriquecidos
    #     doc = Document(
    #         page_content=chunk_text,
    #         metadata={
    #             'source': documento.metadata.get('source', 'unknown'),
    #             'chunk_id': chunk_id,
    #             'title': chunk_data['title'],
    #             'summary': chunk_data['summary']
    #         }
    #     )
    #     processed_chunks.append(doc)
    
    # chunks = processed_chunks
    # print(f"Processados {len(chunks)} chunks para indexação")

    # # Verificar se já existe um banco de dados persistente
    # if os.path.exists("./chroma_db") and os.path.isdir("./chroma_db"):
    #     print("Carregando base de dados vetorial existente...")
    #     from sentence_transformers import SentenceTransformer
        
    #     # Criar adaptador para SentenceTransformer compatível com LangChain
    #     class SentenceTransformerEmbeddings:
    #         def __init__(self, model_name):
    #             self.model = SentenceTransformer(model_name)
                
    #         def embed_documents(self, texts):
    #             return self.model.encode(texts)
                
    #         def embed_query(self, text):
    #             return self.model.encode(text)
    
    # # Criar instância do adaptador
    # embeddings = SentenceTransformerEmbeddings("intfloat/e5-mistral-7b-instruct")
    # vectorstore = Chroma(persist_directory="./chroma_db",
    #                      embedding_function=embeddings)
    
    ### -- DIVISÃO MANUAL EM CHUNKS -- ###

    print("Dividindo documentos em chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=256, chunk_overlap=51)
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
        from sentence_transformers import SentenceTransformer
        
        # Criar adaptador para SentenceTransformer compatível com LangChain
        class SentenceTransformerEmbeddings:
            def __init__(self, model_name):
                self.model = SentenceTransformer(model_name)
                
            def embed_documents(self, texts):
                return self.model.encode(texts)
                
            def embed_query(self, text):
                return self.model.encode(text)
        
        # Criar instância do adaptador
        embeddings = SentenceTransformerEmbeddings("sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory="./chroma_db" # A persistência ocorre aqui
        )

    #  Configure o retrievador usando MMR para buscar documentos relevantes e diversos
    retriever = vectorstore.as_retriever(
        search_type="mmr",  # Maximum Marginal Relevance
        search_kwargs={
            "k": 8,
            "fetch_k": 20,  # Busca mais documentos inicialmente
            "lambda_mult": 0.7,  # Equilíbrio entre relevância e diversidade
        }
    )

    # Template de prompt personalizado para melhorar as respostas
    # template = """
    # Você é um especialista em analisar e extrair informações de documentos acadêmicos e técnicos, principalmente dados administrativos e financeiros.

    # INSTRUÇÕES:
    # 1. Use principalmente as informações fornecidas na FONTE para responder à pergunta.
    # 2. Seja detalhado e preciso em sua resposta, mantendo um tom neutro e objetivo.
    # 3. Cite informações específicas dos documentos, incluindo números, datas e fatos quando disponíveis.
    # 4. Quando documentos apresentarem diferentes perspectivas sobre o mesmo assunto, mencione essas diferentes visões.
    # 5. Se a informação não estiver explicitamente disponível na fonte, indique quais partes do contexto são relevantes para a pergunta, mesmo que incompletas.
            
    # Contexto: {context}
            
    # Pergunta: {question}
            
    # Resposta:
    # """
    
    template = """
    Você é um especialista em analisar e extrair informações de documentos acadêmicos e técnicos, principalmente dados administrativos e financeiros.
    
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
        model="deepseek-reasoner",
        temperature=0.1,
        max_tokens=4096,
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
        print("Acesse a documentação em: http://localhost:8008/docs")
        uvicorn.run(app, host="0.0.0.0", port=8008)

except Exception as e:
    print(f"Ocorreu um erro: {e}")
