import os
import requests
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class PexelsSearchInput(BaseModel):
    """Input schema para a ferramenta de busca de imagens no Pexels."""
    search_query: str = Field(..., description="O termo de busca para encontrar uma imagem relevante no Pexels.")

class PexelsImageSearchTool(BaseTool):
    name: str = "Pexels Image Search"
    description: str = (
        "Busca no Pexels por uma imagem de alta qualidade e de uso livre com base em um termo de busca e retorna seu URL."
    )
    args_schema: Type[BaseModel] = PexelsSearchInput

    def _run(self, search_query: str) -> str:
        """
        Executa a busca de imagem na API do Pexels.
        """
        api_key = os.getenv("PEXELS_API_KEY")
        if not api_key:
            return "Erro: A chave da API do Pexels (PEXELS_API_KEY) não foi encontrada no ambiente."

        headers = {
            "Authorization": api_key
        }
        url = "https://api.pexels.com/v1/search"
        params = {
            "query": search_query,
            "per_page": 1,
            "orientation": "portrait"
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status() # Lança um erro para respostas HTTP ruins (4xx ou 5xx)
            data = response.json()

            if data.get("photos"):
                # Retorna a URL da imagem no tamanho 'large2x' para alta qualidade
                return data["photos"][0]["src"]["large2x"]
            else:
                return f"Nenhuma imagem encontrada para a busca: '{search_query}'."

        except requests.exceptions.RequestException as e:
            return f"Erro ao acessar a API do Pexels: {e}"