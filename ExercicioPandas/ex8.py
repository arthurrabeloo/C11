import pandas as pd
import numpy as np

np.random.seed(10) # colocando a semente para se iniciar em 10
df = pd.DataFrame(
    index=['A','B','C','D','E'],
    columns=['W','X','Y','Z'],
    data=np.random.randint(1, 50, [5, 4])
) # criando o dataframe

# Fazendo o slicing: linhas A, C, E e colunas X, Y
df_slicing = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print('Slicing:', df_slicing)

# Somando as linhas
print('Soma linha A: ', df_slicing.loc['A'].sum())
print('Soma linha C: ', df_slicing.loc['C'].sum())
print('Soma linha E: ', df_slicing.loc['E'].sum())

# Somando as colunas
print('Soma coluna X: ', df_slicing['X'].sum())
print('Soma coluna Y: ', df_slicing['Y'].sum())


