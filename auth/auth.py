import uuid
import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

from .models import User, get_db_connection

# Armazenamento simples em memória para sessões
# Em produção, seria melhor usar Redis ou outro armazenamento persistente
sessions = {}

def generate_session_token() -> str:
    """Gera um token de sessão aleatório."""
    return secrets.token_urlsafe(32)

def create_session(user: User, expiry_days: int = 1) -> str:
    """
    Cria uma sessão para o usuário fornecido.
    
    Args:
        user: O objeto usuário.
        expiry_days: Número de dias até a expiração da sessão.
        
    Returns:
        O token de sessão gerado.
    """
    session_token = generate_session_token()
    expiry = datetime.now() + timedelta(days=expiry_days)
    
    sessions[session_token] = {
        'user_id': user.id,
        'expires': expiry
    }
    
    return session_token

def validate_session(session_token: str) -> Optional[str]:
    """
    Valida um token de sessão e retorna o ID do usuário se válido.
    
    Args:
        session_token: O token de sessão a ser validado.
        
    Returns:
        O ID do usuário se o token for válido, None caso contrário.
    """
    if session_token not in sessions:
        return None
    
    session = sessions[session_token]
    
    if datetime.now() > session['expires']:
        # Sessão expirada
        del sessions[session_token]
        return None
    
    return session['user_id']

def get_current_user(session_token: str) -> Optional[User]:
    """
    Retorna o usuário atual com base no token de sessão.
    
    Args:
        session_token: O token de sessão.
        
    Returns:
        O objeto usuário se o token for válido, None caso contrário.
    """
    user_id = validate_session(session_token)
    
    if not user_id:
        return None
    
    return User.get_by_id(user_id)

def end_session(session_token: str) -> bool:
    """
    Encerra uma sessão.
    
    Args:
        session_token: O token de sessão a ser encerrado.
        
    Returns:
        True se a sessão foi encerrada com sucesso, False caso contrário.
    """
    if session_token in sessions:
        del sessions[session_token]
        return True
    
    return False

def authenticate_user(username: str, password: str, ip_address: str = None) -> tuple[Optional[User], Optional[str]]:
    """
    Autentica um usuário com nome de usuário e senha.
    
    Args:
        username: Nome de usuário.
        password: Senha.
        ip_address: Endereço IP do requisitante (opcional).
        
    Returns:
        Tupla (User, session_token) se autenticação bem-sucedida, (None, None) caso contrário.
    """
    # Verifica se a entrada é email ou nome de usuário
    if '@' in username:
        user = User.get_by_email(username)
    else:
        user = User.get_by_username(username)
    
    if not user or not user.verify_password(password):
        return None, None
    
    if not user.is_active:
        return None, None
    
    # Atualiza o último login e registra o acesso
    user.update_last_login(ip_address)
    
    # Cria uma nova sessão
    session_token = create_session(user)
    
    return user, session_token