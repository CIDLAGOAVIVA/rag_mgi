import re
from typing import Dict, List, Any

class MCPValidator:
    """Valida se as respostas estão seguindo o protocolo MCP adequadamente."""
    
    def __init__(self):
        pass
    
    def extract_citations(self, response: str) -> List[int]:
        """Extrai IDs de documentos citados na resposta."""
        citation_pattern = r'\[(\d+)\]'
        citations = re.findall(citation_pattern, response)
        return [int(c) for c in citations if c.isdigit()]
    
    def validate_response(self, response: str, query: str, retrieved_docs: List[Any]) -> Dict:
        """Valida se a resposta segue o protocolo MCP."""
        citations = self.extract_citations(response)
        
        validation_results = {
            "follows_mcp": len(citations) > 0,
            "citations": citations,
            "citation_count": len(citations),
            "cited_docs_percentage": len(citations) / len(retrieved_docs) if retrieved_docs else 0,
            "hallucination_risk": "Baixo" if len(citations) > 0 else "Alto"
        }
        
        return validation_results