import numpy as np

# importando o dataset
ds = np.loadtxt('space.csv',
                    delimiter = ';',
                    dtype = str,
                    encoding = 'utf-8') #delimiter significa o separador de cada dado(importante todos para string usando dtype str)
# Colunas do dataset
print(ds[0, :])

# calculando a media de uma missao espacial
# slicing para extrair a coluna custo(Cost)
ds_cost = ds[1:, 6] # todas as linhas, mas apenas a coluna 6
# Transformando os valores em Float
ds_cost = ds_cost.astype(float)
# Calculando a media
print(ds_cost.mean())