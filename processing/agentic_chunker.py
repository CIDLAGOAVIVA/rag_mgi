from typing import Optional, Dict, List, Any
import uuid
from rich import print
from dotenv import load_dotenv
import os
import requests
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_deepseek import ChatDeepSeek # Importação principal já usada em rag_api.py
# Nota: DeepSeekChatMessage e DeepSeekChatOptions podem não ser mais classes exportadas ou necessárias
from langchain_core.language_models.chat_models import BaseChatModel # Import BaseChatModel

load_dotenv()

class AgenticChunker:
    # -- API DO DEEPSEEK --
    # def __init__(self, deepseek_api_key=None, api_base=None, model='deepseek-chat', print_logging=True): # Adicionado print_logging ao construtor para uso da API do deepseek
    # -- MODELO LLM LOCAL --
    def __init__(self, llm: BaseChatModel, print_logging=True): # Accept BaseChatModel
        self.chunks = {}
        self.id_truncate_limit = 5

        # Whether or not to update/refine summaries and titles as you get new information
        self.generate_new_metadata_ind = True
        self.print_logging = print_logging # Usar o parâmetro passado

        # Store the passed LLM instance
        self.llm = llm # Use the passed llm object

    def add_propositions(self, propositions):
        for proposition in propositions:
            self.add_proposition(proposition)
    
    def add_proposition(self, proposition):
        if self.print_logging:
            print(f"\nAdding: '{proposition}'")

        # If it's your first chunk, just make a new chunk and don't check for others
        if len(self.chunks) == 0:
            if self.print_logging:
                print("No chunks, creating a new one")
            self._create_new_chunk(proposition)
            return

        chunk_id = self._find_relevant_chunk(proposition)

        # If a chunk was found then add the proposition to it
        if chunk_id:
            if self.print_logging:
                print(f"Chunk Found ({self.chunks[chunk_id]['chunk_id']}), adding to: {self.chunks[chunk_id]['title']}")
            self.add_proposition_to_chunk(chunk_id, proposition)
            return
        else:
            if self.print_logging:
                print("No chunks found")
            # If a chunk wasn't found, then create a new one
            self._create_new_chunk(proposition)
        
    def add_proposition_to_chunk(self, chunk_id, proposition):
        # Add the proposition
        self.chunks[chunk_id]['propositions'].append(proposition)

        # Then grab a new summary
        if self.generate_new_metadata_ind:
            self.chunks[chunk_id]['summary'] = self._update_chunk_summary(self.chunks[chunk_id])
            self.chunks[chunk_id]['title'] = self._update_chunk_title(self.chunks[chunk_id])

    def _update_chunk_summary(self, chunk):
        """
        If you add a new proposition to a chunk, you may want to update the summary or else they could get stale
        """
        messages = [
            {
                "role": "system",
                "content": """
                Você é o guardião de um grupo de chunks que representam grupos de frases que falam sobre um tópico semelhante.
                Uma nova proposição acabou de ser adicionada a um dos seus chunks, você deve gerar um resumo muito breve de 1 frase
                que informará aos visualizadores sobre o que um grupo de chunk se trata.

                Um bom resumo dirá sobre o que é o chunk e fornecerá instruções esclarecedoras sobre o que adicionar ao chunk.

                Você receberá um grupo de proposições que estão no chunk e o resumo atual do chunk.

                Seus resumos devem antecipar a generalização. Se você receber uma proposição sobre maçãs, generalize para alimentos.
                Ou mês, generalize para "datas e horários".

                Example:
                Input: Proposição: Greg gosta de comer pizza
                Output: Este chunk contém informações sobre os tipos de comida que Greg gosta de comer.

                Responda apenas com o novo resumo do chunk, nada mais.
                """
            },
            {
                "role": "user",
                "content": f"Proposições do chunk:\n{chr(10).join(chunk['propositions'])}\n\nResumo atual do chunk:\n{chunk['summary']}"
            }
        ]

        new_chunk_summary = self.llm.invoke(messages).content
        return new_chunk_summary
    
    def _update_chunk_title(self, chunk):
        """
        Se você adicionar uma nova proposição a um chunk, você pode querer atualizar o título ou ele pode se tornar desatualizado
        """
        messages = [
            {
                "role": "system",
                "content": """
                Você é o guardião de um grupo de chunks que representam grupos de frases que falam sobre um tópico semelhante.
                Uma nova proposição acabou de ser adicionada a um dos seus chunks, você deve gerar um título atualizado muito breve
                que informará aos visualizadores sobre o que um grupo de chunk se trata.

                Um bom título dirá sobre o que o chunk trata.

                Você receberá um grupo de proposições que estão no chunk, o resumo do chunk e o título do chunk.

                Seu título deve antecipar a generalização. Se você receber uma proposição sobre maçãs, generalize para alimentos.
                Ou mês, generalize para "datas e horários".

                Example:
                Input: Resumo: Este chunk é sobre datas e horários sobre os quais o autor fala
                Output: Data e horários

                Responda apenas com o novo título do chunk, nada mais.
                """
            },
            {
                "role": "user",
                "content": f"Proposição do chunk:\n{chr(10).join(chunk['propositions'])}\n\nResumo do chunk:\n{chunk['summary']}\n\nTítulo atual do chunk:\n{chunk['title']}"
            }
        ]

        updated_chunk_title = self.llm.invoke(messages).content
        return updated_chunk_title

    def _get_new_chunk_summary(self, proposition):
        messages = [
            {
                "role": "system",
                "content": """
                Você é o guardião de um grupo de chunks que representam grupos de frases que falam sobre um tópico semelhante.
                Você deve gerar um resumo muito breve de 1 frase que informará aos visualizadores sobre o que um grupo de chunk se trata.

                Um bom resumo dirá sobre o que é o chunk e fornecerá instruções esclarecedoras sobre o que adicionar ao chunk.

                Você receberá uma proposição que irá para um novo chunk. Este novo chunk precisa de um resumo.

                Seus resumos devem antecipar a generalização. Se você receber uma proposição sobre maçãs, generalize para alimentos.
                Ou mês, generalize para "datas e horários".

                Example:
                Input: Proposição: Greg gosta de comer pizza
                Output: Este chunk contém informações sobre os tipos de comida que Greg gosta de comer.

                Responda apenas com o novo resumo do chunk, nada mais.
                """
            },
            {
                "role": "user",
                "content": f"Determine o resumo do novo chunk em que esta proposição será incluída:\n{proposition}"
            }
        ]

        new_chunk_summary = self.llm.invoke(messages).content
        return new_chunk_summary
    
    def _get_new_chunk_title(self, summary):
        messages = [
            {
                "role": "system",
                "content": """
                Você é o guardião de um grupo de chunks que representam grupos de frases que falam sobre um tópico semelhante.
                Você deve gerar um título muito breve com poucas palavras que informará aos visualizadores sobre o que um grupo de chunk se trata.

                Um bom título de chunk é breve, mas abrange o assunto do chunk.

                Você receberá um resumo de um chunk que precisa de um título.

                Seus títulos devem antecipar a generalização. Se você receber uma proposição sobre maçãs, generalize para alimentos.
                Ou mês, generalize para "datas e horários".

                Example:
                Input: Resumo: Este chunk é sobre datas e horários sobre os quais o autor fala
                Output: Datas & Horários

                Responda apenas com o novo título do chunk, nada mais.
                """
            },
            {
                "role": "user",
                "content": f"Determine o título do chunk ao qual este resumo pertence:\n{summary}"
            }
        ]

        new_chunk_title = self.llm.invoke(messages).content
        return new_chunk_title

    def _create_new_chunk(self, proposition):
        new_chunk_id = str(uuid.uuid4())[:self.id_truncate_limit]  # I don't want long ids
        new_chunk_summary = self._get_new_chunk_summary(proposition)
        new_chunk_title = self._get_new_chunk_title(new_chunk_summary)

        self.chunks[new_chunk_id] = {
            'chunk_id': new_chunk_id,
            'propositions': [proposition],
            'title': new_chunk_title,
            'summary': new_chunk_summary,
            'chunk_index': len(self.chunks)
        }
        if self.print_logging:
            print(f"Created new chunk ({new_chunk_id}): {new_chunk_title}")
    
    def get_chunk_outline(self):
        """
        Get a string which represents the chunks you currently have.
        This will be empty when you first start off
        """
        chunk_outline = ""

        for chunk_id, chunk in self.chunks.items():
            single_chunk_string = f"""Chunk ({chunk['chunk_id']}): {chunk['title']}\nResumo: {chunk['summary']}\n\n"""
        
            chunk_outline += single_chunk_string
        
        return chunk_outline

    def _find_relevant_chunk(self, proposition):
        current_chunk_outline = self.get_chunk_outline()

        messages = [
            {
                "role": "system",
                "content": """
                Determine se a "Proposição" deve pertencer a algum dos chunks existentes.

                Uma proposição deve pertencer a um chunk se o significado, a direção ou a intenção deles forem semelhantes.
                O objetivo é agrupar proposições e chunks similares.

                Se você acha que uma proposição deve ser unida a um chunk, retorne o ID do chunk.
                Se você não acha que um item deve ser unido a um chunk existente, apenas retorne "Sem chunks"

                Exemplo:
                Input:
                    - Proposição: "Greg realmente gosta de hambúrgueres"
                    - Chunks Atuais:
                        - ID do Chunk: 2n4l3d
                        - Nome do Chunk: Lugares em São Francisco
                        - Resumo do Chunk: Visão geral das coisas para fazer com Lugares em São Francisco

                        - ID do Chunk: 93833k
                        - Nome do Chunk: Comidas que Greg gosta
                        - Resumo do Chunk: Listas de comidas e pratos que Greg gosta
                Output: 93833k
                """
            },
            {
                "role": "user",
                "content": f"Chunk Atuais:\n--Começo dos chunks atuais--\n{current_chunk_outline}\n--Fim dos chunks atuais--"
            },
            {
                "role": "user",
                "content": f"Determine se a seguinte declaração deve pertencer a um dos chunks destacados:\n{proposition}"
            }
        ]

        chunk_found = self.llm.invoke(messages).content

        # Implementing a simple extraction method for chunk ID
        # Since we don't have the create_extraction_chain_pydantic, we'll use a simpler approach
        # Look for the chunk ID pattern (exactly matching the truncate limit characters)
        import re
        match = re.search(r'\b[a-zA-Z0-9]{' + str(self.id_truncate_limit) + r'}\b', chunk_found)
        
        if match:
            chunk_id = match.group(0)
            # Verify this chunk ID exists in our chunks
            if chunk_id in self.chunks:
                return chunk_id
                
        return None
    
    def get_chunks(self, get_type='dict'):
        """
        This function returns the chunks in the format specified by the 'get_type' parameter.
        If 'get_type' is 'dict', it returns the chunks as a dictionary.
        If 'get_type' is 'list_of_strings', it returns the chunks as a list of strings, where each string is a proposition in the chunk.
        """
        if get_type == 'dict':
            return self.chunks
        if get_type == 'list_of_strings':
            chunks = []
            for chunk_id, chunk in self.chunks.items():
                chunks.append(" ".join([x for x in chunk['propositions']]))
            return chunks
    
    def pretty_print_chunks(self):
        print(f"\nVocê tem {len(self.chunks)} chunks\n")
        for chunk_id, chunk in self.chunks.items():
            print(f"Chunk #{chunk['chunk_index']}")
            print(f"Chunk ID: {chunk_id}")
            print(f"Resumo: {chunk['summary']}")
            print(f"Proposições:")
            for prop in chunk['propositions']:
                print(f"    -{prop}")
            print("\n\n")

    def pretty_print_chunk_outline(self):
        print("Chunk Outline\n")
        print(self.get_chunk_outline())


# Classe para criar proposições usando DeepSeek (funcionalidade extra baseada no artigo)
class LLMPropositionizer: # Rename class for clarity
    # def __init__(self, api_key=None, api_base=None, model='deepseek-chat'):
    def __init__(self, llm: BaseChatModel): # Accept BaseChatModel
         # Store the passed LLM instance
        self.llm = llm # Use the passed llm object

    def text_to_propositions(self, text):
        """
        Converte um texto em uma lista de proposições atômicas
        baseado nas ideias do artigo sobre proposições como unidades de recuperação
        """
        messages = [
            {
                "role": "system",
                "content": """
                Decomponha o texto fornecido em proposições claras e simples que sejam interpretáveis fora de contexto.
                
                Uma proposição é uma afirmação atômica que expressa uma ideia ou fato distinto.
                
                Regras para decomposição:
                1. Divida sentenças compostas em sentenças simples, mantendo a formulação original sempre que possível.
                2. Para entidades nomeadas acompanhadas de informações descritivas, separe essas informações em proposições distintas.
                3. Descontextualize a proposição adicionando os modificadores necessários e substituindo pronomes pelos nomes completos das entidades.
                4. Cada proposição deve ser autocontida e compreensível sem contexto adicional.
                
                Retorne uma lista de proposições, uma por linha. Não adicione numeração ou marcadores.
                """
            },
            {
                "role": "user",
                "content": f"Texto original:\n{text}\n\nGere proposições atômicas a partir deste texto:"
            }
        ]
        
        try:
            result = self.llm.invoke(messages).content
            # Process the result into a list of propositions
            # Remove linhas vazias e espaços extras
            propositions = [p.strip() for p in result.split('\n') if p.strip()] 
            return propositions
        except Exception as e:
            print(f"Erro ao gerar proposições: {e}")
            return [] # Retorna lista vazia em caso de erro


if __name__ == "__main__":
    # Exemplo de uso needs update if you want to run this file directly
    # You would need to instantiate an LLM (like OllamaChat) here first
    try:
        # --- Example setup for running directly (requires langchain_community) ---
        # from langchain_community.chat_models import ChatOllama
        # ollama_llm = ChatOllama(model="llama3:latest") 
        # ac = AgenticChunker(llm=ollama_llm, print_logging=True) 
        # prop_generator = LLMPropositionizer(llm=ollama_llm)
        # --- End Example setup ---

        # Comment out the original example or adapt it
        # ac = AgenticChunker(print_logging=True) # Original instantiation
        # prop_generator = DeepSeekPropositionizer() # Original instantiation
        
        print("Running agentic_chunker.py directly requires manual LLM setup (see comments).")
        
        # text = """O artigo discute diferentes granularidades de recuperação em modelos de linguagem. 
        # Retrieval by propositions supera retrieval por sentenças ou passagens na maioria das tarefas 
        # para recuperadores não supervisionados e supervisionados. O céu é azul e a grama é verde."""
        
        # print("Gerando proposições...")
        # propositions = prop_generator.text_to_propositions(text)
        
        # if propositions:
        #     print(f"Proposições geradas: {propositions}")
        #     ac.add_propositions(propositions)
            
        #     # Imprimir resultados
        #     ac.pretty_print_chunks()
        #     ac.pretty_print_chunk_outline()
        #     print("\nChunks como lista de strings:")
        #     print(ac.get_chunks(get_type='list_of_strings'))
        # else:
        #     print("Nenhuma proposição foi gerada.")

    except ValueError as ve:
         print(f"Erro de configuração: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    # Exemplo com proposições diretas (comentar o bloco acima se usar este)
    # try:
    #     ac = AgenticChunker(print_logging=True)
    #     propositions_direct = [
    #         'O mês é Outubro.',
    #         'O ano é 2023.',
    #         "Uma das coisas mais importantes que eu não entendi sobre o mundo quando criança foi o grau em que os retornos pelo desempenho são superlineares.",
    #         'Professores e treinadores implicitamente nos disseram que os retornos eram lineares.',
    #         "Eu ouvi mil vezes que 'Você recebe de volta o que você coloca'.",
    #     ]
    #     print("Adicionando proposições diretas...")
    #     ac.add_propositions(propositions_direct)
    #     ac.pretty_print_chunks()
    #     ac.pretty_print_chunk_outline()
    #     print("\nChunks como lista de strings:")
    #     print(ac.get_chunks(get_type='list_of_strings'))
    # except ValueError as ve:
    #      print(f"Erro de configuração: {ve}")
    # except Exception as e:
    #     print(f"Ocorreu um erro inesperado: {e}")