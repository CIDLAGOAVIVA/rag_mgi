import os
import gradio as gr
import requests
from dotenv import load_dotenv
from openai import OpenAI
import json
import os.path
import sqlite3
import sys
import datetime  # Adicione esta importação se estiver faltando

# Adicionar o diretório raiz do projeto ao path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Importar auth necessários
from auth.models import SessionLocal, User

# Carrega variáveis de ambiente
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# Configuração do cliente OpenAI para usar com DeepSeek
client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=DEEPSEEK_API_KEY
)

# Variável global para armazenar o usuário atual
current_user = None

# Função para realizar login
def login(username, password):
    db = None
    try:
        db = SessionLocal()
        user = db.query(User).filter(User.username == username).first()
        
        if not user or not User.verify_password(password, user.hashed_password):
            return False, "Nome de usuário ou senha incorretos"
        
        # Atualizar último login
        global current_user
        current_user = user  # Salva o usuário para uso global
        
        # Atualiza o último login e commita enquanto a sessão está ativa
        user.last_login = datetime.datetime.now()
        db.commit()
        
        # Importante: depois do commit, o objeto user ainda está vinculado à sessão
        # Extraia os dados necessários do usuário antes de fechar a sessão
        username_to_display = user.username  # Se precisar usar algo do objeto user depois
        
        return True, f"Login bem-sucedido! Bem-vindo(a), {username_to_display}!"
    except Exception as e:
        return False, f"Erro ao fazer login: {str(e)}"
    finally:
        if db:
            db.close()

# Função para registro de usuário
def register(username, email, password, confirm_password):
    db = None  # Inicializa db como None para evitar UnboundLocalError
    try:
        if password != confirm_password:
            return False, "As senhas não coincidem"
            
        if len(password) < 6:
            return False, "A senha deve ter pelo menos 6 caracteres"
            
        db = SessionLocal()
        
        # Verificar se o usuário já existe
        existing_user = db.query(User).filter(
            (User.username == username) | (User.email == email)
        ).first()
        
        if existing_user:
            if existing_user.username == username:
                return False, "Nome de usuário já está sendo usado"
            else:
                return False, "Email já está sendo usado"
                
        # Criar novo usuário
        hashed_password = User.get_password_hash(password)
        new_user = User(
            username=username,
            email=email,
            hashed_password=hashed_password
        )
        
        db.add(new_user)
        db.commit()
        
        return True, f"Registro concluído com sucesso! Você pode fazer login agora, {username}!"
    except Exception as e:
        return False, f"Erro ao registrar: {str(e)}"
    finally:
        if db:  # Verifica se db foi inicializado antes de tentar fechá-lo
            db.close()

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

def rag_chat_response(message, history):
    try:
        response = requests.post(
            "http://localhost:8099/query",
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

# Função para alternar entre as abas de login e registro
def switch_tab():
    return gr.Tabs(selected=1) if is_login_tab.value else gr.Tabs(selected=0)

# Variável para armazenar o estado atual da aba
is_login_tab = gr.State(True)

# Função para verificar se o usuário está logado
def check_auth(username=""):
    global current_user
    if current_user:
        return gr.update(visible=False), gr.update(visible=True), f"Usuário: {current_user.username}"
    else:
        return gr.update(visible=True), gr.update(visible=False), ""

def logout():
    global current_user
    current_user = None
    return gr.update(visible=True), gr.update(visible=False), ""

# Criando a interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("# Sistema de consulta de dados CID")
    gr.Markdown("## Autenticação e Chatbot RAG - MGI")

    user_info = gr.Textbox(label="", visible=False)
    
    # Componentes de autenticação
    with gr.Group(visible=True) as auth_container:
        with gr.Tabs() as auth_tabs:
            with gr.TabItem("Login") as login_tab:
                login_username = gr.Textbox(label="Nome de usuário")
                login_password = gr.Textbox(label="Senha", type="password")
                login_button = gr.Button("Login")
                login_message = gr.Textbox(label="Status", interactive=False)
                gr.Markdown("Não tem uma conta? Vá para a aba de registro.")
                
            with gr.TabItem("Registro") as register_tab:
                register_username = gr.Textbox(label="Nome de usuário")
                register_email = gr.Textbox(label="Email")
                register_password = gr.Textbox(label="Senha", type="password")
                register_confirm = gr.Textbox(label="Confirmar senha", type="password")
                register_button = gr.Button("Registrar")
                register_message = gr.Textbox(label="Status", interactive=False)
                gr.Markdown("Já tem uma conta? Vá para a aba de login.")
    
    # Container do chat (inicialmente escondido)
    with gr.Group(visible=False) as chat_container:
        with gr.Row():
            logout_button = gr.Button("Logout")
        
        with gr.Tabs() as chat_tabs:
            with gr.TabItem("Chat DeepSeek"):
                deepseek_chatbot = gr.ChatInterface(
                    deepseek_response,
                    chatbot=gr.Chatbot(height=400, type='messages'),
                    textbox=gr.Textbox(
                        placeholder="Digite sua mensagem aqui...", container=False),
                    title="Chat DeepSeek",
                    type='messages'
                )

            with gr.TabItem("Chat RAG - TELEBRAS"):
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

    # Lógica de eventos
    login_button.click(
        login, 
        inputs=[login_username, login_password], 
        outputs=[login_message]
    ).success(
        check_auth, 
        inputs=[login_username], 
        outputs=[auth_container, chat_container, user_info]
    )
    
    register_button.click(
        register,
        inputs=[register_username, register_email, register_password, register_confirm],
        outputs=[register_message]
    )
    
    logout_button.click(
        logout,
        outputs=[auth_container, chat_container, user_info]
    )

if __name__ == "__main__":
    try:
        # Tentar portas alternativas se a 8520 estiver em uso
        ports = [8520, 8521, 8522, 8523, 8524, 8525, 8526, 8527, 8528, 8529, 8530]

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
