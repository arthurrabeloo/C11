import numpy as np

ds = np.loadtxt('shopping_trends.csv', delimiter=',', dtype=str, encoding='utf-8')

ds_amount = ds[1:, 5].astype(int) # pegando a coluna dos valores gastos e ja transformando em int
media = ds_amount.mean() # fazendo a media dos gastos
qtd_clientes = np.sum(ds_amount > media) # fazendo uma soma da quantidade de clientes que compraram acima da media

print('Média de gastos: ', round(media, 2)) # mostrando a media de gastos
print('Clientes que gastaram acima da média: ', qtd_clientes) # mostrando a quantidade de clientes que compraram acima da media