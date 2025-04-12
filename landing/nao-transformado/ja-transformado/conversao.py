import os
import shutil
from docling.document_converter import DocumentConverter

# Definir diretórios de entrada e saída
input_dir = "landing/nao-transformado"
output_dir = "landing/ja-transformado/Markdown"

# Criar a pasta de saída se ela não existir
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Listar todos os arquivos PDF e DOCX no diretório de entrada
pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
docx_files = [f for f in os.listdir(input_dir) if f.endswith('.docx')]

# Inicializar o conversor
converter = DocumentConverter()

# Converter cada PDF para Markdown
for pdf_file in pdf_files:
    print(f"Convertendo PDF: {pdf_file} para Markdown...")
    
    input_path = os.path.join(input_dir, pdf_file)
    output_name = os.path.splitext(pdf_file)[0]
    output_path = os.path.join(output_dir, output_name + '.md')
    
    # Converter o PDF para Markdown
    result = converter.convert(input_path)
    markdown_content = result.document.export_to_markdown()
    
    # Salvar o conteúdo markdown no arquivo de saída
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Convertido para {output_path}")

# Converter cada DOCX para Markdown
for docx_file in docx_files:
    print(f"Convertendo DOCX: {docx_file} para Markdown...")
    
    input_path = os.path.join(input_dir, docx_file)
    output_name = os.path.splitext(docx_file)[0]
    output_path = os.path.join(output_dir, output_name + '.md')
    
    # Converter o DOCX para Markdown
    result = converter.convert(input_path)
    markdown_content = result.document.export_to_markdown()
    
    # Salvar o conteúdo markdown no arquivo de saída
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Convertido para {output_path}")

total_files = len(pdf_files) + len(docx_files)
print(f"Todos os {total_files} arquivos ({len(pdf_files)} PDFs e {len(docx_files)} DOCXs) foram convertidos para Markdown.")
