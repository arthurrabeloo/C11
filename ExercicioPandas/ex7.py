import pandas as pd
import numpy as np

np.random.seed(10) # colocando as semente para se iniciar em 10
df = pd.DataFrame(
    index=['A','B','C','D','E'],
    columns = ['W','X','Y','Z'],
    data = np.random.randint(1, 50, [5, 4])
    ) # criando o dataframe
print(df)
print(df.iloc[3].mean()) # fazendo a media da linha D
print(df.loc['E'].sum()) # somando todos os elementos da linha E