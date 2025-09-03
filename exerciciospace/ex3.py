import numpy as np

ds = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

ds_location = ds[1:, 2]
quantidadeEUA = np.sum(np.char.find(ds_location, "USA") >= 0) # usando uma soma para somar sempre que encontra USA na frase
print(quantidadeEUA)