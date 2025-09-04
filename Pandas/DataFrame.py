import pandas as pd
import numpy as np

np.random.seed(10)

df = pd.DataFrame(
    index=['A','B','C','D','E'],
    columns = ['W','X','Y','Z'],
    data = np.random.randint(1, 50, [5, 4])
    ) # criando um dataframe, index representa as linhas, columns as colunas e data sao os elementos dentro delas
print(df)

# FAZENDO SLICINGS COM iloc (padrão Numpy - indices numéricos)
print(df.iloc[0:2, :]) # iloc continua usando os numeros como numpy

# FAZENDO SLICING COM LOC
print(df.loc[['A', 'B'], ['W', 'X', 'Y', 'Z']]) # usando slicing como indices costumizaveis(colocados no dataframa)
print(df.loc[['A', 'B'], ['W', 'Y']]) # é possivel pegar colunas distantes apenas escolhendo pelos indices
