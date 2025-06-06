import asyncio
import re
import os
from pathlib import Path
import sys
# Adicionar o diretório do script atual ao sys.path
project_root_dir = os.path.dirname(os.path.abspath(__file__))

# Construir o caminho para o diretório 'mcp-client'
mcp_client_actual_dir = os.path.join(project_root_dir, "mcp-client")

# Adicionar o diretório 'mcp-client' ao sys.path
if mcp_client_actual_dir not in sys.path:
    sys.path.insert(0, mcp_client_actual_dir)

# Assegure-se de que mcp_client.py esteja no mesmo diretório ou PYTHONPATH
# e que suas inicializações (load_dotenv, openai_client, MCP_SERVERS, cross_encoder)
# ocorram no nível do módulo para serem acessíveis na importação.
from mcp_client import async_rag_mcp_response, DEEPSEEK_API_KEY, MCP_SERVERS, RERANKING_ENABLED
from striprtf.striprtf import rtf_to_text

import logging

# Configurar logging para o script de batch
logger = logging.getLogger("batch_processor")
if not logger.hasHandlers(): # Evitar adicionar handlers múltiplos se o módulo for recarregado
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("batch_processor.log", mode='w')
        ]
    )

# --- Configurações ---
RTF_FILE_PATH = Path("perguntas-respostas-fine-tuning.rtf")
# Salvar em um novo arquivo para evitar perda de dados no original
OUTPUT_RTF_FILE_PATH = Path("perguntas-respostas-ANTERIORES-fine-tuning.rtf")
# Mude para True se quiser que o script obtenha novas respostas mesmo que já existam
OVERWRITE_EXISTING_ANSWERS = False
# --- Fim das Configurações ---

def load_and_convert_rtf_to_text(filepath: Path) -> str:
    """Lê um arquivo RTF, converte para texto plano e retorna o texto."""
    logger.info(f"Carregando e convertendo arquivo RTF: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            rtf_content = f.read()
        
        # Se o conteúdo já parecer texto plano (contém "## Pergunta")
        if "## Pergunta" in rtf_content[:500]: # Checa o início do arquivo
             logger.info("Arquivo parece ser texto plano ou RTF muito simples. Usando conteúdo diretamente.")
             text_content = rtf_content
        else:
            text_content = rtf_to_text(rtf_content, errors="ignore")

        if not text_content.strip() and rtf_content.strip():
            logger.warning("Conversão RTF para texto resultou em conteúdo vazio, mas arquivo original não estava. Usando conteúdo original como fallback.")
            text_content = rtf_content
        elif not text_content.strip() and not rtf_content.strip():
            logger.warning("Arquivo RTF e sua conversão para texto estão vazios.")
            return ""
            
        return text_content
    except FileNotFoundError:
        logger.error(f"Arquivo RTF não encontrado: {filepath}")
        raise
    except Exception as e:
        logger.error(f"Erro ao carregar ou converter RTF '{filepath}': {e}. Tentando ler como texto plano.")
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception as plain_read_e:
            logger.error(f"Erro ao ler como texto plano: {plain_read_e}")
            raise plain_read_e from e

def parse_qa_structure(text_content: str) -> list:
    """
    Parseia o conteúdo textual para extrair perguntas e respostas existentes.
    Retorna uma lista de dicionários, onde cada dicionário pode ser
    um bloco de texto ou um bloco de Pergunta/Resposta.
    """
    parsed_blocks = []
    current_pos = 0
    
    # Regex para encontrar "## Pergunta N" seguido por seu texto,
    # e "## Resposta N" seguido por seu texto (que pode ser vazio).
    # Captura todo o bloco de P&R.
    qa_block_pattern = re.compile(
        r"(## Pergunta\s*(\d+)\s*\n(.*?)\n## Resposta\s*\2\s*\n(.*?))(?=\n## Pergunta\s*\d+\s*\n|\Z)",
        re.DOTALL | re.MULTILINE
    )

    for match in qa_block_pattern.finditer(text_content):
        # Adiciona texto não-QA que veio antes deste bloco
        if match.start() > current_pos:
            parsed_blocks.append({"type": "text", "content": text_content[current_pos:match.start()]})

        numero = match.group(2)
        pergunta_texto = match.group(3).strip()
        resposta_texto_atual = match.group(4).strip()
        
        parsed_blocks.append({
            "type": "qa",
            "numero": numero,
            "pergunta_texto": pergunta_texto,
            "resposta_texto_atual": resposta_texto_atual,
            "original_full_block": match.group(1) # O bloco completo como encontrado
        })
        current_pos = match.end()
    
    # Adiciona qualquer texto restante no final do arquivo
    if current_pos < len(text_content):
        parsed_blocks.append({"type": "text", "content": text_content[current_pos:]})
        
    num_qa = len([b for b in parsed_blocks if b['type'] == 'qa'])
    logger.info(f"Parseados {num_qa} blocos de Pergunta/Resposta.")
    if num_qa == 0 and text_content.strip():
        logger.warning("Nenhum bloco de P&R encontrado. Verifique o formato do arquivo de entrada ou o regex.")
        # Adiciona todo o conteúdo como um único bloco de texto se nenhum QA for encontrado
        if not parsed_blocks or (len(parsed_blocks) == 1 and parsed_blocks[0]["type"] == "text" and not parsed_blocks[0]["content"].strip()):
            parsed_blocks = [{"type": "text", "content": text_content}]


    return parsed_blocks

async def generate_answers_and_reconstruct_rtf(
    rtf_filepath: Path, 
    output_filepath: Path, 
    overwrite_answers: bool = False
):
    """
    Processa o arquivo RTF: lê perguntas, obtém respostas para as que estão vazias
    (ou todas, se overwrite_answers=True), e salva em um novo arquivo RTF.
    """
    text_content = load_and_convert_rtf_to_text(rtf_filepath)
    if not text_content.strip():
        logger.error(f"Conteúdo de '{rtf_filepath}' está vazio ou não pôde ser lido.")
        return

    parsed_structure = parse_qa_structure(text_content)
    
    final_text_parts = []

    for block in parsed_structure:
        if block["type"] == "text":
            final_text_parts.append(block["content"])
        
        elif block["type"] == "qa":
            numero = block["numero"]
            pergunta_texto = block["pergunta_texto"]
            resposta_texto_atual = block["resposta_texto_atual"]

            fetch_new_answer = overwrite_answers or not resposta_texto_atual.strip()

            if fetch_new_answer:
                logger.info(f"Processando Pergunta {numero}: {pergunta_texto[:100].replace('\\n', ' ')}...")
                try:
                    # Chama a função do mcp_client para obter a resposta.
                    # O 'history' é geralmente para o chatbot Gradio, pode ser [] aqui.
                    # 'mode="aggregated"' é para obter a resposta consolidada.
                    nova_resposta = await async_rag_mcp_response(message=pergunta_texto, history=[], mode="aggregated")
                    
                    logger.info(f"Resposta para Pergunta {numero} obtida (tamanho: {len(nova_resposta)}).")
                    # Formata o bloco de P&R com a nova resposta
                    # Adicionamos duas newlines ao final para separar do próximo bloco.
                    qa_block_text = (
                        f"## Pergunta {numero}\n{pergunta_texto}\n\n"
                        f"## Resposta {numero}\n{nova_resposta.strip()}\n\n"
                    )
                    final_text_parts.append(qa_block_text)

                except Exception as e:
                    logger.error(f"Erro ao obter resposta para Pergunta {numero}: {e}", exc_info=True)
                    # Em caso de erro, mantém o bloco original
                    final_text_parts.append(block["original_full_block"])
            else:
                logger.info(f"Mantendo resposta existente para Pergunta {numero}.")
                final_text_parts.append(block["original_full_block"]) # Mantém o bloco original

    reconstructed_text_content = "".join(final_text_parts)

    # Cria um RTF básico encapsulando o texto plano.
    # Isso não preservará formatação RTF complexa do original.
    rtf_header = f"{{\\rtf1\\ansi\\deff0\\nouicompat\n{{\\fonttbl{{\\f0\\fnil\\fcharset0 Calibri;}}}}\n\\viewkind4\\uc1 \n"
    rtf_footer = "\n}"
    
    # Escapa caracteres especiais RTF e converte newlines para \\par
    rtf_body = reconstructed_text_content.replace('\\\\', '\\\\\\\\') # Escapa barras existentes
    rtf_body = rtf_body.replace('{', '\\\\{').replace('}', '\\\\}') # Escapa chaves
    # Converte newlines. \n sozinhos para \par. \n\n para \par\par.
    # Uma forma mais simples: tratar cada linha como um parágrafo.
    lines = rtf_body.split('\\n')
    rtf_body_pars = '\\n\\par\n'.join(lines) # \\par para nova linha RTF
    
    final_rtf_content = rtf_header + rtf_body_pars + rtf_footer
    
    try:
        output_filepath.parent.mkdir(parents=True, exist_ok=True) # Garante que o diretório de saída exista
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(final_rtf_content)
        logger.info(f"Arquivo RTF com respostas processadas salvo em: {output_filepath}")
    except Exception as e:
        logger.error(f"Erro ao salvar arquivo RTF final em '{output_filepath}': {e}")

async def main():
    """Função principal para executar o processamento em batch."""
    # Verifica se as dependências globais do mcp_client estão prontas
    
    # DEBUG PRINT:
    print(f"[DEBUG] Valor de OVERWRITE_EXISTING_ANSWERS no início de main(): {OVERWRITE_EXISTING_ANSWERS}")
    
    if not DEEPSEEK_API_KEY:
        logger.error("DEEPSEEK_API_KEY não está configurada. Verifique o .env e as importações.")
        return
    if not MCP_SERVERS:
        logger.error("MCP_SERVERS não está configurado.")
        return
    # RERANKING_ENABLED é importado e usado diretamente por async_rag_mcp_response

    logger.info(f"Iniciando processamento em batch do arquivo: {RTF_FILE_PATH}")
    logger.info(f"As respostas serão salvas em: {OUTPUT_RTF_FILE_PATH}")
    if OVERWRITE_EXISTING_ANSWERS:
        logger.info("O modo de sobrescrever respostas existentes está ATIVADO.")
    else:
        logger.info("O modo de sobrescrever respostas existentes está DESATIVADO (respostas existentes não serão alteradas).")

    await generate_answers_and_reconstruct_rtf(
        RTF_FILE_PATH, 
        OUTPUT_RTF_FILE_PATH, 
        overwrite_answers=OVERWRITE_EXISTING_ANSWERS
    )
    logger.info("Processamento em batch concluído.")

if __name__ == "__main__":
    # Importante: Este script assume que os servidores MCP (Telebras, CEITEC, IMBEL)
    # já estão em execução e acessíveis nas URLs configuradas em MCP_SERVERS.
    
    # O loop de eventos asyncio é necessário para as chamadas await.
    asyncio.run(main()) 