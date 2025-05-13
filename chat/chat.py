import os
import gradio as gr
import requests
from dotenv import load_dotenv
from openai import OpenAI

# Carrega variáveis de ambiente
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# Configuração do cliente OpenAI para usar com DeepSeek
client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=DEEPSEEK_API_KEY
)


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

        print(f"Contexto atual: {len(messages)} mensagens")  # Debug

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.7,
            max_tokens=2000,
            stream=False
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Erro detalhado: {str(e)}")  # Debug
        return f"Erro ao processar a requisição: {str(e)}"


def custom_api_response(message, history):
    # Aqui iremos implementar a chamada à nossa API customizada
    # Por enquanto, retornamos uma mensagem de placeholder
    return f"API Customizada (será implementada): {message}"


def rag_chat_response(message, history):
    try:
        response = requests.post(
            "http://localhost:8010/query",
            json={"query": message}
        )

        if response.status_code == 200:
            data = response.json()
            answer = data["answer"]
            sources = data["sources"]

            # Formatar resposta com as fontes
            full_response = f"{answer}\n\nFontes:\n" + \
                "\n".join([f"- {s}" for s in sources])
            return full_response
        else:
            return f"Erro na API: {response.status_code}"

    except Exception as e:
        return f"Erro ao conectar com a API: {str(e)}"


# Criando a interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("# Sistema de consulta de dados CID")
    gr.Markdown("## Chatbot DeepSeek e RAG - MGI")

    with gr.Tab("Chat DeepSeek"):
        deepseek_chatbot = gr.ChatInterface(
            deepseek_response,
            # Adicionado type='messages'
            chatbot=gr.Chatbot(height=400, type='messages'),
            textbox=gr.Textbox(
                placeholder="Digite sua mensagem aqui...", container=False),
            title="Chat DeepSeek",
            type='messages'  # Adicionando o tipo explicitamente
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

    # Remove ou comente a antiga implementação do custom_chatbot

if __name__ == "__main__":
    try:
        # Tentar portas alternativas se a 8520 estiver em uso
        ports = [8520, 8521, 8522, 8523, 8524, 8525, 8526, 8527, 8528, 8529, 8530, 8531]

        for port in ports:
            try:
                print(f"Tentando iniciar o servidor na porta {port}...")
                demo.launch(
                    share=False,
                    server_name="0.0.0.0",
                    server_port=port,
                    show_error=True
                )
                break  # Se chegou aqui, o servidor iniciou com sucesso
            except OSError as e:
                if port == ports[-1]:  # Se for a última porta da lista
                    raise OSError(
                        f"Não foi possível encontrar uma porta disponível entre {ports[0]} e {ports[-1]}")
                print(f"Porta {port} em uso, tentando próxima porta...")
                continue

    except Exception as e:
        print(f"Erro ao iniciar o servidor: {str(e)}")
        raise
