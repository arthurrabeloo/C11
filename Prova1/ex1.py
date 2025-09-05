import numpy as np

ds = np.loadtxt('shopping_trends.csv', delimiter=',', dtype=str, encoding='utf-8')

ds_gender = ds[1:, 2] # pegando a coluna do gênero
mask_male = ds_gender == 'Male' # mascara para somente homens

ds_idade = ds[1:, 1][mask_male].astype(float) # pegando a idade dos homens e transformando em float
print('Média de idade dos homens: ', round(ds_idade.mean(), 2)) # fazendo a media de idade dos homens

