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
import sqlite3
from typing import List, Dict, Any, Set, Tuple
from pathlib import Path
from dotenv import load_dotenv

# Adicionar o diretório raiz do projeto ao path ANTES da importação local
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from datetime import datetime

# Imports do LangChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader, CSVLoader
from langchain_core.documents import Document

# Imports do processador semântico (agora o path está correto)
from processing.semantic_chunker import E5SemanticChunker

# Carregar variáveis de ambiente
load_dotenv()

# Verificar se a chave API está definida (para manter compatibilidade com o resto do sistema)
if "DEEPSEEK_API_KEY" not in os.environ:
    print("Erro: Chave de API do DeepSeek não encontrada no arquivo .env")
    sys.exit(1)

# Configurações
CHROMA_DB_DIR_CEITEC = "./chroma_db_semantic_CEITEC"
PROCESSED_FILES_RECORD = "./processed_files.json"
EMBEDDING_MODEL = "intfloat/multilingual-e5-large"

# Definir os caminhos para busca de documentos
base_paths_CEITEC = [
    '/mnt/data02/MGI/projetoscid/051 Vídeos',
    '/mnt/data02/MGI/projetoscid/051 Vídeos CEITEC',
    '/mnt/data02/MGI/projetoscid/060 Sites Institucionais',
    '/mnt/data02/MGI/projetoscid/061 Sites Institucionais CEITEC',
    '/mnt/data02/MGI/projetoscid/071 Artigos Científicos CEITEC',
    '/mnt/data02/MGI/projetoscid/090 Prompts e Scripts',
    '/mnt/data02/MGI/projetoscid/091 Notícias Ceitec'
]

def calculate_file_hash(file_path: str) -> str:
    """Calcula o hash MD5 de um arquivo para verificar modificações."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def load_processed_files() -> Dict[str, str]:
    """
    Carrega o registro de arquivos processados.
    Se o registro não existir ou estiver vazio, tenta extrair as fontes do banco ChromaDB.
    """
    # Primeiro, tenta carregar o registro JSON existente
    if os.path.exists(PROCESSED_FILES_RECORD):
        try:
            with open(PROCESSED_FILES_RECORD, 'r', encoding='utf-8') as f:
                processed_files = json.load(f)
                if processed_files:  # Se não estiver vazio
                    print(f"Registro carregado do arquivo JSON: {len(processed_files)} entradas")
                    return processed_files
        except json.JSONDecodeError:
            print(f"Erro ao ler arquivo de registro JSON. Tentando extrair do ChromaDB.")
    
    # Se chegamos aqui, o arquivo não existe, está vazio ou corrompido
    # Tentar extrair as fontes diretamente do banco de dados ChromaDB
    processed_files = {}
    db_path = os.path.join(CHROMA_DB_DIR_CEITEC, "chroma.sqlite3")
    
    if os.path.exists(db_path):
        print(f"Extraindo fontes do banco de dados ChromaDB em {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Primeiro, vamos verificar quais tabelas e colunas existem no banco
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            print(f"Tabelas encontradas: {[t[0] for t in tables]}")
            
            # Verificar estrutura da tabela embeddings
            try:
                cursor.execute("PRAGMA table_info(embeddings)")
                columns = cursor.fetchall()
                column_names = [col[1] for col in columns]
                print(f"Colunas na tabela embeddings: {column_names}")
                
                # Identificar a coluna que contém os metadados
                if "document" in column_names:
                    # Consultar a tabela embeddings para obter os documentos que contêm metadados
                    cursor.execute("SELECT document FROM embeddings")
                    rows = cursor.fetchall()
                    
                    # Processar os resultados
                    count = 0
                    for row in rows:
                        try:
                            # O documento está armazenado como JSON
                            document = json.loads(row[0])
                            if 'metadata' in document and 'source' in document['metadata']:
                                source_path = document['metadata']['source']
                                # Verificar se o arquivo ainda existe
                                if os.path.exists(source_path):
                                    if source_path not in processed_files:
                                        file_hash = calculate_file_hash(source_path)
                                        processed_files[source_path] = file_hash
                                        count += 1
                                        if count % 50 == 0:
                                            print(f"Adicionados {count} arquivos ao registro...")
                        except (json.JSONDecodeError, KeyError) as e:
                            continue  # Ignora entradas com documento inválido
                else:
                    print("Coluna 'document' não encontrada na tabela embeddings")
            except sqlite3.Error as e:
                print(f"Erro ao verificar estrutura da tabela embeddings: {e}")
            
            conn.close()
            print(f"Extraídas {len(processed_files)} fontes únicas do banco de dados")
            
            # Salvar o registro reconstruído para uso futuro
            if processed_files:
                save_processed_files(processed_files)
                print(f"Registro reconstruído salvo em {PROCESSED_FILES_RECORD}")
                
        except sqlite3.Error as e:
            print(f"Erro ao acessar o banco de dados SQLite: {e}")
    else:
        print(f"Banco de dados ChromaDB não encontrado em {db_path}")
    
    return processed_files

def save_processed_files(processed_files: Dict[str, str]) -> None:
    """Salva o registro de arquivos processados."""
    with open(PROCESSED_FILES_RECORD, 'w', encoding='utf-8') as f:
        json.dump(processed_files, f, ensure_ascii=False, indent=2)

def find_supported_files() -> List[str]:
    """Encontra todos os arquivos suportados (.md, .txt, .csv) nas pastas definidas."""
    all_files = []
    supported_extensions = ['.md', '.txt', '.csv']
    
    for base_path in base_paths_CEITEC:
        if not os.path.exists(base_path) or not os.path.isdir(base_path):
            print(f"Aviso: Pasta não encontrada ou não é um diretório: {base_path}")
            continue
            
        for root, _, files in os.walk(base_path):
            for file in files:
                file_lower = file.lower()
                if any(file_lower.endswith(ext) for ext in supported_extensions):
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
            # Determinar o tipo de arquivo e usar o loader apropriado
            file_extension = os.path.splitext(file_path)[1].lower()
            
            if file_extension in ['.md', '.txt']:
                # Usar TextLoader para arquivos de texto e markdown
                loader = TextLoader(file_path, encoding='utf-8')
                doc = loader.load()[0]
            elif file_extension == '.csv':
                # Usar CSVLoader para arquivos CSV
                loader = CSVLoader(file_path, encoding='utf-8')
                csv_docs = loader.load()
                # Para CSV, concatenar todos os documentos em um só
                combined_content = "\n\n".join([doc.page_content for doc in csv_docs])
                doc = Document(
                    page_content=combined_content,
                    metadata={'source': file_path, 'file_type': 'csv'}
                )
            else:
                print(f"  → Tipo de arquivo não suportado: {file_extension}")
                continue
            
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
                        'file_type': file_extension[1:],  # Remove o ponto da extensão
                        'processed_date': datetime.now().isoformat()
                    }
                )
                processed_chunks.append(chunk_doc)
                
            print(f"  → Criados {len(doc_chunks)} chunks para este arquivo ({file_extension})")
            
        except Exception as e:
            print(f"  → ERRO ao processar {file_path}: {e}")
            
    return processed_chunks

def main():
    start_time = time.time()
    print("=== Iniciando atualização incremental da base vetorial ===")
    print(f"Data e hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Verificar se a base vetorial existe
    if not os.path.exists(CHROMA_DB_DIR_CEITEC) or not os.path.isdir(CHROMA_DB_DIR_CEITEC):
        print(f"Erro: Base vetorial não encontrada em {CHROMA_DB_DIR_CEITEC}")
        print("Execute primeiro o arquivo rag_api.py para criar a base inicial.")
        sys.exit(1)
    
    # Carregar o registro de arquivos processados
    processed_files = load_processed_files()
    print(f"Registro de arquivos processados carregado: {len(processed_files)} arquivos")
    
    # Encontrar todos os arquivos suportados
    all_files = find_supported_files()
    print(f"Total de arquivos suportados encontrados: {len(all_files)}")
    
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
        max_tokens_per_chunk=1000,
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
    vectorstore = Chroma(persist_directory=CHROMA_DB_DIR_CEITEC, embedding_function=embeddings)
    
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