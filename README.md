# RAG MGI - Sistema de Consulta a Documentos

Sistema de consulta baseado em RAG (Retrieval-Augmented Generation) para documentos do MGI, utilizando LLM DeepSeek e embeddings locais.

## Tecnologias Utilizadas

### Core
- Python 3.12+
- FastAPI - Framework web para API
- Gradio - Interface de chat
- LangChain - Framework para LLM
- DeepSeek - Modelo de linguagem
- Sentence Transformers - Embeddings locais
- ChromaDB - Banco de dados vetorial

### Dependências Principais
- langchain-deepseek: Integração com modelo DeepSeek
- langchain-community: Componentes comunitários do LangChain
- sentence-transformers/all-MiniLM-L6-v2: Modelo de embeddings
- chromadb: Armazenamento vetorial
- FastAPI: API REST
- Gradio: Interface web
- uvicorn: Servidor ASGI

## Estrutura do Projeto
```
rag_mgi/ 
├── api/
│   └── rag_api.py # API REST (FastAPI)
├── chat/
│   └── chat.py # Interface de chat (Gradio)
├── processing/
│   ├── agentic_chunker.py # Chunking semântico (Opcional)
│   └── conversao.py # Conversor de documentos (PDF/DOCX -> MD)
├── rag/
│   └── rag_pergunta_resposta.py # Lógica RAG principal (Não usado pela API/Chat atualmente)
├── data/ # Diretório padrão para documentos Markdown processados (verificar código)
├── data2/ # Diretório alternativo usado em alguns scripts (verificar código)
│   ├── raw/ # Dados brutos para conversão
│   └── processed/ # Dados convertidos para MD
├── chroma_db/ # Base de dados vetorial (gerada)
├── logs/ # Logs da API e do Chat (gerados)
├── .env # Arquivo para variáveis de ambiente (API Keys, etc.)
├── requirements.txt # Dependências Python (pip)
├── pyproject.toml # Configuração do projeto e dependências (uv/pip)
├── run_api.sh # Script para iniciar a API em background
├── run_chat.sh # Script para iniciar o Chat em background
├── stop_services.sh # Script para parar os serviços em background
└── README.md # Este arquivo

```

## Configuração

1. Crie um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows
```

2. Instale as dependências:
```bash
uv pip install -r requirements.txt
# ou
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite .env e adicione sua DEEPSEEK_API_KEY
```

4. Prepare seus documentos:
- Coloque seus arquivos Markdown na pasta `data/`
- Os documentos devem estar no formato `.md`

## Executando o Sistema

### Método 1: Execução em Background (Recomendado)

1. Dê permissão aos scripts:
```bash
chmod +x run_api.sh run_chat.sh stop_services.sh
```

2. Inicie os serviços:
```bash
./run_api.sh    # Inicia API na porta 8000
./run_chat.sh   # Inicia chat na porta 8520
```

3. Monitore os logs:
```bash
tail -f logs/api.log    # Logs da API
tail -f logs/chat.log   # Logs do chat
```

4. Para parar os serviços:
```bash
./stop_services.sh
```

### Método 2: Execução Manual

1. Inicie a API (Terminal 1):
```bash
uv run api/rag_api.py
```

2. Inicie o chat (Terminal 2):
```bash
uv run chat/chat.py
```

## Acessando o Sistema

- API RAG: http://localhost:8000
  - Documentação: http://localhost:8000/docs
  - Endpoint principal: http://localhost:8000/query

- Interface Chat: http://localhost:8520
  - Chat DeepSeek: Aba 1
  - Chat RAG: Aba 2

## Capacidades do Sistema

1. Chat DeepSeek
- Responde em português do Brasil
- Mantém contexto da conversa
- Temperatura 0.7 para respostas criativas

2. Chat RAG
- Consulta documentos locais
- Retorna fontes das informações
- Embeddings locais para privacidade
- Respostas baseadas em contexto

## Troubleshooting

1. Portas em uso:
- API: tenta porta 8000
- Chat: tenta portas 8520-8524

2. Logs:
- API: `logs/api.log`
- Chat: `logs/chat.log`

3. Problemas comuns:
- "DEEPSEEK_API_KEY não encontrada": Configure no .env
- "Directory not found": Crie pasta data/
- "Porta em uso": Use GRADIO_SERVER_PORT=<porta> ou aguarde porta alternativa

## Limitações

- Aceita apenas arquivos Markdown (.md)
- Requer chave API DeepSeek válida
- Embeddings podem consumir memória significativa

## Licença

MIT License
