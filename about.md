## Introdução

O presente projeto tem como objetivo analisar os dados do ENEM na região Centro-Oeste do Brasil, compreendendo os anos de 2018 a 2022. O ENEM é uma avaliação nacional realizada anualmente com o intuito de medir o desempenho dos estudantes e contribuir para o acesso ao ensino superior. Nossa análise é dividida em várias seções, cada uma abordando uma perspectiva específica dos dados.

## Dados

Os dados foram obtidos por meio de arquivos Parquet para cada ano de aplicação do ENEM, cobrindo os seguintes anos: 2018, 2019, 2020, 2021 e 2022. Cada conjunto de dados foi carregado e consolidado em um único DataFrame para possibilitar a análise comparativa.

## Limpeza e Tratamento

### Exclusão de Colunas

- Foram excluídas colunas de questões socioeconômicas, respostas e gabaritos.
- Colunas relacionadas a códigos de município, estado e códigos de prova também foram excluídas.

### Unificação de Colunas

- As colunas de presença nas diferentes provas foram unificadas, representando se o aluno esteve presente em todas as provas ou não.

### Tratativa dos Dados

- Foram criadas tabelas "de-para" para representar valores categóricos em formato numérico.
- Valores nulos foram tratados, incluindo a exclusão de linhas de participantes com presença nula.
- Notas nulas foram preenchidas com zero.
- A idade dos participantes foi categorizada em faixas etárias.

### Exportação dos Dados Tratados

Os dados tratados foram exportados para um arquivo CSV chamado "ENEM_CO_TRATADO.csv".

## Análise Exploratória

A análise exploratória dos dados foi realizada para obter insights relevantes sobre os participantes do ENEM na região Centro-Oeste.

### Faixa Etária dos Inscritos

Foi observado que a maioria dos participantes tem entre 17 e 19 anos, correspondendo aos anos finais do ensino médio e à fase de cursinho preparatório.

### Evolução da Faixa Etária

A faixa etária dos participantes se manteve concentrada entre 17 e 19 anos ao longo dos anos, com uma diminuição notável de participantes acima de 20 anos em 2020 e 2022.

### Perfil Escolar dos Participantes

A proporção de participantes de escolas particulares e públicas se manteve relativamente constante ao longo dos anos. A quantidade de participantes que não responderam a essa pergunta diminuiu significativamente entre 2020 e 2022.

### Presença e Ausência

A quantidade de ausentes teve um aumento expressivo em 2020, possivelmente devido à pandemia da COVID-19. Nos anos subsequentes, a presença foi se normalizando.

### Quantidade de Inscritos e Presentes

A quantidade de inscritos e presentes teve uma diminuição acentuada em 2020, possivelmente influenciada pela pandemia. Os anos seguintes apresentaram uma recuperação gradual, mas não voltaram aos níveis pré-pandemia.


### Participação e Presença

Nesta seção, exploramos a evolução da participação e da presença dos candidatos no ENEM ao longo dos anos. Observamos que houve uma redução na quantidade de inscritos e presentes nos últimos anos, principalmente após o início da pandemia em 2020. Esta queda pode ser atribuída a vários fatores, incluindo a situação de saúde pública e outras circunstâncias.

### Pandemia e Participação

Analisamos o impacto da pandemia nas taxas de participação. Identificamos que o ano de 2020, quando a pandemia estava no auge, apresentou uma queda acentuada tanto na participação quanto na conversão de inscritos em presentes na prova. Essa queda pode ser resultado da preocupação das pessoas em relação à saúde, restrições de mobilidade e outros fatores decorrentes da pandemia.

### Preferência de Língua

Investigamos as preferências dos inscritos em relação à prova de língua estrangeira nos últimos cinco anos. Observamos uma redução na escolha da prova de espanhol em comparação com a prova de inglês de 2020 a 2022. No entanto, não identificamos uma relação clara entre a escolha da língua estrangeira e a proximidade geográfica de países que falam espanhol.

### Notas Gerais

Analisamos a distribuição das notas gerais (excluindo a nota de redação) nos últimos cinco anos. Observamos uma mudança nos patamares de notas acima de 600 a partir de 2020, com uma diminuição no volume de notas altas. No entanto, as análises de box plot indicaram uma ampliação das notas, contradizendo a primeira impressão.

### Notas de Redação

Exploramos várias análises relacionadas às notas de redação dos participantes:

- Analisamos a distribuição das notas de redação ao longo dos anos por meio de gráficos de box plot, identificando mudanças na distribuição e nas medianas.
- Calculamos as correlações entre as notas de redação e as notas nas provas de linguagens e códigos, bem como as notas gerais, identificando relações de associação.
- Investigamos os diferentes tipos de redação (status) ao longo dos anos, mostrando como os status de redação variaram.

### Alunos do Terceiro Ano

Analisamos os alunos do terceiro ano do ensino médio e suas notas de redação. Observamos que os alunos do terceiro ano apresentaram notas de redação superiores à média geral dos participantes desde 2019, com uma diferença que aumentou após 2020. Também identificamos uma queda significativa na participação de terceiro-anistas após o início da pandemia.

##  Conclusão

Nesta seção, destacamos as principais dificuldades, aprendizados e pontos positivos do projeto:

### Dificuldades e Aprendizados

- O curto tempo para selecionar o conjunto de dados e as dificuldades em trabalhar com um dataset muito grande.
- Dificuldades em garantir a reprodutibilidade em um ambiente colaborativo e versionado.

### Pontos Positivos

- Trabalho em equipe multidisciplinar.
- Oportunidade de troca de experiências entre membros da equipe.

### Melhorias Futuras

- Realização de testes estatísticos de normalidade e hipótese.
- Exploração de análises mais avançadas e detalhadas em futuros projetos.

Este projeto oferece uma visão abrangente das tendências e características dos participantes do ENEM, permitindo uma compreensão mais profunda de como fatores como pandemia, tipo de escola, língua estrangeira e outras variáveis impactam os resultados dos alunos.

Nosso brainstorm: https://docs.google.com/document/d/1glOZW6rd96mHSCWUo1fBT1F2LVegyK3n_5nuEmWe9aw/edit?usp=sharing