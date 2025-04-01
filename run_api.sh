#!/bin/bash
echo "Iniciando RAG API..."
cd "$(dirname "$0")"
uv run api/rag_api.py
