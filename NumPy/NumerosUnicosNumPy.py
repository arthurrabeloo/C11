import numpy as np

arr = np.random.randint(1, 10, 10)
print(arr)
print(np.unique(arr, return_counts = True)) #mostrando apenas elementos unicos e ordenados
#return counts serve pra mostrar quantos vezes cada elemento(ordenado) se repete