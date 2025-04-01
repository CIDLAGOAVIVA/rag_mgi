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
        messages = [
            {
                "role": "system",
                "content": """Você é um assistente em português do Brasil. 
                REGRAS IMPORTANTES:
                1. SEMPRE responda em português do Brasil
                2. Mesmo que a pergunta seja em outro idioma, responda em português
                3. Nunca responda no idioma da pergunta se não for português
                4. Mantenha suas respostas claras e diretas"""
            }
        ]
        
        # Novo formato para processar o histórico
        if history:
            for msg in history:
                # Cada mensagem agora é um dicionário com 'role' e 'content'
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
        
        # Adicionar a mensagem atual
        messages.append({
            "role": "user",
            "content": f"{message}\n[RESPONDA EM PORTUGUÊS DO BRASIL]"
        })
        
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.7,
            max_tokens=2000,
            stream=False
        )
        
        return response.choices[0].message.content

    except Exception as e:
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
            chatbot=gr.Chatbot(height=400, type='messages'),  # Adicionado type='messages'
            textbox=gr.Textbox(placeholder="Digite sua mensagem aqui...", container=False),
            title="Chat DeepSeek",
        )
    
    with gr.Tab("Chat API Customizada"):
        custom_chatbot = gr.ChatInterface(
            custom_api_response,
            chatbot=gr.Chatbot(height=400, type='messages'),  # Adicionado type='messages'
            textbox=gr.Textbox(placeholder="Digite sua mensagem aqui...", container=False),
            title="Chat API Customizada",
        )

if __name__ == "__main__":
    # Tenta diferentes portas se a 7860 estiver ocupada
    for port in range(7860, 7870):
        try:
            demo.launch(share=False, server_name="0.0.0.0", server_port=port)
            break
        except OSError:
            if port == 7869:  # Última tentativa
                print("Não foi possível encontrar uma porta disponível entre 7860-7869")
                raise
            continue
