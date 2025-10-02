import numpy as np

ds = np.loadtxt('shopping_trends.csv', delimiter=',', dtype=str, encoding='utf-8')

ds_item = ds[1:, 3] # pegando a coluna de itens
item, qtd = np.unique(ds_item, return_counts=True) #item serve para pega qual item
# qtd serve para pegar a quantidade que esses itens aparece
idx_menosvendido = qtd.argmin() #index(indice) do item menos vendido
print('Item menos vendido:', item[idx_menosvendido]) # imprimindo qual o item menos vendido

print('Porcentagem de vendas desse item: ', round((qtd[idx_menosvendido]/np.sum(qtd)) * 100, 2), '%')
#round para arredondamento para duas casas decimais
# pegando a quantidade de item menos vendido / pela soma total desses itens vezes 100