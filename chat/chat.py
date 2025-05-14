import os
import sys
import gradio as gr
import requests
from dotenv import load_dotenv
from openai import OpenAI

# Adicionar o diretório raiz do projeto ao path ANTES de qualquer importação local
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print(f"Adicionado {project_root} ao sys.path")

# Carrega variáveis de ambiente
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# Configuração do cliente OpenAI para usar com DeepSeek
client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=DEEPSEEK_API_KEY
)

# Função para resposta do DeepSeek
def deepseek_response(message, history):
    try:
        # Iniciar com a mensagem do sistema
        messages = [
            {
                "role": "system",
                "content": """Você é um assistente em português do Brasil. 
                REGRAS IMPORTANTES:
                1. SEMPRE responda em português do Brasil
                2. Mesmo que a pergunta seja em outro idioma, responda em português
                3. Nunca responda no idioma da pergunta se não for português
                4. Mantenha suas respostas claras e diretas
                5. Use o contexto das mensagens anteriores para manter a coerência"""
            }
        ]

        # Processar histórico mantendo a ordem cronológica
        if history:
            for msg in history:
                if isinstance(msg, dict):  # Novo formato (type='messages')
                    messages.append(msg)
                else:  # Formato antigo (tuplas)
                    user_msg, assistant_msg = msg
                    messages.append({"role": "user", "content": user_msg})
                    messages.append(
                        {"role": "assistant", "content": assistant_msg})

        # Adicionar nova mensagem
        messages.append({"role": "user", "content": message})

        print(f"Contexto atual: {len(messages)} mensagens")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.7,
            max_tokens=2000,
            stream=False
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Erro detalhado: {str(e)}")
        return f"Erro ao processar a requisição: {str(e)}"

# Função para resposta do RAG
def rag_chat_response(message, history):
    try:
        print(f"Enviando requisição para a API RAG: {message}")
        response = requests.post(
            "http://localhost:8010/query",
            json={"query": message},
            timeout=60  # Aumentar timeout para 60 segundos
        )
        print(f"Resposta recebida com status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            answer = data["answer"]
            sources = data["sources"]

            # Formatar resposta com as fontes
            full_response = f"{answer}\n\nFontes:\n" + \
                "\n".join([f"- {s}" for s in sources])
            return full_response
        else:
            print(f"Erro da API RAG: {response.text}")
            return f"Erro na API: {response.status_code}"

    except Exception as e:
        print(f"Erro ao conectar com a API RAG: {str(e)}")
        return f"Erro ao conectar com a API: {str(e)}"

# Criando a interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("# Sistema de consulta de dados CID")
    gr.Markdown("## Chatbot DeepSeek e RAG - MGI")

    with gr.Tab("Chat DeepSeek"):
        deepseek_chatbot = gr.ChatInterface(
            deepseek_response,
            chatbot=gr.Chatbot(height=400, type='messages'),
            textbox=gr.Textbox(
                placeholder="Digite sua mensagem aqui...", container=False),
            title="Chat DeepSeek",
            type='messages'
        )

    with gr.Tab("Chat RAG - TELEBRAS"):
        rag_chatbot = gr.ChatInterface(
            rag_chat_response,
            chatbot=gr.Chatbot(height=400, type='messages'),
            textbox=gr.Textbox(
                placeholder="Digite sua pergunta sobre TELEBRAS...",
                container=False
            ),
            title="Chat RAG - TELEBRAS",
            type='messages'
        )

if __name__ == "__main__":
    try:
        # Obter a porta da variável de ambiente
        port = int(os.environ.get("PORT", os.environ.get("CHAT_PORT", 8525)))
        
        print(f"\n====== INICIANDO SERVIDOR CHAT NA PORTA: {port} ======\n")
        
        # Tentar iniciar na porta especificada
        try:
            demo.launch(
                share=False,
                server_name="0.0.0.0",
                server_port=port,
                show_error=True
            )
        except OSError as e:
            print(f"ERRO ao iniciar na porta {port}: {e}")
            
            # Tentar portas alternativas se a especificada falhar
            for alt_port in range(8520, 8532):
                if alt_port != port:
                    try:
                        print(f"Tentando porta alternativa {alt_port}...")
                        demo.launch(
                            share=False,
                            server_name="0.0.0.0",
                            server_port=alt_port,
                            show_error=True
                        )
                        print(f"\n====== SERVIDOR INICIADO NA PORTA: {alt_port} ======\n")
                        break
                    except OSError:
                        continue
    
    except Exception as e:
        print(f"Erro fatal ao iniciar o servidor: {str(e)}")
        sys.exit(1)
