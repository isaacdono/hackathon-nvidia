# import os
# import requests
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from ddgs import DDGS

# class PexelsSearchInput(BaseModel):
#     """Input schema para a ferramenta de busca de imagens no Pexels."""
#     search_query: str = Field(..., description="O termo de busca para encontrar uma imagem relevante no Pexels.")

# class PexelsImageSearchTool(BaseTool):
#     name: str = "Pexels Image Search"
#     description: str = (
#         "Busca no Pexels por uma imagem de alta qualidade com base em um termo de busca e retorna seu URL."
#     )
#     args_schema: Type[BaseModel] = PexelsSearchInput

#     def _run(self, search_query: str) -> str:
#         """
#         Executa a busca de imagem na API do Pexels.
#         """
#         api_key = os.getenv("PEXELS_API_KEY")
#         if not api_key:
#             return "Erro: A chave da API do Pexels (PEXELS_API_KEY) não foi encontrada no ambiente."

#         headers = {
#             "Authorization": api_key
#         }
#         url = "https://api.pexels.com/v1/search"
#         params = {
#             "query": search_query,
#             "per_page": 1,
#             "orientation": "portrait"
#         }

#         try:
#             response = requests.get(url, headers=headers, params=params)
#             response.raise_for_status() # Lança um erro para respostas HTTP ruins (4xx ou 5xx)
#             data = response.json()

#             if data.get("photos"):
#                 # Retorna a URL da imagem no tamanho 'large2x' para alta qualidade
#                 return data["photos"][0]["src"]["large2x"]
#             else:
#                 return f"Nenhuma imagem encontrada para a busca: '{search_query}'."

#         except requests.exceptions.RequestException as e:
#             return f"Erro ao acessar a API do Pexels: {e}"

class DDGImageSearchInput(BaseModel):
    """Input schema for the DuckDuckGo Image Search tool."""
    search_query: str = Field(..., description="The search query for finding a relevant image.")

class DDGImageSearchTool(BaseTool):
    name: str = "DuckDuckGo Image Search"
    description: str = (
        "Searches DuckDuckGo for a relevant, high-quality, and royalty-free image "
        "based on a search query and returns its URL."
    )
    args_schema: Type[BaseModel] = DDGImageSearchInput

    def _run(self, search_query: str) -> str:
        """
        Executes the image search using the duckduckgo_search library.
        """
        try:
            # O 'max_results=1' garante que pegamos apenas o melhor resultado
            results = DDGS().images(
                query=search_query,
                region="wt-wt",
                safesearch="moderate",
                size=None,
                color=None,
                type_image=None,
                layout=None,
                license_image=None,
                max_results=1
            )

            if results:
                # Retorna a URL da imagem do primeiro resultado
                return results[0]["image"]
            else:
                return f"Nenhuma imagem encontrada para a busca: '{search_query}'."

        except Exception as e:
            return f"Erro ao acessar a busca de imagens do DuckDuckGo: {e}"