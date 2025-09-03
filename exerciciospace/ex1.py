import numpy as np

ds = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

ds_status = ds[1:, 7]
sucessos = np.sum(ds_status == "Success")
statusqtd = len(ds_status) # vendo a quantidade de status que temos
porcentagem = ((sucessos / statusqtd) * 100) #dividindo o sucesso pela quantidade e multiplicando por 100
print(porcentagem)
