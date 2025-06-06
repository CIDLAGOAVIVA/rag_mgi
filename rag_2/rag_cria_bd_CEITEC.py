import os
import dotenv
from dotenv import load_dotenv
import sys
import hashlib
import json
from datetime import datetime
from typing import List, Dict, Optional

# Importações do LangChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_deepseek import ChatDeepSeek
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader, DirectoryLoader, CSVLoader
from langchain.prompts import PromptTemplate
from langchain_core.documents import Document

# Adicionar o diretório raiz do projeto ao path ANTES da importação local
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Importar o chunker semântico 
from processing.semantic_chunker import E5SemanticChunker

# Carregar variáveis de ambiente
load_dotenv()

# Verificar se a chave API está definida
if "DEEPSEEK_API_KEY" not in os.environ:
    print("Erro: Chave de API do DeepSeek não encontrada no arquivo .env")
    sys.exit(1)

# Definições e constantes
CHROMA_DB_DIR_CEITEC = "./chroma_db_semantic_CEITEC"
PROCESSED_FILES_RECORD_CEITEC = "./processed_files_CEITEC.json"
EMBEDDING_MODEL = "intfloat/multilingual-e5-large"

# Definir o caminho base do projeto 
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_path, 'data')

# Caminhos padrão para documentos
DEFAULT_BASE_PATHS_CEITEC = [
    '/mnt/data02/MGI/projetoscid/051 Vídeos',
    '/mnt/data02/MGI/projetoscid/051 Vídeos CEITEC',
    '/mnt/data02/MGI/projetoscid/060 Sites Institucionais',
    '/mnt/data02/MGI/projetoscid/061 Sites Institucionais CEITEC',
    '/mnt/data02/MGI/projetoscid/071 Artigos Científicos CEITEC',
    '/mnt/data02/MGI/projetoscid/090 Prompts e Scripts',
    '/mnt/data02/MGI/projetoscid/091 Notícias Ceitec'
]

# Funções para gerenciar o registro de arquivos processados
def calculate_file_hash(file_path: str) -> str:
    """Calcula o hash MD5 de um arquivo para verificar modificações."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def load_processed_files() -> Dict[str, str]:
    """Carrega o registro de arquivos processados."""
    if os.path.exists(PROCESSED_FILES_RECORD_CEITEC):
        try:
            with open(PROCESSED_FILES_RECORD_CEITEC, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Erro ao ler arquivo de registro. Criando novo registro.")
            return {}
    return {}

def save_processed_files(processed_files: Dict[str, str]) -> None:
    """Salva o registro de arquivos processados."""
    with open(PROCESSED_FILES_RECORD_CEITEC, 'w', encoding='utf-8') as f:
        json.dump(processed_files, f, ensure_ascii=False, indent=2)

def create_vectorstore(base_paths: List[str] = None, chroma_db_dir_CEITEC: str = CHROMA_DB_DIR_CEITEC) -> Chroma:
    """
    Cria uma nova base de dados vetorial a partir dos documentos nas pastas especificadas.
    
    Args:
        base_paths: Lista de caminhos de pastas para buscar documentos
        chroma_db_dir: Diretório para salvar a base de dados vetorial
        
    Returns:
        Objeto Chroma contendo a base vetorial criada
    """
    try:
        # Se base_paths não for fornecido, usar caminhos padrão
        if base_paths is None:
            base_paths = DEFAULT_BASE_PATHS_CEITEC
        
        # Inicializar registro de arquivos
        novo_registro = {}
        
        # Carregando documentos de múltiplas pastas
        print("Carregando documentos de múltiplas pastas...")
        documentos = []
        
        for base_path in base_paths:
            if os.path.exists(base_path) and os.path.isdir(base_path):
                print(f"Carregando documentos de: {base_path}")
                
                # Carregar arquivos Markdown (.md)
                loader_md = DirectoryLoader(
                    base_path, 
                    glob="**/*.md",
                    loader_cls=lambda file_path: TextLoader(file_path, encoding='utf-8'), 
                    show_progress=True
                )
                docs_md = loader_md.load()
                documentos.extend(docs_md)
                print(f"  - Carregados {len(docs_md)} arquivos .md")
                
                # Carregar arquivos de texto (.txt)
                loader_txt = DirectoryLoader(
                    base_path, 
                    glob="**/*.txt",
                    loader_cls=lambda file_path: TextLoader(file_path, encoding='utf-8'), 
                    show_progress=True
                )
                docs_txt = loader_txt.load()
                documentos.extend(docs_txt)
                print(f"  - Carregados {len(docs_txt)} arquivos .txt")
                
                # Carregar arquivos CSV (.csv)
                loader_csv = DirectoryLoader(
                    base_path, 
                    glob="**/*.csv",
                    loader_cls=lambda file_path: CSVLoader(file_path, encoding='utf-8'), 
                    show_progress=True
                )
                docs_csv = loader_csv.load()
                documentos.extend(docs_csv)
                print(f"  - Carregados {len(docs_csv)} arquivos .csv")
                
                total_docs_pasta = len(docs_md) + len(docs_txt) + len(docs_csv)
                print(f"  - Total de documentos desta pasta: {total_docs_pasta}")
                
                # Calcular hash de cada arquivo carregado e adicionar ao novo registro
                for doc in documentos[-total_docs_pasta:]:  # Apenas os documentos recém-adicionados
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
            similarity_threshold=0.7,
            max_tokens_per_chunk=1000,
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
                        'processed_date': datetime.now().isoformat()
                    }
                )
                processed_chunks.append(doc)
        
        chunks = processed_chunks
        print(f"Processados {len(chunks)} chunks para indexação")
        
        # Crie embeddings e armazene em uma base vetorial
        print(f"Criando nova base de dados vetorial em {chroma_db_dir_CEITEC}...")
        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        
        # Criar a base vetorial e persistir
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=chroma_db_dir_CEITEC,
        )
        
        # Salvar o novo registro de arquivos processados
        print(f"Salvando registro de {len(novo_registro)} arquivos processados...")
        save_processed_files(novo_registro)
        print(f"Registro salvo em {PROCESSED_FILES_RECORD_CEITEC}")
        
        return vectorstore
        
    except Exception as e:
        print(f"Erro ao criar banco de dados vetorial: {e}")
        raise

# Executado diretamente        
if __name__ == "__main__":
    """
    Se executado diretamente, cria a base de dados vetorial.
    """
    print("Criando base de dados vetorial...")
    create_vectorstore()
    print("Base de dados vetorial criada com sucesso!")