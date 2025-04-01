#!/bin/bash
mkdir -p logs
echo "Iniciando Chat Interface..."
cd "$(dirname "$0")"
nohup uv run chat/chat.py > logs/chat.log 2>&1 &
echo $! > chat.pid
echo "Chat iniciado na porta 8520"
echo "PID: $(cat chat.pid)"
echo "Logs em: logs/chat.log"
