# Documentação dos Servidores MCP

Este documento descreve a implementação e funcionalidades dos servidores MCP (Meta Content Provider) para as bases de conhecimento da CEITEC, TELEBRAS e IMBEL.

## Índice

1. [Visão Geral](#visão-geral)
2. [Configuração do Ambiente](#configuração-do-ambiente)
3. [Arquitetura Comum](#arquitetura-comum)
   - [Inicialização e Ciclo de Vida](#inicialização-e-ciclo-de-vida)
   - [Base Vetorial e Embeddings](#base-vetorial-e-embeddings)
   - [RAG (Retrieval-Augmented Generation)](#rag-retrieval-augmented-generation)
4. [Servidor CEITEC](#servidor-ceitec)
   - [Endpoints](#endpoints-ceitec)
   - [Recursos](#recursos-ceitec)
   - [Formatos de Resposta](#formatos-de-resposta-ceitec)
5. [Servidor TELEBRAS](#servidor-telebras)
   - [Endpoints](#endpoints-telebras)
   - [Recursos](#recursos-telebras)
   - [Formatos de Resposta](#formatos-de-resposta-telebras)
6. [Servidor IMBEL](#servidor-imbel)
   - [Endpoints](#endpoints-imbel)
   - [Recursos](#recursos-imbel)
   - [Formatos de Resposta](#formatos-de-resposta-imbel)
7. [Migração para o Modelo E5-Mistral-7B](#migração-para-o-modelo-e5-mistral-7b)
8. [Monitoramento e Diagnóstico](#monitoramento-e-diagnóstico)

## Visão Geral

Os servidores MCP são interfaces para consulta de documentos usando técnicas de RAG (Retrieval-Augmented Generation). Cada servidor é dedicado a uma base de conhecimento específica:

- **CEITEC**: Documentos sobre a empresa CEITEC e seu setor de semicondutores
- **TELEBRAS**: Documentos sobre a empresa TELEBRAS e seus serviços de telecomunicações
- **IMBEL**: Documentos sobre a empresa IMBEL e seus produtos de defesa e segurança

Cada servidor expõe uma API que permite consultas semânticas à base de conhecimento correspondente.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.10+
- Dependências listadas em `requirements.txt`
- Acesso à API DeepSeek (chave em `.env`)
- Arquivos de documentos Markdown organizados por empresa

### Variáveis de Ambiente

```
DEEPSEEK_API_KEY=sua_chave_aqui  # Necessária para o LLM
PORT_CEITEC=8009  # Porta padrão para o servidor CEITEC
PORT_IMBEL=8010   # Porta padrão para o servidor IMBEL
PORT_TELEBRAS=8011  # Porta padrão para o servidor TELEBRAS
```

### Diretórios de Base Vetorial

- CEITEC: `./chroma_db_semantic_CEITEC`
- TELEBRAS: `./chroma_db_semantic_Telebras`
- IMBEL: `./chroma_db_semantic_IMBEL`

## Arquitetura Comum

Todos os servidores compartilham uma arquitetura comum:

### Inicialização e Ciclo de Vida

Cada servidor implementa:

1. **Lifespan**: Gerencia o ciclo de vida do servidor através de `app_lifespan()`
2. **Estado**: Mantém referências ao vectorstore e à cadeia RAG
3. **Inicialização**: Carrega ou cria bases vetoriais através de `initialize_vectorstore()`

### Base Vetorial e Embeddings

Aspectos comuns:

- **Modelo de Embedding**: Atualmente usa `intfloat/multilingual-e5-base`
- **Registro de Arquivos**: Mantém hash de arquivos já processados
- **Vectorstore**: Implementação ChromaDB para armazenamento de embeddings

### RAG (Retrieval-Augmented Generation)

Todos os servidores implementam:

- **Retrievers**: Configurados com MMR (Maximum Marginal Relevance)
- **LLM**: Utiliza o modelo DeepSeek para geração de respostas
- **Prompts Personalizados**: Templates específicos para cada tipo de empresa

## Servidor CEITEC

### Endpoints CEITEC

O servidor CEITEC implementa os seguintes endpoints:

#### `query_ceitec`

```python
@mcp.tool()
async def query_ceitec(query: str, max_results: int = 15, ctx: Context = None) -> dict
```

Consulta a base de conhecimento com perguntas sobre a CEITEC.

**Parâmetros:**
- `query`: Consulta em linguagem natural
- `max_results`: Número máximo de fontes a retornar (padrão: 15)
- `ctx`: Contexto da requisição

**Retorno:**
```json
{
  "answer": "Resposta contextualizada",
  "sources": ["caminho/para/doc1.md", "caminho/para/doc2.md"],
  "processing_time": 2.45
}
```

#### `list_document_categories`

```python
@mcp.tool()
async def list_document_categories(ctx: Context = None) -> dict
```

Lista categorias de documentos disponíveis.

**Retorno:**
```json
{
  "categories": ["Relatórios Financeiros", "Especificações Técnicas", "Documentos Legais", "Notícias", "Artigos Científicos"]
}
```

#### `/health` (GET)

Endpoint para verificação de saúde do servidor.

**Retorno:**
```json
{ "status": "íntegro" }
```
ou
```json
{ "status": "degradado", "reason": "Cadeia RAG não inicializada" }
```

### Recursos CEITEC

#### `ceitec://overview`

```python
@mcp.resource("ceitec://overview")
def ceitec_overview() -> dict
```

Visão geral sobre a empresa CEITEC.

**Retorno:**
```json
{
  "name": "CEITEC S.A.",
  "full_name": "Centro Nacional de Tecnologia Eletrônica Avançada S.A.",
  "founded": "2008",
  "headquarters": "Porto Alegre, RS, Brasil",
  "industry": "Semicondutores",
  "main_products": ["Chips RFID", "Circuitos integrados para aplicações específicas"],
  "description": "A CEITEC S.A. é uma empresa pública federal brasileira, vinculada ao Ministério da Ciência, Tecnologia e Inovações, focada no desenvolvimento e produção de componentes semicondutores."
}
```

#### `ceitec://document-count`

```python
@mcp.resource("ceitec://document-count")
def document_count() -> dict
```

Informações sobre a quantidade de documentos na base.

**Retorno:**
```json
{
  "total_documents": 156,
  "total_chunks": "Variável conforme processamento",
  "last_updated": "2023-07-19 15:30:45"
}
```

### Formatos de Resposta CEITEC

O servidor CEITEC define dois templates de formatação:

#### `technical_response`

```python
@mcp.prompt()
def technical_response(summary: str, details: str, specs: str, sources: str) -> str
```

Para respostas técnicas sobre semicondutores e produtos da CEITEC.

#### `general_response`

```python
@mcp.prompt()
def general_response(main_content: str, additional_info: str, sources: str) -> str
```

Para respostas gerais sobre a empresa CEITEC.

## Servidor TELEBRAS

### Endpoints TELEBRAS

#### `query_telebras`

```python
@mcp.tool()
async def query_telebras(query: str, max_results: int = 15, ctx: Context = None) -> dict
```

Consulta a base de conhecimento com perguntas sobre a TELEBRAS.

**Parâmetros e Retorno:** similares ao `query_ceitec`.

#### `list_document_categories`

```python
@mcp.tool()
async def list_document_categories(ctx: Context = None) -> dict
```

Lista categorias de documentos disponíveis.

**Retorno:**
```json
{
  "categories": ["Relatórios Anuais", "Documentos Técnicos", "Releases de Imprensa", "Projetos de Conectividade", "Relatórios de Governança", "Documentos Regulatórios"]
}
```

#### `search_services`

```python
@mcp.tool()
async def search_services(service_name: str, ctx: Context = None) -> dict
```

Busca informações sobre serviços específicos da TELEBRAS.

**Parâmetros:**
- `service_name`: Nome do serviço a ser pesquisado

**Retorno:**
```json
{
  "service_name": "Internet Banda Larga",
  "description": "Descrição detalhada do serviço...",
  "sources": ["caminho/para/doc1.md", "caminho/para/doc2.md"],
  "processing_time": 3.21
}
```

#### `search_projects`

```python
@mcp.tool()
async def search_projects(project_name: str = "", region: str = "", ctx: Context = None) -> dict
```

Busca informações sobre projetos da TELEBRAS.

**Parâmetros:**
- `project_name`: Nome do projeto a ser pesquisado (opcional)
- `region`: Região geográfica do projeto (opcional)

**Retorno:**
```json
{
  "query": "Informações sobre o projeto SGDC da TELEBRAS",
  "projects": "Detalhes sobre o projeto...",
  "sources": ["caminho/para/doc1.md", "caminho/para/doc2.md"],
  "processing_time": 2.89
}
```

#### `/health` (GET)

Endpoint para verificação de saúde do servidor (similar ao CEITEC).

### Recursos TELEBRAS

#### `telebras://overview`

```python
@mcp.resource("telebras://overview")
def telebras_overview() -> dict
```

Visão geral sobre a empresa TELEBRAS.

**Retorno:**
```json
{
  "name": "TELEBRAS",
  "full_name": "Telecomunicações Brasileiras S.A.",
  "founded": "1972",
  "headquarters": "Brasília, DF, Brasil",
  "industry": "Telecomunicações",
  "main_services": ["Internet banda larga", "Satélite SGDC", "Backbone de fibra óptica", "Redes Governamentais"],
  "description": "A TELEBRAS é uma empresa estatal brasileira de telecomunicações vinculada ao Ministério das Comunicações, focada em implementar e operar redes de telecomunicações e prover serviços de internet."
}
```

#### `telebras://document-count`

```python
@mcp.resource("telebras://document-count")
def document_count() -> dict
```

Informações sobre a quantidade de documentos na base (similar ao CEITEC).

#### `telebras://service-categories`

```python
@mcp.resource("telebras://service-categories")
def service_categories() -> dict
```

Categorias de serviços da TELEBRAS.

**Retorno:**
```json
{
  "categories": ["Internet banda larga", "Comunicação via satélite", "Redes corporativas", "Soluções governamentais", "Backbone nacional"]
}
```

#### `telebras://key-projects`

```python
@mcp.resource("telebras://key-projects")
def key_projects() -> dict
```

Principais projetos da TELEBRAS.

**Retorno:**
```json
{
  "projects": [
    {"name": "SGDC", "description": "Satélite Geoestacionário de Defesa e Comunicações Estratégicas", "year": "2017"},
    {"name": "PNBL", "description": "Programa Nacional de Banda Larga", "year": "2010"}
  ]
}
```

### Formatos de Resposta TELEBRAS

O servidor TELEBRAS define quatro templates de formatação:

#### `technical_response`

```python
@mcp.prompt()
def technical_response(summary: str, details: str, specs: str, sources: str) -> str
```

Para respostas técnicas sobre telecomunicações.

#### `general_response`

```python
@mcp.prompt()
def general_response(main_content: str, additional_info: str, sources: str) -> str
```

Para respostas gerais sobre a empresa.

#### `project_response`

```python
@mcp.prompt()
def project_response(project_name: str, description: str, goals: str, status: str, sources: str) -> str
```

Para respostas sobre projetos específicos.

#### `comparison_response`

```python
@mcp.prompt()
def comparison_response(topic: str, option1: str, details1: str, option2: str, details2: str, comparison: str, sources: str) -> str
```

Para comparações entre diferentes serviços ou tecnologias.

## Servidor IMBEL

### Endpoints IMBEL

#### `query_imbel`

```python
@mcp.tool()
async def query_imbel(query: str, max_results: int = 15, ctx: Context = None) -> dict
```

Consulta a base de conhecimento com perguntas sobre a IMBEL.

**Parâmetros e Retorno:** similares ao `query_ceitec`.

#### `list_document_categories`

```python
@mcp.tool()
async def list_document_categories(ctx: Context = None) -> dict
```

Lista categorias de documentos disponíveis.

**Retorno:**
```json
{
  "categories": ["Relatórios Técnicos", "Manuais de Produtos", "Documentos Institucionais", "Notícias", "Publicações Técnicas", "Catálogos de Produtos"]
}
```

#### `search_products`

```python
@mcp.tool()
async def search_products(product_name: str, details: bool = False, ctx: Context = None) -> dict
```

Busca informações sobre produtos específicos da IMBEL.

**Parâmetros:**
- `product_name`: Nome do produto a ser pesquisado
- `details`: Se deve retornar detalhes técnicos completos

**Retorno:**
```json
{
  "product_name": "IA2",
  "description": "Descrição detalhada do produto...",
  "sources": ["caminho/para/doc1.md", "caminho/para/doc2.md"],
  "processing_time": 1.95,
  "technical_details": "Detalhes técnicos completos disponíveis mediante solicitação."
}
```

#### `/health` (GET)

Endpoint para verificação de saúde do servidor (similar ao CEITEC e TELEBRAS).

### Recursos IMBEL

#### `imbel://overview`

```python
@mcp.resource("imbel://overview")
def imbel_overview() -> dict
```

Visão geral sobre a empresa IMBEL.

**Retorno:**
```json
{
  "name": "IMBEL",
  "full_name": "Indústria de Material Bélico do Brasil",
  "founded": "1975",
  "headquarters": "Brasília, DF, Brasil",
  "industry": "Defesa e Segurança",
  "main_products": ["Armamentos", "Munições", "Explosivos", "Equipamentos militares"],
  "description": "A IMBEL é uma empresa estatal brasileira vinculada ao Exército Brasileiro, focada no desenvolvimento e produção de material de defesa e segurança."
}
```

#### `imbel://document-count`

```python
@mcp.resource("imbel://document-count")
def document_count() -> dict
```

Informações sobre a quantidade de documentos na base (similar ao CEITEC e TELEBRAS).

#### `imbel://product-categories`

```python
@mcp.resource("imbel://product-categories")
def product_categories() -> dict
```

Categorias de produtos da IMBEL.

**Retorno:**
```json
{
  "categories": ["Armas de pequeno porte", "Munições", "Explosivos", "Equipamentos de comunicação", "Sistemas de defesa"]
}
```

### Formatos de Resposta IMBEL

O servidor IMBEL define três templates de formatação:

#### `technical_response`

```python
@mcp.prompt()
def technical_response(summary: str, details: str, specs: str, sources: str) -> str
```

Para respostas técnicas sobre produtos da IMBEL.

#### `general_response`

```python
@mcp.prompt()
def general_response(main_content: str, additional_info: str, sources: str) -> str
```

Para respostas gerais sobre a empresa.

#### `product_response`

```python
@mcp.prompt()
def product_response(product_name: str, description: str, features: str, specs: str, sources: str) -> str
```

Para respostas sobre produtos específicos.

## Migração para o Modelo E5-Mistral-7B

Para migrar do modelo atual (`intfloat/multilingual-e5-base`) para o modelo E5-Mistral-7B (`intfloat/e5-mistral-7b-instruct`), são necessárias as seguintes alterações:

### 1. Atualização da Constante de Modelo

Em cada arquivo de servidor:

```python
# Substituir
EMBEDDING_MODEL = "intfloat/multilingual-e5-base"

# Por
EMBEDDING_MODEL = "intfloat/e5-mistral-7b-instruct"
```

### 2. Modificação das Funções de Embedding

Ao inicializar o modelo de embeddings:

```python
embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL,
    model_kwargs={"max_seq_length": 4096}  # Definir max_seq_length para o novo modelo
)
```

### 3. Modificação do Chunker Semântico

No arquivo `semantic_chunker.py`:

```python
class E5SemanticChunker:
    def __init__(
        self, 
        model_name: str = "intfloat/e5-mistral-7b-instruct",
        similarity_threshold: float = 0.6,
        max_tokens_per_chunk: int = 1000,
        min_tokens_per_chunk: int = 100,
        max_seq_length: int = 4096,  # Parâmetro adicional
        prompt_template: str = "Instruct: Given a text, extract semantic information\nQuery: {text}",  # Template para instrução
        print_logging: bool = False
    ):
        self.model = SentenceTransformer(model_name)
        self.model.max_seq_length = max_seq_length
        # ...restante do método...
        self.prompt_template = prompt_template
```

### 4. Modificação no Método de Cálculo de Embeddings

```python
def _compute_embeddings(self, sentences: List[str]) -> np.ndarray:
    # ...código existente...
    
    # Usar o formato de instrução para consultas
    formatted_sentences = []
    for sentence in sentences:
        formatted_sentence = self.prompt_template.format(text=sentence)
        formatted_sentences.append(formatted_sentence)
    
    return self.model.encode(formatted_sentences, show_progress_bar=self.print_logging)
```

### 5. Reconstrução de Bases Vetoriais

Como o novo modelo produz embeddings de dimensão diferente (4096 vs 1024), será necessário reconstruir as bases vetoriais:

```bash
# Excluir bases atuais
rm -rf ./chroma_db_semantic_CEITEC
rm -rf ./chroma_db_semantic_IMBEL
rm -rf ./chroma_db_semantic_Telebras

# Reconstruir bases com novo modelo
python rag_2/rag_cria_bd_CEITEC.py
python rag_2/rag_cria_bd_IMBEL.py
python rag_2/rag_cria_bd_Telebras.py
```

### Observações sobre a migração:

- O modelo E5-Mistral-7B requer significativamente mais recursos computacionais (7B parâmetros vs ~300M)
- É multilíngue, mas tem melhor desempenho em inglês
- O espaço de armazenamento necessário para embeddings será aproximadamente 4x maior

## Monitoramento e Diagnóstico

Todos os servidores implementam rotas de diagnóstico e logs detalhados.

### Rota `/health`

Verifica o estado do servidor e componentes críticos.

### Logs de Servidor

Os servidores registram eventos-chave:

- Inicialização e encerramento
- Inicialização e falhas de recursos
- Processamento e duração de consultas
- Erros e exceções

### Recuperação Automática

Funcionalidades de recuperação incluem:

- Detecção de bases vetoriais ausentes com reconstrução automática
- Reconstrução de registros de arquivos quando necessário
- Relatórios detalhados de erros para diagnóstico