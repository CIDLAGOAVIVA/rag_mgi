import json
import os
from datetime import datetime
from typing import Dict, Any, List

class MCPLogger:
    """Registra interações MCP para análise posterior."""
    
    def __init__(self, log_dir: str = "./mcp_logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
    
    def log_interaction(self, 
                        query: str, 
                        mcp_prompt: str, 
                        response: str, 
                        retrieved_docs: List[Any],
                        validation_results: Dict[str, Any] = None,
                        processing_time: float = None):
        """Registra uma interação completa com o modelo usando MCP."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_entry = {
            "timestamp": timestamp,
            "query": query,
            "mcp_prompt": mcp_prompt,
            "response": response,
            "retrieved_docs_count": len(retrieved_docs),
            "retrieved_docs_sources": [doc.metadata.get('source', 'unknown') for doc in retrieved_docs] if retrieved_docs else [],
            "validation_results": validation_results,
            "processing_time": processing_time
        }
        
        # Salvar em arquivo
        filename = f"{self.log_dir}/mcp_interaction_{timestamp}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(log_entry, f, ensure_ascii=False, indent=2)
        
        return filename