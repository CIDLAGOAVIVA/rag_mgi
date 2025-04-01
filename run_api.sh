#!/bin/bash
mkdir -p logs
echo "Iniciando RAG API..."
cd "$(dirname "$0")"
nohup uv run api/rag_api.py > logs/api.log 2>&1 &
echo $! > api.pid
echo "API iniciada na porta 8000"
echo "PID: $(cat api.pid)"
echo "Logs em: logs/api.log"
