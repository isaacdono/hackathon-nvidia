# Newsletter com Agentes de IA

## Descrição

Inspirado no Hackathon da Nvidia na Semana da Computação de minha universidade, tive a ideia desta aplicação com o auxílio de IA.
O projeto utiliza um **sistema multiagente (CrewAI)** para gerar newsletters personalizadas sob demanda.

A saída final é um arquivo em formato Markdown, pronto para leitura ou distribuição.

## Funcionalidades Principais

  * Sumarização de notícias principais sobre um tópico específico.
  * Curadoria de conteúdo relacionado com base nos interesses do usuário.
  * Filtragem de conteúdo baseada em uma "constituição" de valores definida pelo usuário.
  * Inclusão de diferentes perspectivas e análises críticas sobre o tema.
  * Geração automática da newsletter em formato Markdown.

## Como Funciona: A Arquitetura Multiagente

O sistema é composto por uma equipe de agentes de IA, cada um com uma responsabilidade específica e bem definida:

  * **Agente Pesquisador:** Responsável por coletar um grande volume de dados brutos sobre o tópico solicitado a partir de múltiplas fontes de notícias e APIs.
  * **Agente Analista:** Processa os dados coletados para identificar e sumarizar as notícias mais relevantes e factuais.
  * **Agente de Expansão:** Procura por conteúdo complementar, incluindo artigos de opinião, análises profundas e tópicos relacionados que possam ser de interesse do usuário.
  * **Agente Guardião:** Atua como um filtro ético. Ele avalia todo o conteúdo selecionado (sumários, artigos, opiniões) para garantir que esteja alinhado com a "constituição" de princípios do usuário.
  * **Curador de Imagens:** Busca uma imagem relevante e de alta qualidade que represente o tema.
  * **Agente Editor:** Recebe o conteúdo final aprovado pelo Guardião e o estrutura em um arquivo Markdown coeso e bem formatado.
