#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import signal
import psutil
from pathlib import Path

# Obter o diretório raiz do projeto
project_root = Path(__file__).resolve().parent

def is_port_in_use(port):
    """Verifica se uma porta está em uso."""
    for conn in psutil.net_connections():
        if conn.laddr.port == port and conn.status != 'TIME_WAIT':
            return True
    return False

def find_available_port(start_port, end_port):
    """Encontra uma porta disponível no intervalo especificado."""
    for port in range(start_port, end_port + 1):
        if not is_port_in_use(port):
            return port
    raise ValueError(f"Não foi possível encontrar uma porta disponível entre {start_port} e {end_port}")

def start_services():
    """Inicia os serviços da aplicação."""
    print("Iniciando serviços do RAG MGI...")
    
    # Verificar se as portas estão disponíveis
    auth_port = find_available_port(8500, 8509)
    chat_port = find_available_port(8520, 8529)
    rag_port = 8010  # Porta fixa para o serviço RAG
    
    if is_port_in_use(rag_port):
        print(f"AVISO: A porta {rag_port} para o serviço RAG já está em uso.")
        print("O serviço RAG pode já estar rodando ou pode haver outro serviço nessa porta.")
        print("Tentando usar essa porta mesmo assim...")
    
    print(f"Usando porta {auth_port} para o serviço de autenticação")
    print(f"Usando porta {chat_port} para o serviço de chat")
    print(f"Usando porta {rag_port} para o serviço RAG API")
    
    # Iniciar o servidor RAG API (isso deve ser feito primeiro)
    print("Iniciando o serviço RAG API...")
    rag_process = subprocess.Popen(
        [sys.executable, os.path.join(project_root, "api", "rag_api.py")],
        env={**os.environ, "PORT": str(rag_port)},
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # Aguardar para garantir que o serviço RAG API está rodando
    time.sleep(10)  # Dar mais tempo para o RAG inicializar, pois carrega modelos
    
    # Verificar se o processo RAG está rodando
    if rag_process.poll() is not None:
        print("ERRO: O serviço RAG API falhou ao iniciar.")
        output, _ = rag_process.communicate()
        print(output)
        return None, None, None
    
    print("Serviço RAG API iniciado com sucesso!")
    
    # Iniciar o servidor de autenticação (FastAPI)
    auth_process = subprocess.Popen(
        [sys.executable, os.path.join(project_root, "app.py")],
        env={**os.environ, "PORT": str(auth_port), "CHAT_PORT": str(chat_port)},
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # Aguardar para garantir que o serviço de autenticação está rodando
    time.sleep(2)
    
    # Verificar se o processo está rodando
    if auth_process.poll() is not None:
        print("ERRO: O serviço de autenticação falhou ao iniciar.")
        output, _ = auth_process.communicate()
        print(output)
        rag_process.terminate()
        return None, None, None
    
    print("Serviço de autenticação iniciado com sucesso!")
    
    # Iniciar o servidor de chat (Gradio)
    chat_process = subprocess.Popen(
        [sys.executable, os.path.join(project_root, "chat", "chat.py")],
        env={**os.environ, "PORT": str(chat_port), "CHAT_PORT": str(chat_port)},
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # Aguardar para garantir que o serviço de chat está rodando
    time.sleep(2)
    
    # Verificar se o processo está rodando
    if chat_process.poll() is not None:
        print("ERRO: O serviço de chat falhou ao iniciar.")
        output, _ = chat_process.communicate()
        print(output)
        auth_process.terminate()
        rag_process.terminate()
        return None, None, None
    
    print("Serviço de chat iniciado com sucesso!")
    
    print("\n===================================================")
    print(f"Sistema RAG MGI iniciado!")
    print(f"Acesse a página de login em: http://localhost:{auth_port}")
    print(f"Serviço de chat disponível em: http://localhost:{chat_port}")
    print(f"API RAG disponível em: http://localhost:{rag_port}")
    print("===================================================\n")
    
    return auth_process, chat_process, rag_process

def stop_services(auth_process, chat_process, rag_process):
    """Para os serviços da aplicação."""
    if auth_process and auth_process.poll() is None:
        print("Parando serviço de autenticação...")
        auth_process.terminate()
        auth_process.wait(timeout=5)
    
    if chat_process and chat_process.poll() is None:
        print("Parando serviço de chat...")
        chat_process.terminate()
        chat_process.wait(timeout=5)
    
    if rag_process and rag_process.poll() is None:
        print("Parando serviço RAG API...")
        rag_process.terminate()
        rag_process.wait(timeout=5)
    
    print("Todos os serviços foram encerrados.")

def signal_handler(sig, frame):
    """Manipulador de sinal para SIGINT (Ctrl+C)."""
    print("\nEncerrando os serviços...")
    if 'auth_process' in globals() and 'chat_process' in globals() and 'rag_process' in globals():
        stop_services(auth_process, chat_process, rag_process)
    sys.exit(0)

if __name__ == "__main__":
    # Registrar manipulador de sinal para SIGINT
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        auth_process, chat_process, rag_process = start_services()
        
        if auth_process and chat_process and rag_process:
            print("Pressione Ctrl+C para encerrar os serviços.")
            
            # Manter o script rodando e mostrar logs
            while True:
                # Mostrar logs do RAG
                rag_line = rag_process.stdout.readline()
                if rag_line:
                    print(f"[RAG] {rag_line.strip()}")
                
                # Mostrar logs da autenticação
                auth_line = auth_process.stdout.readline()
                if auth_line:
                    print(f"[AUTH] {auth_line.strip()}")
                
                # Mostrar logs do chat
                chat_line = chat_process.stdout.readline()
                if chat_line:
                    print(f"[CHAT] {chat_line.strip()}")
                
                # Verificar se algum processo morreu
                if auth_process.poll() is not None or chat_process.poll() is not None or rag_process.poll() is not None:
                    print("Um dos serviços foi encerrado inesperadamente. Encerrando...")
                    break
                
                time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\nEncerrando os serviços...")
    finally:
        if 'auth_process' in locals() and 'chat_process' in locals() and 'rag_process' in locals():
            stop_services(auth_process, chat_process, rag_process)