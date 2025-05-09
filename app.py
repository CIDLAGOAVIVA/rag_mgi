import os
import sys
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import threading
import subprocess

# Adicionar o diretório raiz do projeto ao path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from auth.auth import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])

def run_chat_interface():
    chat_script = os.path.join(project_root, "chat", "chat.py")
    subprocess.run([sys.executable, chat_script])

def run_rag_api():
    rag_api_script = os.path.join(project_root, "api", "rag_api.py") 
    subprocess.run([sys.executable, rag_api_script])

if __name__ == "__main__":
    # Iniciar o RAG API em uma thread separada
    rag_thread = threading.Thread(target=run_rag_api)
    rag_thread.daemon = True
    rag_thread.start()
    
    # Iniciar o chat em uma thread separada
    chat_thread = threading.Thread(target=run_chat_interface)
    chat_thread.daemon = True
    chat_thread.start()
    
    # Iniciar a API principal
    uvicorn.run("app:app", host="0.0.0.0", port=8015, reload=False)