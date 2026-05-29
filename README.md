# Mini Projeto - Visualização de Dados e Business Intelligence 
# Curso: SENAI/SC - Lab 365 (Módulo: M1S07)
# Professor: Rodrigo Garcia Brunini

Este repositório contém o desenvolvimento completo do pipeline de engenharia, tratamento e análise estatística de uma base de dados do setor de varejo exportada da plataforma KAGGLE. O objetivo principal do projeto é estruturar dados brutos, aplicar técnicas rigorosas de limpeza (Data Cleaning) e extrair métricas descritivas para suporte à tomada de decisão.

## 📊 Ferramentas e Tecnologias Utilizadas

* **VS Code** (Ambiente de Desenvolvimento Integrado)
* **Python 3** (Linguagem base do projeto)
* **Pandas & NumPy** (Bibliotecas fundamentais para manipulação de DataFrames e análise numérica)
* **Git & GitHub** (Controle de versão, histórico de commits e hospedagem de código)

## 📁 Estrutura de Diretórios Local

* `C:\Teste_GIT\Base_Varejo\Nao Processado\`: Armazena o arquivo bruto original (`Base Varejo.csv`).
* `C:\Teste_GIT\Base_Varejo\Processado\`: Diretório de destino para a base tratada (`Base_Varejo_Limpo.csv`).

## ⚙️ Arquitetura do Pipeline e Lógica de Negócio

O script executa um fluxo estruturado dividido em etapas essenciais de qualidade de dados:

### 1. Carga de Dados e Auditoria Inicial

* **Leitura Customizada:** Importação do CSV utilizando o delimitador ponto e vírgula (`sep=';'`) e codificação padrão `utf-8`.
* **Auditoria de Metadados:** Avaliação estrutural do formato, volumetria e tipos primitivos de dados com as funções `.head()`, `.info()` e `.shape`.

### 2. Tratamento de Anomalias e Nulos Ocultos

* **Mapeamento Pragmático:** O método tradicional `.isnull()`Na verificação de valores nulos, a contagem foi de 0, contudo, no excel, observei que nas colunas PR_CAT e PR_NOME, existem células identificadas como #N/D, que não foram reconhecida como valores nulos, contudo, esses valores precisam ser tratados para a analise.

* **Função Personalizada:** Desenvolvimento de lógica condicional (`if/else`) associada ao método `.apply()` para mapear e converter essas ocorrências #N/D em um rótulo válido chamado `'Sem Categoria'`, preservando a integridade do histórico para as análises volumétricas.

### 3. Engenharia de Tipos (Data Casting)

* **Mapeamento Temporal:** Conversão da coluna `DATA` de formato texto (`str`) para objeto nativo de tempo (`datetime`), com validação rigorosa pós-conversão para garantir que nenhuma data válida tenha sido corrompida ou transformada em `NaT`.

* **Isolamento de Chaves Primárias:** Conversão das colunas de chaves (`CO_ID`, `CL_ID` e `PR_ID`) de formato numérico (`int64`) para formato de texto (`str`). Isso blinda o banco de dados contra erros de truncamento de zeros à esquerda ou operações matemáticas acidentais sobre identificadores.

### 4. Deduplicação Estratégica de Registros

* A análise estrutural identificou **96.553 linhas estritamente duplicadas**, causadas pela repetição idêntica de combinações de chaves.

* **Resolução Matemática:** Aplicação de agrupamento em massa utilizando a lista completa de colunas associada à função agregadora de média (`.groupby().mean()`). Como as linhas eram réplicas perfeitas, a média preservou perfeitamente os valores originais, removendo com precisão matemática as 96.553 redundâncias sem perda de informação.

### 5. Análise Estatística Descritiva

* **Distribuição da Coluna `CL_FHL`.** Levantamento estatístico de Média, Mediana, Desvio Padrão, Mínimo, Máximo e Contagem.**
  * **Validação de Comportamento:** A mediana retornou estritamente `0.0`. Para Validar esse resuldato realizei um teste a mediana., revelando que **52,47% de toda a base possui o valor exato de zero**. Isso valida matematicamente o porquê de a mediana se fixar em `0.0`, comprovando o comportamento. 

* **Análisepor Gênero (`CL_GENERO`):** Agrupamento granular unindo CL_GENERO e PR_ID de produto para extração da volumetria absoluta de compras, ordenando de forma decrescente para expor o genero de consumidor com maior tração comercial.

### 6. Salvandos os Dados (Exportação)

* Salvamento do DataFrame tratado utilizando `index=False` para eliminar o salvamento de colunas de índices do Pandas.

### 7. Salvando no GitHub 

* Utilizei os comandos:
  git add .                     #Preparando os dados para upload
  git commit -m                 #Salvando as configurações para upload
  git pull origin main --rebase #Extraido e organizando as alterações
  git push -u origin main       #Salvando as autereções no repositório GitHub

### 7.1 Atualizando e salvando README

* Utilizei os comandos:
  git add README_Petras_Ruben_Carvalho #Preparando os dados para upload
  git commit -m                        #Salvando as configurações para upload
  git pull origin main --rebase #Extraido e organizando as alterações
  git push -u origin main       #Salvando as autereções no repositório GitHub

## 🏁 Conclusão

O desenvolvimento deste projeto consolidou de forma prática as etapas essenciais de um pipeline real de Análise e Engenharia de Dados (Data Analytics & Data Cleaning), utilizando Python e a biblioteca Pandas como pilares estratégicos.

### 🎯 Principais Entregas e Aprendizados:

* **Qualidade de Dados Realista:** O projeto provou que auditorias visuais e de negócio são indispensáveis. A simples aplicação de métodos automatizados como `.isnull()` indicava uma base perfeita, mas a análise crítica permitiu identificar e tratar anomalias ocultas (valores `#N/D`), transformando-as em dados válidos (`Sem Categoria`) sem perder histórico de vendas.

* **Governança e Integridade:** A conversão correta de dados temporais para `datetime` e a tipagem de chaves primárias (`CO_ID`, `CL_ID`, `PR_ID`) para texto (`str`) garantiram uma base blindada contra erros de truncamento e pronta para integrações em ferramentas de BI.

* **Eficiência Estatística (Deduplicação):** A resolução matemática aplicada para eliminar **96.553 registros duplicados** através de agrupamento reduziu o ruído analítico da base de maneira cirúrgica, preservando a integridade das métricas originais.

* **Validação Científica:** O levantamento estatístico descritivo da coluna `CL_FHL` demonstrou maturidade analítica ao provar, por meio de testes de densidade, o porquê de a mediana fixar-se em `0.0` (visto que `52,47%` da base continha o valor zero), mapeando com precisão o comportamento real de consumo.

* **Inteligência de Mercado:** O cruzamento demográfico mapeou o perfil de consumo e o share de compras por gênero, gerando os primeiros insights comerciais consolidados para direcionamento estratégico de campanhas.

Com a base de dados perfeitamente limpa, padronizada e exportada, o projeto cumpre com sucesso sua etapa de *Data Preparation*, estando 100% maduro e estruturado para a próxima fase: a criação de painéis visuais dinâmicos e relatórios gerenciais avançados.

---
Projeto desenvolvido por **Petras Ruben Carvalho** *Data de Atualização: 25 de Maio de 2026*
