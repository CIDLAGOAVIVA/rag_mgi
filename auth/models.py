import sqlite3
import os
import hashlib
import uuid
from datetime import datetime
from typing import Optional, Dict, Any, List, Tuple

# Garantir que o diretório para o banco de dados existe
os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.db')

def get_db_connection():
    """Estabelece uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa o banco de dados criando as tabelas necessárias."""
    conn = get_db_connection()
    
    # Criar tabela de usuários
    conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        first_name TEXT,
        last_name TEXT,
        created_at TEXT NOT NULL,
        last_login TEXT,
        is_active BOOLEAN DEFAULT 1
    )
    ''')
    
    # Criar tabela para logs de acesso
    conn.execute('''
    CREATE TABLE IF NOT EXISTS access_logs (
        id TEXT PRIMARY KEY,
        user_id TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        ip_address TEXT,
        action TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')
    
    conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    """Gera um hash seguro da senha."""
    return hashlib.sha256(password.encode()).hexdigest()

class User:
    """Modelo para representar um usuário."""
    
    def __init__(self, id: str, username: str, email: str, password_hash: str,
                 first_name: str = None, last_name: str = None,
                 created_at: str = None, last_login: str = None, is_active: bool = True):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = created_at or datetime.now().isoformat()
        self.last_login = last_login
        self.is_active = is_active
    
    @classmethod
    def create(cls, username: str, email: str, password: str, 
               first_name: str = None, last_name: str = None) -> 'User':
        """Cria um novo usuário no banco de dados."""
        user_id = str(uuid.uuid4())
        password_hash = hash_password(password)
        created_at = datetime.now().isoformat()
        
        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (id, username, email, password_hash, first_name, last_name, created_at) '
                'VALUES (?, ?, ?, ?, ?, ?, ?)',
                (user_id, username, email, password_hash, first_name, last_name, created_at)
            )
            conn.commit()
            
            return cls(
                id=user_id,
                username=username,
                email=email,
                password_hash=password_hash,
                first_name=first_name,
                last_name=last_name,
                created_at=created_at
            )
        except sqlite3.IntegrityError:
            # Usuário ou email já existem
            return None
        finally:
            conn.close()
    
    @classmethod
    def get_by_username(cls, username: str) -> Optional['User']:
        """Busca um usuário pelo nome de usuário."""
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if user:
            return cls(**dict(user))
        return None
    
    @classmethod
    def get_by_email(cls, email: str) -> Optional['User']:
        """Busca um usuário pelo email."""
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()
        
        if user:
            return cls(**dict(user))
        return None
    
    @classmethod
    def get_by_id(cls, user_id: str) -> Optional['User']:
        """Busca um usuário pelo ID."""
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()
        
        if user:
            return cls(**dict(user))
        return None
    
    def verify_password(self, password: str) -> bool:
        """Verifica se a senha está correta."""
        return self.password_hash == hash_password(password)
    
    def update_last_login(self, ip_address: str = None) -> None:
        """Atualiza o timestamp do último login."""
        timestamp = datetime.now().isoformat()
        conn = get_db_connection()
        
        # Atualiza o timestamp de último login
        conn.execute(
            'UPDATE users SET last_login = ? WHERE id = ?',
            (timestamp, self.id)
        )
        
        # Registra o log de acesso
        log_id = str(uuid.uuid4())
        conn.execute(
            'INSERT INTO access_logs (id, user_id, timestamp, ip_address, action) '
            'VALUES (?, ?, ?, ?, ?)',
            (log_id, self.id, timestamp, ip_address, 'login')
        )
        
        conn.commit()
        conn.close()
        self.last_login = timestamp

# Inicializar o banco de dados ao importar o módulo
init_db()