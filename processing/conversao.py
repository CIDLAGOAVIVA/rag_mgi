import os
import shutil
from docling.document_converter import DocumentConverter
from docling.exceptions import ConversionError # Importar a exceção específica

# Definir diretórios de entrada e saída
input_dir = "./data2/raw/ceitec_data_pdf"
output_dir = "./data2/processed"

# Criar a pasta de saída se ela não existir
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- PASSO 1: Obter nomes base dos Markdowns existentes na pasta de saída ---
existing_markdown_bases = set()
if os.path.isdir(output_dir):
    print(f"Verificando Markdowns existentes em '{output_dir}'...")
    for filename in os.listdir(output_dir):
        if filename.lower().endswith(".md"):
            base_name = os.path.splitext(filename)[0]
            existing_markdown_bases.add(base_name)
    print(f"Encontrados {len(existing_markdown_bases)} Markdowns existentes.")
else:
    print(f"Pasta de saída '{output_dir}' não encontrada, nenhum Markdown existente para verificar.")


# Listar todos os arquivos PDF e DOCX no diretório de entrada
pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
docx_files = [f for f in os.listdir(input_dir) if f.endswith('.docx')]

# Inicializar o conversor
converter = DocumentConverter()

# --- Loop de conversão de PDF modificado ---
converted_pdf_count = 0
skipped_pdf_count = 0 # Contador para PDFs pulados
failed_pdf_files = []
print("\n--- Iniciando conversão de PDFs ---")
for pdf_file in pdf_files:
    input_path = os.path.join(input_dir, pdf_file)
    output_name = os.path.splitext(pdf_file)[0]
    output_path = os.path.join(output_dir, output_name + '.md')

    # --- PASSO 2: Verificar se o Markdown já existe ---
    if output_name in existing_markdown_bases:
        print(f"Pulando PDF: {pdf_file} (Markdown já existe em '{output_dir}')")
        skipped_pdf_count += 1
        continue # Pula para o próximo arquivo

    # Se não existe, prossegue com a conversão
    print(f"Convertendo PDF: {pdf_file} para Markdown...")
    try:
        # Tentar converter o PDF para Markdown
        result = converter.convert(input_path)
        markdown_content = result.document.export_to_markdown()

        # Salvar o conteúdo markdown no arquivo de saída
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"  -> Convertido para {output_path}")
        converted_pdf_count += 1
        existing_markdown_bases.add(output_name) # Adiciona à lista para evitar reprocessamento no mesmo run

    except ConversionError as e:
        # Capturar o erro específico de conversão do docling
        print(f"  -> ERRO ao converter {pdf_file}: {e}")
        print("     Pulando este arquivo.")
        failed_pdf_files.append(pdf_file)
    except Exception as e:
        # Capturar quaisquer outros erros inesperados durante a conversão
        print(f"  -> ERRO INESPERADO ao converter {pdf_file}: {e}")
        print("     Pulando este arquivo.")
        failed_pdf_files.append(pdf_file)


# --- Loop de conversão de DOCX (com verificação de existência) ---
converted_docx_count = 0
skipped_docx_count = 0 # Contador para DOCXs pulados
failed_docx_files = []
print("\n--- Iniciando conversão de DOCXs ---")
for docx_file in docx_files:
    input_path = os.path.join(input_dir, docx_file)
    output_name = os.path.splitext(docx_file)[0]
    output_path = os.path.join(output_dir, output_name + '.md')

    # --- PASSO 2: Verificar se o Markdown já existe ---
    if output_name in existing_markdown_bases:
        print(f"Pulando DOCX: {docx_file} (Markdown já existe em '{output_dir}')")
        skipped_docx_count += 1
        continue # Pula para o próximo arquivo

    # Se não existe, prossegue com a conversão
    print(f"Convertendo DOCX: {docx_file} para Markdown...")
    try:
        # Tentar converter o DOCX para Markdown
        result = converter.convert(input_path)
        markdown_content = result.document.export_to_markdown()

        # Salvar o conteúdo markdown no arquivo de saída
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"  -> Convertido para {output_path}")
        converted_docx_count += 1
        existing_markdown_bases.add(output_name) # Adiciona à lista

    except ConversionError as e:
        # Capturar o erro específico de conversão do docling
        print(f"  -> ERRO ao converter {docx_file}: {e}")
        print("     Pulando este arquivo.")
        failed_docx_files.append(docx_file)
    except Exception as e:
        # Capturar quaisquer outros erros inesperados durante a conversão
        print(f"  -> ERRO INESPERADO ao converter {docx_file}: {e}")
        print("     Pulando este arquivo.")
        failed_docx_files.append(docx_file)


# --- Resumo Final Atualizado ---
total_input_files = len(pdf_files) + len(docx_files)
total_converted = converted_pdf_count + converted_docx_count
total_skipped = skipped_pdf_count + skipped_docx_count
total_failed = len(failed_pdf_files) + len(failed_docx_files)

print("\n--- Resumo da Conversão ---")
print(f"Total de arquivos de entrada: {total_input_files} ({len(pdf_files)} PDFs, {len(docx_files)} DOCXs)")
print(f"Arquivos pulados (Markdown já existia): {total_skipped} ({skipped_pdf_count} PDFs, {skipped_docx_count} DOCXs)")
print(f"Arquivos convertidos com sucesso nesta execução: {total_converted} ({converted_pdf_count} PDFs, {converted_docx_count} DOCXs)")
print(f"Arquivos com falha na conversão: {total_failed}")
if failed_pdf_files:
    print("  PDFs com falha:")
    for fname in failed_pdf_files:
        print(f"    - {fname}")
if failed_docx_files:
    print("  DOCXs com falha:")
    for fname in failed_docx_files:
        print(f"    - {fname}")
print("--------------------------")
