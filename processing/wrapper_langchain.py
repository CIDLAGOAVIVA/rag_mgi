from typing import List, Dict, Any, Optional, Callable
from langchain_core.documents import Document
from langchain_core.document_transformers import DocumentTransformer
from processing.semantic_chunker import E5SemanticChunker

class E5SemanticTextSplitter(DocumentTransformer):
    """
    Wrapper do E5SemanticChunker compatível com a interface de DocumentTransformer do LangChain.
    Permite usar o chunker semântico de forma intercambiável com outros text splitters do LangChain.
    """
    
    def __init__(
        self,
        model_name: str = "intfloat/multilingual-e5-small",
        similarity_threshold: float = 0.7,
        max_tokens_per_chunk: int = 700,
        min_tokens_per_chunk: int = 100,
        chunk_method: str = "sequential",
        print_logging: bool = False
    ):
        """
        Inicializa o semantic text splitter.
        
        Args:
            model_name: Nome do modelo de embeddings a ser usado
            similarity_threshold: Limiar de similaridade para criar novos chunks
            max_tokens_per_chunk: Número máximo de tokens por chunk
            min_tokens_per_chunk: Número mínimo de tokens por chunk
            chunk_method: Método de chunking ('sequential' ou 'clustering')
            print_logging: Se True, exibe logs durante o processamento
        """
        self.chunker = E5SemanticChunker(
            model_name=model_name,
            similarity_threshold=similarity_threshold,
            max_tokens_per_chunk=max_tokens_per_chunk,
            min_tokens_per_chunk=min_tokens_per_chunk,
            print_logging=print_logging
        )
        self.chunk_method = chunk_method
    
    def transform_documents(
        self,
        documents: List[Document],
        **kwargs: Any,
    ) -> List[Document]:
        """
        Divide os documentos em chunks usando o semantic chunker.
        
        Args:
            documents: Lista de documentos para processar
            
        Returns:
            Lista de novos documentos, cada um representando um chunk
        """
        result_docs = []
        
        for doc in documents:
            chunks = self.chunker.chunk_text(doc.page_content, method=self.chunk_method)
            
            # Criar um novo documento para cada chunk
            for i, chunk in enumerate(chunks):
                # Copiar metadados originais
                metadata = doc.metadata.copy() if doc.metadata else {}
                
                # Adicionar metadados de chunking
                metadata["chunk_index"] = i
                metadata["total_chunks"] = len(chunks)
                
                # Criar novo documento
                new_doc = Document(
                    page_content=chunk,
                    metadata=metadata
                )
                
                result_docs.append(new_doc)
        
        return result_docs
    
    def split_text(self, text: str) -> List[str]:
        """
        Divide um texto em chunks.
        
        Args:
            text: Texto a ser dividido
            
        Returns:
            Lista de strings, cada uma representando um chunk
        """
        return self.chunker.chunk_text(text, method=self.chunk_method)

# Exemplo de uso com LangChain
def example_usage_langchain():
    from langchain_community.document_loaders import TextLoader
    from langchain_community.vectorstores import Chroma
    from langchain_community.embeddings import HuggingFaceEmbeddings
    
    # Carregar um documento
    loader = TextLoader("example.txt")
    documents = loader.load()
    
    # Instanciar o text splitter semântico
    text_splitter = E5SemanticTextSplitter(
        model_name="intfloat/multilingual-e5-small",
        similarity_threshold=0.7,
        max_tokens_per_chunk=700
    )
    
    # Dividir documentos
    split_docs = text_splitter.transform_documents(documents)
    
    print(f"Documento original dividido em {len(split_docs)} chunks semânticos")
    
    # Criar embeddings e armazenar em vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-small")
    
    vectorstore = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings
    )
    
    # Usar para pesquisa
    query = "O que é chunking semântico?"
    results = vectorstore.similarity_search(query, k=2)
    
    print("\nResultados da pesquisa:")
    for doc in results:
        print(f"- {doc.page_content[:100]}...")

# Se o script for executado diretamente, mostre o exemplo
if __name__ == "__main__":
    example_usage_langchain()