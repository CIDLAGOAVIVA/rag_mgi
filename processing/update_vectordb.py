#!/usr/bin/env python
"""
Script para atualização incremental da base vetorial ChromaDB.

Este script:
1. Identifica arquivos Markdown novos ou modificados nas pastas definidas
2. Processa apenas esses arquivos usando chunking semântico
3. Adiciona os novos chunks à base vetorial existente

Funções de Utilidade
calculate_file_hash: calcula um hash MD5 de cada arquivo para detectar alterações
load_processed_files: carrega o registro de arquivos já processados
save_processed_files: salva o registro atualizado
find_markdown_files: busca recursivamente por arquivos .md em todas as pastas definidas
identify_new_or_modified_files: compara os arquivos encontrados com o registro para identificar novos/modificados
process_files: processa os arquivos selecionados usando chunking semântico
"""

import os
import sys
import json
import hashlib
import time
from typing import List, Dict, Any, Set, Tuple
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

# Imports do LangChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

# Imports do processador semântico
from processing.semantic_chunker import E5SemanticChunker

# Carregar variáveis de ambiente
load_dotenv()

# Verificar se a chave API está definida (para manter compatibilidade com o resto do sistema)
if "DEEPSEEK_API_KEY" not in os.environ:
    print("Erro: Chave de API do DeepSeek não encontrada no arquivo .env")
    sys.exit(1)

# Configurações
CHROMA_DB_DIR = "./chroma_db_semantic"
PROCESSED_FILES_RECORD = "./processed_files.json"
EMBEDDING_MODEL = "intfloat/multilingual-e5-base"

# Definir os caminhos para busca de documentos (igual ao rag_api.py)
base_paths = [
    '/mnt/data02/MGI/projetoscid/060 Sites Institucionais CEITEC',
    '/mnt/data02/MGI/projetoscid/061 Sites Institucionais IMBEL',
    '/mnt/data02/MGI/projetoscid/062 Sites Institucionais Telebras',
    '/mnt/data02/MGI/projetoscid/070 Artigos Científicos',
    '/mnt/data02/MGI/projetoscid/080 Transparência',
    '/mnt/data02/MGI/projetoscid/090 Prompts e Scripts',
    '/mnt/data02/MGI/projetoscid/091 Notícias Ceitec',
    '/mnt/data02/MGI/projetoscid/092 Notícias Imbel',
    '/mnt/data02/MGI/projetoscid/093 Notícias Telebras'
]

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

def find_markdown_files() -> List[str]:
    """Encontra todos os arquivos Markdown nas pastas definidas."""
    all_files = []
    
    for base_path in base_paths:
        if not os.path.exists(base_path) or not os.path.isdir(base_path):
            print(f"Aviso: Pasta não encontrada ou não é um diretório: {base_path}")
            continue
            
        for root, _, files in os.walk(base_path):
            for file in files:
                if file.lower().endswith('.md'):
                    file_path = os.path.join(root, file)
                    all_files.append(file_path)
                    
    return all_files

def identify_new_or_modified_files(all_files: List[str], processed_files: Dict[str, str]) -> Tuple[List[str], Dict[str, str]]:
    """Identifica arquivos novos ou modificados comparando com o registro."""
    new_or_modified = []
    updated_record = processed_files.copy()
    
    for file_path in all_files:
        file_hash = calculate_file_hash(file_path)
        
        # Verifica se o arquivo é novo ou foi modificado
        if file_path not in processed_files or processed_files[file_path] != file_hash:
            new_or_modified.append(file_path)
            updated_record[file_path] = file_hash
    
    return new_or_modified, updated_record

def process_files(files_to_process: List[str], chunker: E5SemanticChunker) -> List[Document]:
    """Processa os arquivos em chunks semânticos."""
    processed_chunks = []
    
    for i, file_path in enumerate(files_to_process):
        print(f"Processando arquivo {i+1}/{len(files_to_process)}: {file_path}")
        
        try:
            # Carregar o conteúdo do arquivo
            loader = TextLoader(file_path, encoding='utf-8')
            doc = loader.load()[0]  # Assume um documento por arquivo
            
            # Chunk o conteúdo do documento
            doc_chunks = chunker.chunk_text(doc.page_content)
            
            # Converter os chunks em documentos LangChain
            for j, chunk_text in enumerate(doc_chunks):
                chunk_doc = Document(
                    page_content=chunk_text,
                    metadata={
                        'source': file_path,
                        'chunk_id': f"{i}_{j}",
                        'doc_id': i,
                        'chunk_idx': j,
                        'total_chunks': len(doc_chunks),
                        'processed_date': datetime.now().isoformat()
                    }
                )
                processed_chunks.append(chunk_doc)
                
            print(f"  → Criados {len(doc_chunks)} chunks para este arquivo")
            
        except Exception as e:
            print(f"  → ERRO ao processar {file_path}: {e}")
            
    return processed_chunks

def main():
    start_time = time.time()
    print("=== Iniciando atualização incremental da base vetorial ===")
    print(f"Data e hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Verificar se a base vetorial existe
    if not os.path.exists(CHROMA_DB_DIR) or not os.path.isdir(CHROMA_DB_DIR):
        print(f"Erro: Base vetorial não encontrada em {CHROMA_DB_DIR}")
        print("Execute primeiro o arquivo rag_api.py para criar a base inicial.")
        sys.exit(1)
    
    # Carregar o registro de arquivos processados
    processed_files = load_processed_files()
    print(f"Registro de arquivos processados carregado: {len(processed_files)} arquivos")
    
    # Encontrar todos os arquivos Markdown
    all_files = find_markdown_files()
    print(f"Total de arquivos Markdown encontrados: {len(all_files)}")
    
    # Identificar arquivos novos ou modificados
    files_to_process, updated_record = identify_new_or_modified_files(all_files, processed_files)
    print(f"Arquivos para processar: {len(files_to_process)}")
    
    if not files_to_process:
        print("Nenhum arquivo novo ou modificado encontrado. Nada a fazer.")
        return
    
    # Instanciar o chunker semântico
    print("Inicializando o chunker semântico...")
    chunker = E5SemanticChunker(
        model_name=EMBEDDING_MODEL,
        similarity_threshold=0.7,
        max_tokens_per_chunk=700,
        min_tokens_per_chunk=100,
        print_logging=False
    )
    
    # Processar os arquivos
    print("Processando arquivos...")
    new_chunks = process_files(files_to_process, chunker)
    print(f"Total de novos chunks criados: {len(new_chunks)}")
    
    if not new_chunks:
        print("Nenhum chunk criado. Nada a adicionar à base vetorial.")
        return
    
    # Carregar a base vetorial existente
    print("Carregando base vetorial existente...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embeddings)
    
    # Adicionar novos chunks à base vetorial
    print("Adicionando novos chunks à base vetorial...")
    vectorstore.add_documents(new_chunks)
    
    # Persistir as mudanças
    print("Persistindo mudanças...")
    vectorstore.persist()
    
    # Atualizar o registro de arquivos processados
    print("Atualizando registro de arquivos processados...")
    save_processed_files(updated_record)
    
    elapsed_time = time.time() - start_time
    print(f"=== Atualização concluída em {elapsed_time:.2f} segundos ===")
    print(f"Novos chunks adicionados: {len(new_chunks)}")
    print(f"Total de arquivos no registro: {len(updated_record)}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        sys.exit(1)