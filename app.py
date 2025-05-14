import os
import sys
import uvicorn
from fastapi import FastAPI, Request, Response, Form, Cookie, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse
from typing import Optional, Dict, Any
import json

# Adicionar o diretório raiz do projeto ao path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Importar componentes de autenticação
from auth.models import User
from auth.auth import authenticate_user, get_current_user, end_session, create_session
from auth.utils import validate_registration_data

# Variável global para armazenar a porta atual do chat Gradio
CHAT_PORT = int(os.environ.get("CHAT_PORT", "8520"))

# Criar o app FastAPI
app = FastAPI(title="RAG MGI - Sistema de Chat")

# Montar diretórios estáticos e templates
app.mount("/static", StaticFiles(directory=os.path.join(project_root, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(project_root, "templates"))

# Middleware para injetar o usuário atual em todas as requisições
@app.middleware("http")
async def add_current_user_to_request(request: Request, call_next):
    # Obter o token da sessão através do cookie
    session_token = request.cookies.get("session")
    
    # Se houver um token, verificar se é válido e obter o usuário
    if session_token:
        request.state.user = get_current_user(session_token)
    else:
        request.state.user = None
        
    # Continuar com a próxima middleware ou rota
    response = await call_next(request)
    return response

# Função auxiliar para verificar se o usuário está autenticado
async def require_login(request: Request):
    """Verifica se o usuário está autenticado e retorna o objeto do usuário."""
    user = getattr(request.state, "user", None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            headers={"Location": "/login?next=" + request.url.path}
        )
    return user

# Rotas
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Página inicial."""
    return templates.TemplateResponse(
        "base.html",
        {"request": request, "current_user": request.state.user}
    )

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, error: str = None, username: str = None):
    """Página de login."""
    # Se o usuário já está autenticado, redirecionar para o chat
    if request.state.user:
        return RedirectResponse(url="/chat", status_code=status.HTTP_302_FOUND)
        
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": error, "username": username, "current_user": None}
    )

@app.post("/login", response_class=HTMLResponse)
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    remember_me: bool = Form(False)
):
    """Processar login."""
    # Obter o endereço IP do cliente para registro
    ip_address = request.client.host
    
    # Tentar autenticar o usuário
    user, session_token = authenticate_user(username, password, ip_address)
    
    if not user or not session_token:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": "Nome de usuário/email ou senha incorretos",
                "username": username,
                "current_user": None
            }
        )
    
    # Criar resposta de redirecionamento
    response = RedirectResponse(url="/chat", status_code=status.HTTP_302_FOUND)
    
    # Adicionar cookie de sessão
    max_age = 30 * 24 * 60 * 60 if remember_me else None  # 30 dias se lembrar, senão sessão do navegador
    response.set_cookie(
        key="session",
        value=session_token,
        httponly=True,
        max_age=max_age,
        samesite="lax"
    )
    
    return response

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    """Página de registro."""
    # Se o usuário já está autenticado, redirecionar para o chat
    if request.state.user:
        return RedirectResponse(url="/chat", status_code=status.HTTP_302_FOUND)
        
    return templates.TemplateResponse(
        "register.html",
        {"request": request, "errors": {}, "data": {}, "current_user": None}
    )

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request):
    """Processar registro."""
    # Obter o formulário
    form_data = await request.form()
    data = {k: v for k, v in form_data.items()}
    
    # Validar os dados
    is_valid, errors = validate_registration_data(data)
    
    if not is_valid:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "errors": errors, "data": data, "current_user": None}
        )
    
    # Verificar se o nome de usuário ou email já existem
    if User.get_by_username(data["username"]):
        errors["username"] = "Este nome de usuário já está em uso."
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "errors": errors, "data": data, "current_user": None}
        )
    
    if User.get_by_email(data["email"]):
        errors["email"] = "Este email já está registrado."
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "errors": errors, "data": data, "current_user": None}
        )
    
    # Criar o usuário
    user = User.create(
        username=data["username"],
        email=data["email"],
        password=data["password"],
        first_name=data.get("first_name"),
        last_name=data.get("last_name")
    )
    
    if not user:
        return templates.TemplateResponse(
            "register.html",
            {
                "request": request,
                "errors": {"general": "Erro ao criar usuário. Tente novamente."},
                "data": data,
                "current_user": None
            }
        )
    
    # Criar sessão para o novo usuário
    session_token = create_session(user)
    
    # Redirecionar para o chat com cookie de sessão
    response = RedirectResponse(url="/chat", status_code=status.HTTP_302_FOUND)
    response.set_cookie(
        key="session",
        value=session_token,
        httponly=True,
        samesite="lax"
    )
    
    return response

@app.get("/logout")
async def logout(request: Request, session: str = Cookie(None)):
    """Encerrar a sessão."""
    if session:
        end_session(session)
    
    # Redirecionar para a página inicial e limpar o cookie de sessão
    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    response.delete_cookie(key="session")
    
    return response

@app.get("/chat", response_class=HTMLResponse)
async def chat_page(current_user: User = Depends(require_login), request: Request = None):
    """Página do chat (requer autenticação)."""
    
    # Usar o template de redirecionamento que já existe
    return templates.TemplateResponse(
        "chat_redirect.html",
        {
            "request": request, 
            "current_user": current_user,
            "chat_port": CHAT_PORT
        }
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8500)