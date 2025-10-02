import numpy as np

ds = np.loadtxt('shopping_trends.csv', delimiter=',', dtype=str, encoding='utf-8')

ds_discount = ds[1:, 13] # coluna dos descontos
itens = ds[1:, 3] # coluna de itens
qtd_itens = len(itens) # pegando a quantidade de itens
discount_yes = sum((np.char.find(ds_discount, 'Yes') >= 0))
# fazend uma soma de somente quando for encontrado 'Yes' na coluna desconto
print('Porcentagem de vendas com desconto: ', (discount_yes/qtd_itens) * 100, '%') # imprimindo
# dividindo a quantidade de itens que foram aplicado desconto pela quantidade total de itens