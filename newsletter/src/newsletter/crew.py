from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

@CrewBase
class NewsletterCrew():
    """Define a equipe (crew) para criação da Newsletter."""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # --- AGENTES ---

    @agent
    def pesquisador(self) -> Agent:
        return Agent(
            # Correção: Acessar a chave 'agentes' primeiro
            config=self.agents_config['agentes']['pesquisador'],
            tools=[search_tool],
            verbose=True
        )

    @agent
    def analista(self) -> Agent:
        return Agent(
            # Correção: Acessar a chave 'agentes' primeiro
            config=self.agents_config['agentes']['analista'],
            verbose=True
        )

    @agent
    def expansao(self) -> Agent:
        return Agent(
            # Correção: Acessar a chave 'agentes' primeiro
            config=self.agents_config['agentes']['expansao'],
            tools=[search_tool],
            verbose=True
        )

    @agent
    def guardiao(self) -> Agent:
        return Agent(
            # Correção: Acessar a chave 'agentes' primeiro
            config=self.agents_config['agentes']['guardiao'],
            verbose=True
        )
    
    @agent
    def editor(self) -> Agent:
        return Agent(
            # Correção: Acessar a chave 'agentes' primeiro
            config=self.agents_config['agentes']['editor'],
            verbose=True
        )

    # --- TAREFAS ---
    
    @task
    def pesquisa_de_noticias(self) -> Task:
        return Task(
            # Correção: Acessar a chave 'tasks' primeiro
            config=self.tasks_config['tasks']['pesquisa_de_noticias'],
            agent=self.pesquisador()
        )

    @task
    def analise_e_sumarizacao(self) -> Task:
        return Task(
            # Correção: Acessar a chave 'tasks' primeiro
            config=self.tasks_config['tasks']['analise_e_sumarizacao_factual'],
            agent=self.analista(),
            context=[self.pesquisa_de_noticias()]
        )
        
    @task
    def expansao_de_conteudo(self) -> Task:
        return Task(
            # Correção: Acessar a chave 'tasks' primeiro
            config=self.tasks_config['tasks']['expansao_com_perspectivas'],
            agent=self.expansao(),
            context=[self.analise_e_sumarizacao()]
        )

    @task
    def filtro_etico(self) -> Task:
        return Task(
            # Correção: Acessar a chave 'tasks' primeiro
            config=self.tasks_config['tasks']['filtro_de_alinhamento_com_constituicao'],
            agent=self.guardiao(),
            context=[self.analise_e_sumarizacao(), self.expansao_de_conteudo()]
        )

    @task
    def montagem_da_newsletter(self) -> Task:
        return Task(
            # Correção: Acessar a chave 'tasks' primeiro
            config=self.tasks_config['tasks']['compilacao_final_em_markdown'],
            agent=self.editor(),
            context=[self.filtro_etico()],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )