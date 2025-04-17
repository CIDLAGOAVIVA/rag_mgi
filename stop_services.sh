#!/bin/bash

echo "Parando serviços..."

# Tenta matar o processo da API (porta 8000)
sudo pkill -f "uvicorn main:app --host 0.0.0.0 --port 8000"
if ! pgrep -f "uvicorn main:app" > /dev/null; then
    echo "API parada com sucesso"
else
    echo "Erro ao parar API"
fi

# Tenta matar o processo do Chat (portas 8520-8524)
sudo pkill -f "python.*chat.py"
if ! pgrep -f "python.*chat.py" > /dev/null; then
    echo "Chat parado com sucesso"
else
    echo "Erro ao parar Chat"
fi

echo "Processo de parada concluído"
