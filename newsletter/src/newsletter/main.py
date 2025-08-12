#!/usr/bin/env python
import sys
from newsletter.crew import NewsletterCrew

# Este arquivo principal destina-se a ser uma maneira de você executar sua equipe
# localmente. Evite adicionar lógica desnecessária a este arquivo.
# Substitua pelas entradas que você deseja testar; ele irá interpolar
# automaticamente quaisquer informações de tarefas e agentes.

def run():
    """
    Executa a equipe com as entradas definidas.
    """
    # Defina as entradas para a sua equipe aqui.
    # A 'constitution' é usada pelo Agente Guardião para filtrar o conteúdo.
    inputs = {
        'topic': 'Avanços em Inteligência Artificial e LLMs em 2025',
        'constitution': """
        1. Foco na Objetividade: Priorizar reportagens factuais e baseadas em dados. Evitar conteúdo excessivamente especulativo ou sensacionalista.
        2. Balanceamento de Perspectivas: Para qualquer tópico controverso, incluir pontos de vista de diferentes lados, desde que bem fundamentados.
        3. Evitar Discurso de Ódio e Extremismo: Excluir qualquer conteúdo que promova violência, discriminação ou teorias da conspiração infundadas.
        4. Relevância e Atualidade: O conteúdo deve ser recente e diretamente relacionado ao tópico principal.
        5. Fonte Confiável: Dar preferência a fontes de notícias com um histórico estabelecido de jornalismo de qualidade e evitar fontes conhecidas por desinformação.
        6. Foco Técnico para Engenheiros: Incluir detalhes técnicos ou análises que sejam relevantes para um estudante de Engenharia da Computação, quando possível.
        """
    }
    
    try:
        # Inicia a execução da equipe com as entradas fornecidas.
        # A classe foi renomeada para NewsletterCrew no arquivo crew.py
        NewsletterCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        # Captura e exibe qualquer erro que ocorra durante a execução.
        print(f"Ocorreu um erro ao executar a equipe: {e}")

if __name__ == "__main__":
    run()