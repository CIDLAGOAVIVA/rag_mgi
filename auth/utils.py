import re
from typing import Tuple, Dict, Any

def validate_email(email: str) -> bool:
    """Valida um endereço de email usando uma expressão regular simples."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_username(username: str) -> bool:
    """
    Valida um nome de usuário.
    Regras:
    - Pelo menos 3 caracteres
    - No máximo 20 caracteres
    - Apenas letras, números e underscores
    """
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    return bool(re.match(pattern, username))

def validate_password(password: str) -> Tuple[bool, str]:
    """
    Valida uma senha.
    Regras:
    - Pelo menos 8 caracteres
    - Pelo menos uma letra maiúscula
    - Pelo menos uma letra minúscula
    - Pelo menos um número
    """
    if len(password) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."
    
    if not re.search(r'[A-Z]', password):
        return False, "A senha deve ter pelo menos uma letra maiúscula."
    
    if not re.search(r'[a-z]', password):
        return False, "A senha deve ter pelo menos uma letra minúscula."
    
    if not re.search(r'[0-9]', password):
        return False, "A senha deve ter pelo menos um número."
    
    return True, ""

def validate_registration_data(data: Dict[str, Any]) -> Tuple[bool, Dict[str, str]]:
    """
    Valida os dados de registro de usuário.
    
    Args:
        data: Dicionário contendo os dados de registro.
        
    Returns:
        Tupla (sucesso, erros), onde:
        - sucesso: True se todos os dados são válidos, False caso contrário.
        - erros: Dicionário mapeando campos para mensagens de erro.
    """
    errors = {}
    
    # Validar username
    if 'username' not in data or not data['username']:
        errors['username'] = "O nome de usuário é obrigatório."
    elif not validate_username(data['username']):
        errors['username'] = "Nome de usuário inválido. Use apenas letras, números e underscores (3-20 caracteres)."
    
    # Validar email
    if 'email' not in data or not data['email']:
        errors['email'] = "O email é obrigatório."
    elif not validate_email(data['email']):
        errors['email'] = "Endereço de email inválido."
    
    # Validar senha
    if 'password' not in data or not data['password']:
        errors['password'] = "A senha é obrigatória."
    else:
        password_valid, password_error = validate_password(data['password'])
        if not password_valid:
            errors['password'] = password_error
    
    # Validar confirmação de senha
    if 'password2' not in data or data['password'] != data['password2']:
        errors['password2'] = "As senhas não coincidem."
    
    # Campos opcionais não precisam de validação rigorosa
    
    return len(errors) == 0, errors