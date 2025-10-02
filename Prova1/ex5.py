import numpy as np

ds =  np.loadtxt('shopping_trends.csv', delimiter=',', dtype=str, encoding='utf-8')

ds_color = ds[1:, 8] # pegando a coluna das cores
ds_season = ds[1:, 9] # pegando a coluna das estações
mask_verao = ds_season == "Summer" # fazendo uma mascara para verao na coluna das estações
ds_color_verao = ds_color[mask_verao] # colocando a mascara de "Summer" na coluna das cores
cor, qtd = np.unique(ds_color_verao, return_counts=True) # pegando a cor e a quantidade que ela aparece no verao
cor_popular_verao = np.argmax(qtd) # pegando a cor que mais aparece no verao
print('A cor mais popular no verao:', cor[cor_popular_verao]) # imprimindo a cor mais popular do verao