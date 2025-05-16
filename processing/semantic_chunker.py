import numpy as np
from typing import List, Dict, Any, Optional, Tuple
from sentence_transformers import SentenceTransformer
import textwrap
from sklearn.cluster import AgglomerativeClustering
import uuid
from tqdm import tqdm

class E5SemanticChunker:
    """
    Uma implementação de Semantic Chunker usando o modelo multilingual-e5-large.
    Esta classe divide textos em chunks com base na similaridade semântica,
    utilizando embeddings do modelo de sentence transformers.
    """
    
    def __init__(
        self, 
        model_name: str = "intfloat/multilingual-e5-large",
        similarity_threshold: float = 0.6,
        max_tokens_per_chunk: int = 1000,
        min_tokens_per_chunk: int = 100,
        print_logging: bool = False
    ):
        """
        Inicializa o chunker semântico.
        
        Args:
            model_name: Nome do modelo de embedding a ser usado
            similarity_threshold: Limiar de similaridade para decidir quando criar um novo chunk
            max_tokens_per_chunk: Número máximo aproximado de tokens em um chunk
            min_tokens_per_chunk: Número mínimo aproximado de tokens em um chunk
            print_logging: Se True, exibe logs durante o processamento
        """
        self.model = SentenceTransformer(model_name)
        self.similarity_threshold = similarity_threshold
        self.max_tokens_per_chunk = max_tokens_per_chunk
        self.min_tokens_per_chunk = min_tokens_per_chunk
        self.print_logging = print_logging
        
    def _split_text_to_sentences(self, text: str) -> List[str]:
        """
        Divide o texto em sentenças usando pontuação.
        
        Args:
            text: Texto a ser dividido
            
        Returns:
            Lista de sentenças
        """
        # Simplificado: dividir por pontos, mas preservar a pontuação
        import re
        sentences = re.split(r'(?<=[.!?])\s+', text)
        # Filtrar sentenças vazias
        return [s.strip() for s in sentences if s.strip()]
    
    def _estimate_token_count(self, text: str) -> int:
        """
        Estimativa simples de contagem de tokens baseada em palavras.
        
        Args:
            text: Texto para estimar tokens
            
        Returns:
            Número estimado de tokens
        """
        # Aproximação: 1 token ~= 0.75 palavras
        return int(len(text.split()) / 0.75)
    
    def _compute_embeddings(self, sentences: List[str]) -> np.ndarray:
        """
        Calcula os embeddings para uma lista de sentenças.
        
        Args:
            sentences: Lista de sentenças
            
        Returns:
            Array numpy com embeddings
        """
        if self.print_logging:
            print(f"Calculando embeddings para {len(sentences)} sentenças...")
        
        return self.model.encode(sentences, show_progress_bar=self.print_logging)
    
    def _compute_similarity_matrix(self, embeddings: np.ndarray) -> np.ndarray:
        """
        Calcula a matriz de similaridade entre todos os embeddings.
        
        Args:
            embeddings: Array de embeddings
            
        Returns:
            Matriz de similaridade
        """
        # Normalizar embeddings
        normalized_embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
        
        # Calcular similaridade de cosseno entre todos os pares
        similarity_matrix = np.dot(normalized_embeddings, normalized_embeddings.T)
        
        return similarity_matrix
    
    def _create_chunks_with_agglomerative_clustering(
        self, 
        sentences: List[str], 
        embeddings: np.ndarray
    ) -> List[str]:
        """
        Cria chunks usando clustering aglomerativo hierárquico.
        
        Args:
            sentences: Lista de sentenças
            embeddings: Array de embeddings
            
        Returns:
            Lista de chunks
        """
        similarity_matrix = self._compute_similarity_matrix(embeddings)
        
        # Converter similaridade para distância (1 - similaridade)
        distance_matrix = 1 - similarity_matrix
        
        # Determinar número aproximado de clusters baseado no tamanho total do texto
        total_tokens = sum(self._estimate_token_count(s) for s in sentences)
        num_clusters = max(1, total_tokens // self.max_tokens_per_chunk)
        
        # Aplicar clustering
        clustering = AgglomerativeClustering(
            n_clusters=num_clusters,
            affinity='precomputed',
            linkage='average'
        )
        
        labels = clustering.fit_predict(distance_matrix)
        
        # Agrupar sentenças por cluster
        clusters = {}
        for i, label in enumerate(labels):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(sentences[i])
        
        # Criar chunks a partir dos clusters
        chunks = []
        for label, cluster_sentences in clusters.items():
            chunk = " ".join(cluster_sentences)
            chunks.append(chunk)
            
        return chunks
    
    def _create_chunks_sequential(
        self,
        sentences: List[str],
        embeddings: np.ndarray
    ) -> List[str]:
        """
        Cria chunks sequencialmente com base na similaridade.
        
        Args:
            sentences: Lista de sentenças
            embeddings: Array de embeddings
            
        Returns:
            Lista de chunks
        """
        if len(sentences) == 0:
            return []
            
        similarity_matrix = self._compute_similarity_matrix(embeddings)
        
        chunks = []
        current_chunk_sentences = [sentences[0]]
        current_chunk_embedding = embeddings[0].reshape(1, -1)
        
        for i in range(1, len(sentences)):
            # Calcular similaridade com o chunk atual
            normalized_current = current_chunk_embedding / np.linalg.norm(current_chunk_embedding)
            normalized_sentence = embeddings[i] / np.linalg.norm(embeddings[i])
            similarity = np.dot(normalized_current.flatten(), normalized_sentence)
            
            # Estimar tokens do chunk atual + nova sentença
            current_tokens = self._estimate_token_count(" ".join(current_chunk_sentences))
            new_tokens = self._estimate_token_count(sentences[i])
            
            # Decidir se criar um novo chunk ou adicionar à existente
            if (similarity < self.similarity_threshold or 
                current_tokens + new_tokens > self.max_tokens_per_chunk):
                # Finalizar chunk atual se tem tokens suficientes
                if current_tokens >= self.min_tokens_per_chunk:
                    chunks.append(" ".join(current_chunk_sentences))
                    current_chunk_sentences = [sentences[i]]
                    current_chunk_embedding = embeddings[i].reshape(1, -1)
                else:
                    # Senão, continue adicionando mesmo com baixa similaridade
                    current_chunk_sentences.append(sentences[i])
                    # Atualizar embedding do chunk (média simples)
                    count = len(current_chunk_sentences)
                    current_chunk_embedding = ((count-1) * current_chunk_embedding + embeddings[i].reshape(1, -1)) / count
            else:
                # Adicionar à chunk atual
                current_chunk_sentences.append(sentences[i])
                # Atualizar embedding do chunk (média simples)
                count = len(current_chunk_sentences)
                current_chunk_embedding = ((count-1) * current_chunk_embedding + embeddings[i].reshape(1, -1)) / count
        
        # Adicionar o último chunk se não estiver vazio
        if current_chunk_sentences:
            chunks.append(" ".join(current_chunk_sentences))
            
        return chunks
    
    def chunk_text(self, text: str, method: str = "sequential") -> List[str]:
        """
        Divide o texto em chunks semânticos.
        
        Args:
            text: Texto a ser dividido em chunks
            method: Método de chunking ('sequential' ou 'clustering')
            
        Returns:
            Lista de chunks
        """
        sentences = self._split_text_to_sentences(text)
        
        if not sentences:
            return []
            
        if self.print_logging:
            print(f"Dividido em {len(sentences)} sentenças")
            
        embeddings = self._compute_embeddings(sentences)
        
        if method == "clustering":
            chunks = self._create_chunks_with_agglomerative_clustering(sentences, embeddings)
        else:
            chunks = self._create_chunks_sequential(sentences, embeddings)
            
        if self.print_logging:
            print(f"Criados {len(chunks)} chunks")
            for i, chunk in enumerate(chunks):
                print(f"\nChunk {i+1}, tokens ~{self._estimate_token_count(chunk)}")
                print("-" * 80)
                print(textwrap.fill(chunk, width=100))
                print("-" * 80)
                
        return chunks
        
    def chunk_documents(self, docs: List[str], method: str = "sequential") -> List[List[str]]:
        """
        Processa uma lista de documentos, dividindo cada um em chunks.
        
        Args:
            docs: Lista de documentos (textos)
            method: Método de chunking ('sequential' ou 'clustering')
            
        Returns:
            Lista de listas de chunks (uma lista de chunks para cada documento)
        """
        results = []
        
        for i, doc in enumerate(docs):
            if self.print_logging:
                print(f"\nProcessando documento {i+1}/{len(docs)}")
            
            chunks = self.chunk_text(doc, method)
            results.append(chunks)
            
        return results
    
    def chunk_with_metadata(self, docs: List[Dict[str, Any]], text_key: str = "text", method: str = "sequential") -> List[Dict[str, Any]]:
        """
        Processa uma lista de documentos com metadados, dividindo o texto em chunks
        e preservando os metadados.
        
        Args:
            docs: Lista de dicionários, cada um com texto e metadados
            text_key: A chave que contém o texto em cada documento
            method: Método de chunking ('sequential' ou 'clustering')
            
        Returns:
            Lista de dicionários com chunks e metadados
        """
        chunk_docs = []
        
        for doc_idx, doc in enumerate(docs):
            if text_key not in doc:
                if self.print_logging:
                    print(f"Aviso: Documento {doc_idx} não contém a chave '{text_key}'. Pulando.")
                continue
                
            text = doc[text_key]
            chunks = self.chunk_text(text, method)
            
            for chunk_idx, chunk in enumerate(chunks):
                # Criar novo documento com mesmos metadados
                chunk_doc = doc.copy()
                # Substituir texto pelo chunk
                chunk_doc[text_key] = chunk
                # Adicionar metadados de chunking
                chunk_doc["chunk_id"] = f"{doc_idx}_{chunk_idx}"
                chunk_doc["doc_id"] = doc_idx
                chunk_doc["chunk_idx"] = chunk_idx
                chunk_doc["total_chunks"] = len(chunks)
                
                chunk_docs.append(chunk_doc)
                
        return chunk_docs

# Exemplo de uso:
if __name__ == "__main__":
    chunker = E5SemanticChunker(
        similarity_threshold=0.7,
        max_tokens_per_chunk=1000,
        min_tokens_per_chunk=100,
        print_logging=True
    )
    
    text = """
    Dense retrieval se tornou um método proeminente para obter contexto relevante ou conhecimento 
    mundial em tarefas de PNL de domínio aberto. Quando usamos um recuperador denso aprendido em um 
    corpus de recuperação no momento da inferência, uma escolha de design frequentemente negligenciada 
    é a unidade de recuperação na qual o corpus é indexado, por exemplo, documento, passagem ou sentença. 
    Descobrimos que a escolha da unidade de recuperação impacta significativamente o desempenho das tarefas 
    de recuperação e downstream. Distinto da abordagem típica de usar passagens ou sentenças, introduzimos 
    uma nova unidade de recuperação, proposição, para recuperação densa. Proposições são definidas como 
    expressões atômicas dentro do texto, cada uma encapsulando um factóide distinto e apresentada em um 
    formato de linguagem natural conciso e autocontido. Conduzimos uma comparação empírica de diferentes 
    granularidades de recuperação. Nossos experimentos revelam que indexar um corpus por unidades de 
    granulação fina, como proposições, supera significativamente as unidades de nível de passagem em tarefas 
    de recuperação.
    
    O céu é azul e ensolarado hoje. As nuvens estão esparsas. A temperatura é de 25 graus celsius.
    Os pássaros estão cantando nas árvores. A grama está verde e recém-cortada.
    """
    
    chunks = chunker.chunk_text(text)
    print(f"\nResultado final: {len(chunks)} chunks")