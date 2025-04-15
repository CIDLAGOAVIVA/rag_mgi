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