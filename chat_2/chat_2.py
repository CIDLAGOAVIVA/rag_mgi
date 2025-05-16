import os
import time
import json
import asyncio
import traceback
import logging
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("chat_client.log", mode='w')
    ]
)
logger = logging.getLogger("rag_chat")

# FastMCP v2 importações
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

# Variáveis de ambiente
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    logger.error("DEEPSEEK_API_KEY não encontrada. Verifique o arquivo .env")

# Cliente OpenAI para DeepSeek
openai_client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=DEEPSEEK_API_KEY
)

# Configurações dos servidores MCP (descrições abreviadas para o exemplo)
MCP_SERVERS = {
    "TELEBRAS": {"url": "http://localhost:8011/mcp/", "description": "Conhecimento TELEBRAS."},
    "CEITEC": {"url": "http://localhost:8009/mcp/", "description": "Conhecimento CEITEC."},
    "IMBEL": {"url": "http://localhost:8010/mcp/", "description": "Conhecimento IMBEL."}
}

async def parallel_mcp_query(query: str, max_results: int = 5) -> tuple[dict, list]:
    results = {}
    errors = []

    async def query_server(server_name: str) -> tuple[str, dict]:
        server_config = MCP_SERVERS.get(server_name)
        if not server_config:
            msg = f"Configuração para {server_name} não encontrada."
            logger.error(msg)
            return server_name, {"error": msg}
        try:
            logger.info(f"Consultando {server_name} ({server_config['url']}) com query: '{query[:50]}...'")
            start_time_query = time.time()
            transport = StreamableHttpTransport(url=server_config['url'])
            async with Client(transport=transport) as mcp_client_instance:
                tools_list = await asyncio.wait_for(mcp_client_instance.list_tools(), timeout=15.0)
                tool_name_to_call = f"query_{server_name.lower()}"
                if not any(tool_obj.name == tool_name_to_call for tool_obj in tools_list):
                    available_tools_names = [tool_obj.name for tool_obj in tools_list]
                    msg = f"Ferramenta '{tool_name_to_call}' não encontrada em {server_name}. Disponíveis: {available_tools_names}"
                    logger.error(msg)
                    return server_name, {"error": msg}
                logger.info(f"Chamando '{tool_name_to_call}' em {server_name}...")
                response_content_list = await asyncio.wait_for(
                    mcp_client_instance.call_tool(
                        name=tool_name_to_call,
                        arguments={"query": query, "max_results": max_results}
                    ),
                    timeout=45.0
                )
                response_data = None
                if response_content_list:
                    content_item = response_content_list[0]
                    if hasattr(content_item, 'text'):
                        try:
                            response_data = json.loads(content_item.text)
                        except json.JSONDecodeError as je:
                            raw_text = content_item.text
                            msg = f"Erro ao decodificar JSON de {server_name}: {je}. Recebido: '{raw_text[:200]}...'"
                            logger.error(msg)
                            return server_name, {"error": msg, "raw_response": raw_text}
                    elif isinstance(content_item, dict):
                        response_data = content_item
                
                if isinstance(response_data, dict):
                    logger.info(f"Resposta recebida com sucesso de {server_name}.")
                    return server_name, {
                        "content": {
                            "answer": response_data.get("answer", "N/A"),
                            "sources": response_data.get("sources", []),
                            "processing_time": response_data.get("processing_time", time.time() - start_time_query),
                            "source_server": server_name
                        }
                    }
                else:
                    raw_resp_str = str(response_content_list[0]) if response_content_list else "Lista de conteúdo vazia"
                    msg = f"Formato de dados de resposta inesperado de {server_name}: {type(response_data)}. Conteúdo bruto: '{raw_resp_str[:200]}...'"
                    logger.warning(msg)
                    return server_name, {"error": msg, "raw_response": raw_resp_str}
        except asyncio.TimeoutError:
            msg = f"Timeout ao consultar {server_name}."
            logger.error(msg)
            return server_name, {"error": msg}
        except Exception as e:
            msg = f"Erro ao consultar {server_name}: {type(e).__name__} - {str(e)}"
            logger.error(msg)
            logger.error(traceback.format_exc())
            return server_name, {"error": msg}

    tasks = [query_server(name) for name in MCP_SERVERS.keys()]
    if not tasks:
        logger.warning("Nenhum servidor MCP configurado para consulta.")
        return {}, ["Nenhum servidor configurado"]
    logger.info(f"Iniciando {len(tasks)} consultas MCP paralelas...")
    task_results_tuples = await asyncio.gather(*tasks, return_exceptions=True)
    for i, server_name_key in enumerate(MCP_SERVERS.keys()):
        result_or_exc = task_results_tuples[i]
        if isinstance(result_or_exc, Exception):
            msg = f"Exceção na tarefa de consulta para {server_name_key}: {result_or_exc}"
            logger.error(msg)
            results[server_name_key] = {"error": msg}
            errors.append(msg)
        elif isinstance(result_or_exc, tuple) and len(result_or_exc) == 2:
            actual_server_name, result_dict = result_or_exc
            results[actual_server_name] = result_dict
            if result_dict and "error" in result_dict:
                errors.append(f"{actual_server_name}: {result_dict['error']}")
            elif result_dict and "content" in result_dict:
                 logger.info(f"Consulta a {actual_server_name} bem-sucedida.")
            else:
                msg = f"Resposta inesperada ou malformada de {actual_server_name}: {result_dict}"
                logger.error(msg)
                results[actual_server_name] = {"error": msg}
                errors.append(msg)
        else:
            msg = f"Formato de resultado de tarefa inesperado para {server_name_key}: {result_or_exc}"
            logger.error(msg)
            results[server_name_key] = {"error": msg}
            errors.append(msg)
    return results, errors

def create_consolidated_summary(query: str, results_dict: dict) -> str:
    logger.info(f"Criando resumo consolidado para query: '{query[:50]}...'")
    valid_responses = []
    all_sources = []
    for server_name, result_data in results_dict.items():
        if not result_data or "error" in result_data or "content" not in result_data:
            error_info = result_data.get('error', 'Dados ausentes') if result_data else 'Nulo'
            logger.warning(f"Ignorando {server_name}: {error_info}")
            continue
        answer = result_data["content"].get("answer")
        if not answer:
            logger.warning(f"Resposta vazia de {server_name}, ignorando.")
            continue
        valid_responses.append({"server": server_name, "answer": answer})
        sources = result_data["content"].get("sources", [])
        if sources:
            for source in sources: all_sources.append(f"{server_name}: {source}")
    if not valid_responses:
        logger.error("Nenhuma resposta válida para sintetizar.")
        return "Não foi possível obter informações relevantes."
    logger.info(f"Sintetizando {len(valid_responses)} respostas...")
    system_prompt = "Sintetize as seguintes informações de diferentes fontes (TELEBRAS, CEITEC, IMBEL) sobre empresas estatais brasileiras. Responda em português do Brasil, seja coeso, cite fontes se específico, e não invente dados."
    context_str = "\n\n".join([f"FONTE {r['server']}:\n{r['answer']}" for r in valid_responses])
    user_prompt = f"PERGUNTA: {query}\n\nDADOS DAS FONTES:\n{context_str}\n\nRESPOSTA SINTETIZADA:"
    try:
        logger.info("Enviando para síntese LLM...")
        api_response = openai_client.chat.completions.create(
            model="deepseek-chat", messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}],
            temperature=0.2, max_tokens=3500
        )
        synthesized_answer = api_response.choices[0].message.content
        logger.info(f"Síntese LLM gerada ({len(synthesized_answer)} chars).")
        if all_sources:
            unique_sources = sorted(list(set(all_sources)))[:10]
            return f"{synthesized_answer}\n\n**Fontes:**\n" + "\n".join(f"- {s}" for s in unique_sources)
        return synthesized_answer
    except Exception as e:
        logger.error(f"Erro na síntese LLM: {e}", exc_info=True)
        fallback_answer = "**Respostas Individuais:**\n" + "\n".join(f"**{r['server']}:**\n{r['answer']}" for r in valid_responses)
        if all_sources:
             fallback_answer += "\n\n**Fontes:**\n" + "\n".join(f"- {s}" for s in sorted(list(set(all_sources)))[:10])
        return fallback_answer

async def async_rag_mcp_response(message: str, history: list, mode: str = "aggregated") -> str:
    logger.info(f"Processando consulta (modo: {mode}): '{message[:50]}...'")
    start_time_main = time.time()
    results_data, errors_list = await parallel_mcp_query(message)
    final_response_str = ""

    if not results_data and errors_list:
        return f"Erro: Falha na comunicação com servidores. Detalhes: {'; '.join(errors_list)}"
    elif not results_data:
         return "Erro: Nenhum servidor respondeu."

    all_failed_or_empty = all(
        not rd or "content" not in rd or ("error" in rd) for rd in results_data.values()
    )
    if all_failed_or_empty:
        error_msgs = "; ".join(errors_list) if errors_list else "Respostas vazias/malformadas."
        return f"Erro ao consultar bases: {error_msgs}"

    if mode == "aggregated":
        final_response_str = create_consolidated_summary(message, results_data)
    else:
        if mode in results_data and results_data[mode] and "content" in results_data[mode]:
            content = results_data[mode]["content"]
            answer, sources, proc_time = content.get("answer", "Sem resposta."), content.get("sources", []), content.get("processing_time", 0)
            final_response_str = f"{answer}"
            if sources: final_response_str += "\n\n**Fontes:**\n" + "\n".join(f"- {s}" for s in sorted(list(set(sources)))[:5])
            final_response_str += f"\n\n[{mode}, {proc_time:.2f}s]"
        elif mode in results_data and results_data[mode] and "error" in results_data[mode]:
            final_response_str = f"Erro ({mode}): {results_data[mode]['error']}"
        else:
            final_response_str = f"{mode} não disponível ou resposta inválida."
    
    processing_time_total = time.time() - start_time_main
    logger.info(f"Processamento total da consulta: {processing_time_total:.2f}s.")
    
    if errors_list and (mode != "aggregated" or not any(err_msg.startswith(mode) for err_msg in errors_list)):
        filtered_errors = [e for e in errors_list if not e.startswith(f"{mode}:")] if mode != "aggregated" else errors_list
        if filtered_errors:
            final_response_str += f"\n\nObs: Outros servidores com erros: {', '.join(filtered_errors)}"
    return final_response_str

async def rag_aggregated_response_async(message, history):
    return await async_rag_mcp_response(message, history, "aggregated")

# Deixando as funções específicas comentadas para simplificar a interface inicial
# async def rag_telebras_response_async(message, history):
#     return await async_rag_mcp_response(message, history, "TELEBRAS")
# async def rag_ceitec_response_async(message, history):
#     return await async_rag_mcp_response(message, history, "CEITEC")
# async def rag_imbel_response_async(message, history):
#     return await async_rag_mcp_response(message, history, "IMBEL")

async def check_server_availability(name: str, url: str) -> tuple[bool, list[str] | str]:
    logger.info(f"Verificando servidor {name} em {url}")
    try:
        transport = StreamableHttpTransport(url=url)
        async with Client(transport=transport) as client_check:
            tools = await asyncio.wait_for(client_check.list_tools(), timeout=10.0)
            tool_names = [tool.name for tool in tools]
            logger.info(f"Servidor {name} OK. Ferramentas: {', '.join(tool_names)}")
            return True, tool_names
    except asyncio.TimeoutError:
        msg = f"Timeout MCP ({url})"
        logger.error(msg)
        return False, msg
    except Exception as e:
        msg = f"Erro MCP ({url}): {type(e).__name__}"
        logger.error(msg, exc_info=True)
        return False, msg

def setup_and_launch_gradio():
    with gr.Blocks(title="Chat RAG MGI", theme=gr.themes.Soft()) as demo: # Definindo tema aqui
        gr.Markdown("# Chat RAG Unificado - MGI")
        gr.Markdown("Faça uma pergunta para consultar as bases de conhecimento TELEBRAS, CEITEC e IMBEL.")
        
        gr.ChatInterface(
            rag_aggregated_response_async,
            chatbot=gr.Chatbot(
                height=600, 
                label="Chat Consolidado",
                type='messages', # Especificar para evitar warning
                # bubble_full_width removido pois está obsoleto
            ),
            textbox=gr.Textbox(placeholder="Digite sua pergunta...", container=False, scale=7),
            # Os botões submit, clear, undo são geralmente adicionados por padrão ou configurados no Chatbot.
            # Removendo parâmetros não suportados diretamente pelo ChatInterface.
        )
        
        # Abas específicas comentadas para o teste inicial simplificado
        # with gr.Tab("Chat RAG - TELEBRAS"):
        #     gr.Markdown(MCP_SERVERS["TELEBRAS"]["description"])
        #     gr.ChatInterface(rag_telebras_response_async, chatbot=gr.Chatbot(height=400, label="TELEBRAS", type='messages'))
        # with gr.Tab("Chat RAG - CEITEC"):
        #     gr.Markdown(MCP_SERVERS["CEITEC"]["description"])
        #     gr.ChatInterface(rag_ceitec_response_async, chatbot=gr.Chatbot(height=400, label="CEITEC", type='messages'))
        # with gr.Tab("Chat RAG - IMBEL"):
        #     gr.Markdown(MCP_SERVERS["IMBEL"]["description"])
        #     gr.ChatInterface(rag_imbel_response_async, chatbot=gr.Chatbot(height=400, label="IMBEL", type='messages'))

    env_port = os.getenv("GRADIO_SERVER_PORT")
    port_to_use = 0
    if env_port:
        try:
            port_to_use = int(env_port)
            logger.info(f"Usando porta da variável de ambiente GRADIO_SERVER_PORT: {port_to_use}")
        except ValueError:
            logger.error(f"Valor inválido para GRADIO_SERVER_PORT: '{env_port}'. Usando portas padrão.")
            port_to_use = 0 # Reseta para que tente as portas padrão
    
    if port_to_use > 0:
        try:
            demo.launch(share=False, server_name="0.0.0.0", server_port=port_to_use, show_error=True, debug=True, prevent_thread_lock=True)
            return # Sucesso
        except Exception as e_launch:
            logger.error(f"Erro ao usar porta {port_to_use} da variável de ambiente: {e_launch}", exc_info=True)
            raise # Relança se a porta especificada falhar
            
    ports_to_try = [8520, 8525, 8530, 7860, 7861] # Lista de portas comuns para Gradio
    logger.info(f"Tentando portas para o servidor Gradio: {ports_to_try}")
    for port_val in ports_to_try:
        try:
            logger.info(f"Tentando iniciar Gradio na porta {port_val}...")
            demo.launch(share=False, server_name="0.0.0.0", server_port=port_val, show_error=True, debug=True, prevent_thread_lock=True)
            break 
        except OSError as e_os:
            if "address already in use" in str(e_os).lower() or "cannot assign requested address" in str(e_os).lower():
                logger.warning(f"Porta {port_val} já está em uso ou endereço não pode ser atribuído.")
            else:
                logger.error(f"OSError ao tentar iniciar Gradio na porta {port_val}: {e_os}", exc_info=True)
            if port_val == ports_to_try[-1]:
                logger.critical(f"Falha ao encontrar porta disponível para Gradio.")
                raise
            logger.info("Tentando próxima porta...")
        except Exception as e_other_launch:
            logger.critical(f"Erro inesperado ao tentar iniciar Gradio na porta {port_val}: {e_other_launch}", exc_info=True)
            if port_val == ports_to_try[-1]: raise
            logger.info("Tentando próxima porta...")

async def main():
    logger.info("Iniciando RAG Chat Client...")
    print("Verificando conexão com servidores MCP...")
    all_servers_ok = True
    for name, config in MCP_SERVERS.items():
        print(f"Verificando {name}...")
        available, details = await check_server_availability(name, config["url"])
        if available:
            print(f"✓ {name} OK. Ferramentas: {', '.join(details) if isinstance(details, list) else details}")
        else:
            print(f"✗ {name} FALHA: {details}")
            all_servers_ok = False
    if not all_servers_ok:
        logger.warning("Um ou mais servidores MCP não estão disponíveis.")
    print("Configurando e iniciando interface Gradio...")
    setup_and_launch_gradio()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Aplicação encerrada.")
    except Exception as e_fatal:
        logger.critical(f"Erro fatal: {e_fatal}", exc_info=True)