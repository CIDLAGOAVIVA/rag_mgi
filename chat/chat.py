import os
import gradio as gr
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

    with gr.Tab("Chat RAG - IMBEL/CEITEC/TELEBRAS"):
        custom_chatbot = gr.ChatInterface(
            custom_api_response,
            # Adicionado type='messages'
            chatbot=gr.Chatbot(height=400, type='messages'),
            textbox=gr.Textbox(
                placeholder="Digite sua mensagem aqui...", container=False),
            title="Chat RAG - IMBEL/CEITEC/TELEBRAS",
            type='messages'  # Adicionando o tipo explicitamente
        )

if __name__ == "__main__":
    try:
        demo.launch(share=False, server_name="0.0.0.0", server_port=8520)
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {str(e)}")
        raise
