#Mini Projeto - Visualização de Dados e Business Intelligence 
# Curso: SENAI/SC - Lab 365 (Módulo: M1S07)
# Professor: Rodrigo Garcia Brunini

### Autor: [Petras Ruben Carvalho] ###
### Data: 2026-05-24 ###

### Importando bibliotecas necessárias ###

import pandas as pd
import numpy as np
from datetime import datetime

# ===============================================================================================================
# 1. Carregando os dados do arquivo CSV para um DataFrame do Pandas com separação por ponto e vírgula e codificação UTF-8
# ===============================================================================================================

base_varejo = pd.read_csv("C:\\Mini_Projeto\\Nao Processado\\Mini_Projeto.csv", sep=';', encoding='utf-8')

print("===============================================================================================================")

# ===============================================================================================================
# 2. Explorando os dados
# ===============================================================================================================

print(base_varejo.head())  
print("===============================================================================================================")
print(base_varejo.info())  
print(base_varejo.shape)  

print("===============================================================================================================")

### Inciciando o tratamento dos dados ###

# ===============================================================================================================
# 3. Verificando a presença de valores nulos
# ===============================================================================================================

print(base_varejo.isnull().sum()) 
print(f"\nTotal de valores nulos: {base_varejo.isnull().sum().sum()}")
print("===============================================================================================================")

# 3.1 Na verificação de valores nulos, a contagem foi de 0, contudo, no excel, observei que nas colunas PR_CAT e PR_NOME,
# existem células identificadas como #N/D, que não foram reconhecida como valores nulos, contudo, 
# esses valores precisam ser tratados para a analise.
# Exibir a quantidade de ocorrências de '#N/D' nas colunas PR_CAT e PR_NOME

nd_cat = (base_varejo['PR_CAT'] == '#N/D').sum()
nd_nome = (base_varejo['PR_NOME'] == '#N/D').sum()
print(f"\nTotal de ocorrências de '#N/D' na coluna PR_CAT: {nd_cat}")
print(f"Total de ocorrências de '#N/D' na coluna PR_NOME: {nd_nome}")
print("===============================================================================================================")

# 3.2. Substituindo os valores '#N/D' por 'Sem Categoria' usando os comandos if/else.
# Mantém o valor original se não for #N/D
def sub_nd_por_sem_categoria(categoria):
    if categoria == '#N/D':
        return 'Sem Categoria'
    else:
        return categoria

# Aplicamos a função usando o .apply() nas colunas específicas
base_varejo['PR_CAT'] = base_varejo['PR_CAT'].apply(sub_nd_por_sem_categoria)
base_varejo['PR_NOME'] = base_varejo['PR_NOME'].apply(sub_nd_por_sem_categoria)

# Verificando o resultado do tratamento de #N/D

print("Nulos por coluna. (Lembrando que 'Sem Categoria' agora é um texto válido!)")
print(base_varejo.isnull().sum())
print("===============================================================================================================")

# Verificando a auteração de #N/D para 'Sem Categoria'
# Exibe as 100 primeiras linhas que foram alteradas para 'Sem Categoria'
# Optei pela não remoção dos dados com #N/D, pois acredito que a transformação desses dados para "Sem Categoria" pode ser relevante para a análise.

print(base_varejo[base_varejo['PR_CAT'] == 'Sem Categoria'][['PR_CAT', 'PR_NOME']])
print("===============================================================================================================")
print(base_varejo.head(100))   
print("===============================================================================================================")

# ===============================================================================================================
# 4. Convertendo a coluna 'Data' para o formato datetime 
# ===============================================================================================================

base_varejo['DATA'] = pd.to_datetime(base_varejo['DATA'], format='%d/%m/%Y')


# 4.1 Verificando o tipo de dados da coluna 'DATA' após a conversão
print(base_varejo.info())
print("===============================================================================================================")

# 4.2. Verificando a presença de datas inválidas
print("\nPrimeiras linhas da coluna DATA:")
print(base_varejo['DATA'].head())
print(base_varejo['DATA'].head(100))
print("===============================================================================================================")

# 4.3. Validação de Nulos: Garante que nenhuma data real virou nula por erro de digitação
print(f"\nTotal de valores nulos na coluna DATA após a conferência: {base_varejo['DATA'].isnull().sum()}")
print("===============================================================================================================")

# 4.4 Contagem das linhas que possuem dados preenchidos o resultado deve ser igual ao número total do DataFrame, 
# indicando que todas as datas foram convertidas corretamente.
total_datas_linhas = base_varejo['DATA'].count()
print(f"Quantidade de linhas com datas válidas: {total_datas_linhas} de {base_varejo.shape[0]} linhas totais.")
print("===============================================================================================================")

# ===============================================================================================================
# 5. Verificando a presença de valores duplicados
# ===============================================================================================================

print(f"\nTotal de valores duplicados: {base_varejo.duplicated().sum()}")
print("===============================================================================================================")
print(base_varejo.head(100))   
print("===============================================================================================================")

# Tivemos 96553 numeros de linhas duplicadas, acredito que sejo por causa das colunas CO_ID, CL_ID e PR_ID, 
# que são as chaves primárias, ou seja, a combinação dessas colunas deve ser única para cada linha.


# ===============================================================================================================
# 6. Transformando as colunas CO_ID, CL_ID e PR_ID de int64 para string, assim evitamo sproblemas de formatação facilitando a análise.
# ===============================================================================================================

base_varejo['CO_ID'] = base_varejo['CO_ID'].astype(str)
base_varejo['CL_ID'] = base_varejo['CL_ID'].astype(str)
base_varejo['PR_ID'] = base_varejo['PR_ID'].astype(str)

# Verificando os tipos de dados após a conversão.

print(base_varejo.info())  
print("===============================================================================================================")

# ===============================================================================================================
# 7. Realizando o Agrupamento por todas as colunas usando a média (.mean). Como as linhas são idênticas, a média mantém os valores originais intactos,
# e o resultado é um DataFrame sem linhas duplicadas, ou seja, com 96553 linhas a menos do que o DataFrame original.
# ===============================================================================================================

base_varejo_agrupado = base_varejo.groupby(list(base_varejo.columns), as_index=False).mean()

# 7.1. Pegando as quantidades de linhas para validar o resultado do agrupamento. 
# A diferença entre as quantidades de linhas antes e depois do agrupamento deve ser exatamente 96553, 
# que é o número de linhas duplicadas identificadas anteriormente.

linhas_antes = base_varejo.shape[0]
linhas_depois = base_varejo_agrupado.shape[0]
resultado = linhas_antes - linhas_depois

# 7.2. Verificação do resultado do agrupamento.
print(f"Quantidade de linhas DEPOIS: {linhas_depois}")
print(f"Diferença (Antes - Depois): {resultado}")
print("===============================================================================================================")

### Análise Estatística Descritiva 01 ###

# ===============================================================================================================
# 8. Analisando a coluna CL_FHL, para saber a média, mediana, desvio padrão, moda, máximo, mínimo e contagem.
# ===============================================================================================================

# 8.1. Calculando cada métrica solicitada para a coluna CL_FHL.
media = base_varejo['CL_FHL'].mean()
mediana = base_varejo['CL_FHL'].median()
desvio_padrao = base_varejo['CL_FHL'].std()
maximo = base_varejo['CL_FHL'].max()
minimo = base_varejo['CL_FHL'].min()
contagem = base_varejo['CL_FHL'].count()

# 8.2. Exibindo os resultados de forma limpa e organizada. OBS: O :.2f serve para mostrar apenas 2 casas decimais.
print(f"Contagem (Total de registros): {contagem}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
print(f"Média: {media:.2f}")         
print(f"Mediana: {mediana}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print("===============================================================================================================")

# 8.3 No processo anterior a mediana retornou 0.0. Para Validar esse resuldato realizei um teste para validar a mediana. 
# Mostra a porcentagem de zeros na coluna CL_FHL(teste mediana)
total_zeros = (base_varejo['CL_FHL'] == 0).sum()
porcentagem_zeros = (total_zeros / contagem) * 100
print(f"Porcentagem de linhas com valor 0: {porcentagem_zeros:.2f}%")
print("===============================================================================================================")

# O resultado do teste retornou 52,47%, ou seja, mais da metade dos registros na coluna CL_FHL possuem o valor 0, 
# o que explica a mediana ser 0.0, pois a mediana é o valor que separa a metade inferior da metade superior dos dados, 
# e nesse caso, como mais da metade dos valores são 0, a mediana também é 0.


### Análise Estatística Descritiva 02 ###

# ===============================================================================================================
# # 9. Realizando o agrupamento por Gênero e ID do Produto para contar as compras.
# Usamos o .size() para contar as linhas e .reset_index() para manter o formato de tabela.
# Atribui o nome 'QUANTIDADE_COMPRAS' para a nova coluna que contém a contagem de compras.
# ===============================================================================================================

compras_por_genero = base_varejo.groupby(['CL_GENERO', 'PR_ID']).size().reset_index(name='QUANTIDADE_COMPRAS')

# 9.1. Somando o total de compras absoluto de cada gênero para descobrir quem compra mais
total_por_genero = compras_por_genero.groupby('CL_GENERO')['QUANTIDADE_COMPRAS'].sum().reset_index()

# 9.2. Ordenando o resultado para que o maior comprador fique no topo.
total_por_genero_ordenado = total_por_genero.sort_values(by='QUANTIDADE_COMPRAS', ascending=False)

# 9.3. Exibindo o resultado final
print("TOTAL DE COMPRAS POR GÊNERO")
print(total_por_genero_ordenado)
print("===============================================================================================================")

# Pegando o gênero que mais  (o primeiro da tabela ordenada)
genero_compras = total_por_genero_ordenado.iloc[0]['CL_GENERO']
qtd_compras = total_por_genero_ordenado.iloc[0]['QUANTIDADE_COMPRAS']
print(f"O gênero que mais compra é o '{genero_compras}' com um total de {qtd_compras} produtos adquiridos.")
print("===============================================================================================================")

# ===============================================================================================================
# 10. Salvando o DataFrame processado em um novo arquivo CSV
# ===============================================================================================================

base_varejo.to_csv(r"C:\Mini_Projeto\Processado\Mini_Projeto_Limpo.csv", index=False, encoding='utf-8')
print("Processamento concluído. O arquivo 'Mini_Projeto_Limpo.csv' foi salvo com sucesso.")



