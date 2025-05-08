rag_empresas/
├── config/                     # Configurações
│   ├── settings.py             # Configurações gerais
│   └── prompts.py              # Templates de prompts
├── data/                       # Dados brutos e processados
│   ├── raw/                    # Dados originais
│   │   ├── empresa_1/          # Organizado por empresa
│   │   ├── empresa_2/
│   │   └── empresa_3/
│   ├── processed/              # Dados processados
│   └── summaries/              # Resumos gerados pela IA
├── scraping/                   # Raspagem de dados
│   ├── news_scraper.py         # Raspagem de notícias
│   ├── articles_scraper.py     # Raspagem de artigos científicos
│   └── utils/                  # Utilitários para scraping
├── processing/                 # Processamento de documentos
│   ├── converter.py            # Converter de PDF/DOCX para MD (baseado no seu código)
│   ├── cleaner.py              # Limpeza de texto
│   └── summarizer.py           # Resumo automático de textos
├── rag/                        # Componentes RAG
│   ├── embeddings.py           # Geração de embeddings
│   ├── vectordb.py             # Gerenciamento da base vetorial
│   └── retrieval.py            # Funções de recuperação
├── api/                        # API REST (FastAPI)
│   ├── main.py                 # Ponto de entrada da API
│   ├── routes/                 # Rotas da API
│   └── models/                 # Modelos Pydantic
├── ui/                         # Interface de usuário (Gradio)
│   ├── chat.py                 # Interface de chat
│   └── components/             # Componentes reutilizáveis
├── models/                     # Configuração de modelos
│   ├── config.py               # Configurações dos modelos
│   └── prompts.py              # Templates de prompts
├── utils/                      # Utilitários gerais
│   ├── logger.py               # Logging
│   └── helpers.py              # Funções auxiliares
├── scripts/                    # Scripts para automação
│   ├── run_api.sh              # Executar API
│   ├── run_chat.sh             # Executar chat
│   ├── stop_services.sh        # Parar serviços
│   └── run_pipeline.py         # Executar pipeline completo
├── tests/                      # Testes automatizados
│   ├── test_scraping.py
│   ├── test_rag.py
│   └── test_api.py
├── logs/                       # Registros de log
├── vectordb/                   # Base de dados vetorial
├── .env                        # Variáveis de ambiente
├── requirements.txt            # Dependências
├── pyproject.toml              # Configuração do projeto
├── README.md                   # Documentação
└── main.py                     # Ponto de entrada principal


rag_mgi/ 
├── api/
│   └── rag_api.py              # API REST (FastAPI)
├── chat/
│   └── chat.py                 # Interface de chat (Gradio)
├── processing/
│   ├── agentic_chunker.py      # Chunking baseado em agente
│   ├── semantic_chunker.py     # Chunker semântico E5
│   ├── wrapper_langchain.py    # Wrapper para compatibilidade LangChain
│   └── conversao.py            # Conversor de documentos (PDF/DOCX -> MD)
├── rag/
│   ├── rag_pergunta_resposta.py # Lógica RAG original
│   └── update_vectordb.py      # Atualização incremental da base vetorial
├── data/                       # Diretório para chunks e documentos processados
│   ├── chunks/                 # Chunks gerados
│   ├── processed/              # Documentos processados
│   ├── raw/                    # Documentos brutos
│   └── summaries/              # Resumos gerados
├── chroma_db_semantic/         # Base de dados vetorial (gerada)
│   ├── chroma.sqlite3          # Banco SQLite da base vetorial 
│   └── 0770f7d0-351e-4bf0-bfe7-7c5e9f0010be/ # Diretório de embeddings
├── logs/                       # Logs dos serviços
│   ├── api.log                 # Log da API
│   └── chat.log                # Log do Chat
├── .vscode/                    # Configurações do VS Code
│   └── settings.json           # Configurações do editor
├── .env                        # Variáveis de ambiente (API Keys, etc.)
├── .gitignore                  # Arquivos ignorados pelo Git
├── .python-version             # Versão Python do projeto (3.12)
├── apaga_duplicata_raw_processed.py # Utilitário para remover duplicatas
├── api.pid                     # PID do processo da API
├── chat.pid                    # PID do processo do Chat
├── estrutura.md                # Este arquivo de estrutura
├── processed_files.json        # Registro de arquivos processados
├── pyproject.toml              # Configuração do projeto e dependências
├── README.md                   # Documentação
├── requirements.txt            # Dependências Python (pip)
├── run_api.sh                  # Script para iniciar a API em background
├── run_chat.sh                 # Script para iniciar o Chat em background
├── s3file.py                   # Utilitário para operações no S3
├── stop_services.sh            # Script para parar os serviços
├── token_analyzer.py           # Ferramenta de análise de tokens
└── uv.lock                     # Lock file do gerenciador de pacotes uv

