# token_analyzer.py
#!/usr/bin/env python3
import tiktoken
import os
import argparse
from pathlib import Path

def count_tokens(text, encoding_name="cl100k_base"):
    """Conta tokens em um texto usando o tokenizador especificado."""
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))

def main():
    # Definir os caminhos específicos para análise
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
    
    parser = argparse.ArgumentParser(description='Analisa tokens em arquivos Markdown')
    parser.add_argument('--glob', default="**/*.md", help='Padrão glob para seleção de arquivos')
    parser.add_argument('--directory', help='Diretório opcional para análise (sobrescreve os caminhos padrão)')
    args = parser.parse_args()
    
    # Estatísticas globais
    total_tokens = 0
    total_files_analyzed = 0
    all_largest_files = []
    directory_stats = {}
    
    # Se um diretório específico foi fornecido na linha de comando, usar apenas ele
    if args.directory:
        paths_to_analyze = [args.directory]
    else:
        paths_to_analyze = base_paths
    
    # Analisar cada diretório base
    for base_path in paths_to_analyze:
        path = Path(base_path)
        if not path.exists() or not path.is_dir():
            print(f"Aviso: {base_path} não é um diretório válido")
            continue
        
        print(f"\nAnalisando: {base_path}")
        dir_tokens = 0
        dir_files = 0
        largest_files = []
        
        for file_path in path.glob(args.glob):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                token_count = count_tokens(content)
                dir_tokens += token_count
                dir_files += 1
                total_tokens += token_count
                total_files_analyzed += 1
                
                # Manter registro dos maiores arquivos neste diretório
                largest_files.append((str(file_path), token_count))
                largest_files.sort(key=lambda x: x[1], reverse=True)
                largest_files = largest_files[:5]  # Manter apenas os 5 maiores por diretório
                
                # Adicionar aos maiores arquivos globais
                all_largest_files.append((str(file_path), token_count))
                all_largest_files.sort(key=lambda x: x[1], reverse=True)
                all_largest_files = all_largest_files[:10]  # Manter apenas os 10 maiores globais
                
                if dir_files % 100 == 0:
                    print(f"  Analisados {dir_files} arquivos...")
                    
            except Exception as e:
                print(f"  Erro ao processar {file_path}: {e}")
        
        # Salvar estatísticas deste diretório
        directory_stats[base_path] = {
            "files": dir_files,
            "tokens": dir_tokens,
            "avg_tokens_per_file": dir_tokens / dir_files if dir_files > 0 else 0
        }
        
        # Exibir resultados parciais
        print(f"  Total de arquivos: {dir_files}")
        print(f"  Total de tokens: {dir_tokens:,}")
        if dir_files > 0:
            print(f"  Média de tokens por arquivo: {dir_tokens/dir_files:,.1f}")
    
    # Exibir resultados globais
    print("\n\n=== RESUMO GLOBAL DE TOKENS ===")
    print(f"Total de arquivos analisados: {total_files_analyzed}")
    print(f"Total de tokens estimados: {total_tokens:,}")
    if total_files_analyzed > 0:
        print(f"Média de tokens por arquivo: {total_tokens/total_files_analyzed:,.1f}")
    
    # Exibir estatísticas por diretório
    print("\n=== ESTATÍSTICAS POR DIRETÓRIO ===")
    for dir_path, stats in directory_stats.items():
        dir_name = os.path.basename(dir_path)
        print(f"{dir_name}:")
        print(f"  Arquivos: {stats['files']}")
        print(f"  Tokens: {stats['tokens']:,}")
        if stats['files'] > 0:
            print(f"  Média de tokens/arquivo: {stats['avg_tokens_per_file']:,.1f}")
            percent = (stats['tokens'] / total_tokens) * 100 if total_tokens > 0 else 0
            print(f"  Percentual do total: {percent:.1f}%")
    
    print("\n=== TOP 10 ARQUIVOS COM MAIOR NÚMERO DE TOKENS ===")
    for i, (file_path, count) in enumerate(all_largest_files, 1):
        dir_name = os.path.dirname(file_path).split('/')[-1]
        file_name = os.path.basename(file_path)
        print(f"{i}. [{dir_name}] {file_name}: {count:,} tokens")

if __name__ == "__main__":
    main()