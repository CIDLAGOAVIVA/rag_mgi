from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import sys
import json
import hashlib
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek
from langchain.chains import RetrievalQA
from langchain_core.documents import Document
from typing import List, Dict
from pydantic import BaseModel
import time
from datetime import datetime

# Adicionar o diretório raiz do projeto ao path ANTES da importação local
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Importar o chunker semântico (agora o path está correto)
from processing.semantic_chunker import E5SemanticChunker

# Definir as constantes de configuração (mesmas do update_vectordb.py)
CHROMA_DB_DIR = "./chroma_db_semantic"
PROCESSED_FILES_RECORD = "./processed_files.json"
EMBEDDING_MODEL = "intfloat/multilingual-e5-base"

# Funções para gerenciar o registro de arquivos processados (copiadas do update_vectordb.py)
def calculate_file_hash(file_path: str) -> str:
    """Calcula o hash MD5 de um arquivo para verificar modificações."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def load_processed_files() -> Dict[str, str]:
    """Carrega o registro de arquivos processados."""
    if os.path.exists(PROCESSED_FILES_RECORD):
        try:
            with open(PROCESSED_FILES_RECORD, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Erro ao ler arquivo de registro. Criando novo registro.")
            return {}
    return {}

def save_processed_files(processed_files: Dict[str, str]) -> None:
    """Salva o registro de arquivos processados."""
    with open(PROCESSED_FILES_RECORD, 'w', encoding='utf-8') as f:
        json.dump(processed_files, f, ensure_ascii=False, indent=2)


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
    # Definir os caminhos para busca de documentos
    base_paths = [
        '/mnt/data02/MGI/projetoscid/060 Sites Institucionais CEITEC',
        '/mnt/data02/MGI/projetoscid/061 Sites Institucionais IMBEL',
        '/mnt/data02/MGI/projetoscid/062 Sites Institucionais Telebras',
        '/mnt/data02/MGI/projetoscid/070 Artigos Científicos CEITEC',
        '/mnt/data02/MGI/projetoscid/071 Artigos Científicos IMBEL',
        '/mnt/data02/MGI/projetoscid/072 Artigos Científicos Telebras',
        '/mnt/data02/MGI/projetoscid/080 Transparência',
        '/mnt/data02/MGI/projetoscid/090 Prompts e Scripts',
        '/mnt/data02/MGI/projetoscid/091 Notícias Ceitec'
        '/mnt/data02/MGI/projetoscid/092 Notícias Imbel',
        '/mnt/data02/MGI/projetoscid/093 Notícias Telebras'
    ]
    
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
            for base_path in base_paths:
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
        # Carregando documentos de múltiplas pastas
        print("Carregando documentos de múltiplas pastas...")
        documentos = []
        
        # Novo registro de arquivos processados que será usado para atualizar o arquivo JSON
        novo_registro = {}
        
        for base_path in base_paths:
            if os.path.exists(base_path) and os.path.isdir(base_path):
                print(f"Carregando documentos de: {base_path}")
                loader = DirectoryLoader(base_path, glob="**/*.md",
                                 loader_cls=lambda file_path: TextLoader(file_path, encoding='utf-8'), 
                                 show_progress=True)
                docs_pasta = loader.load()
                documentos.extend(docs_pasta)
                print(f"  - Carregados {len(docs_pasta)} documentos desta pasta")
                
                # Calcular hash de cada arquivo carregado e adicionar ao novo registro
                for doc in docs_pasta:
                    file_path = doc.metadata.get('source')
                    if file_path:
                        novo_registro[file_path] = calculate_file_hash(file_path)
            else:
                print(f"Aviso: Pasta não encontrada: {base_path}")
        
        print(f"Carregados {len(documentos)} documentos no total")
        
        if len(documentos) == 0:
            print("Nenhum documento encontrado nas pastas especificadas. Verifique os caminhos.")
            sys.exit(1)

        # Processando documentos com o E5 Semantic Chunker
        print("Processando documentos com chunking semântico...")
        
        # Instanciar o chunker semântico
        chunker = E5SemanticChunker(
            model_name=EMBEDDING_MODEL,
            similarity_threshold=0.7,  # Ajuste conforme necessário para seu conteúdo
            max_tokens_per_chunk=700,
            min_tokens_per_chunk=100,
            print_logging=True
        )
        
        processed_chunks = []
        
        # Processar cada documento separadamente
        for i, documento in enumerate(documentos):
            source = documento.metadata.get('source', 'unknown')
            print(f"Processando documento {i+1}/{len(documentos)}: {source}")
            
            # Chunk o conteúdo do documento
            doc_chunks = chunker.chunk_text(documento.page_content)
            
            # Converter os chunks em documentos LangChain
            for j, chunk_text in enumerate(doc_chunks):
                doc = Document(
                    page_content=chunk_text,
                    metadata={
                        'source': source,
                        'chunk_id': f"{i}_{j}",
                        'doc_id': i,
                        'chunk_idx': j,
                        'total_chunks': len(doc_chunks),
                        'processed_date': datetime.now().isoformat()  # Adicionando data de processamento
                    }
                )
                processed_chunks.append(doc)
        
        chunks = processed_chunks
        print(f"Processados {len(chunks)} chunks para indexação")
        
        # Crie embeddings e armazene em uma base vetorial
        print(f"Criando nova base de dados vetorial em {CHROMA_DB_DIR}...")
        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        
        # Criar a base vetorial e persistir
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=CHROMA_DB_DIR
        )
        
        # Salvar o novo registro de arquivos processados
        print(f"Salvando registro de {len(novo_registro)} arquivos processados...")
        save_processed_files(novo_registro)
        print(f"Registro salvo em {PROCESSED_FILES_RECORD}")

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