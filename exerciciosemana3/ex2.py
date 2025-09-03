import numpy as np

arr1 = np.arange(0, 52, 2)
arr2 = np.arange(100, 49, -2)

concatenado = np.concatenate((arr1, arr2))

ordenado = np.sort(concatenado)

print("Concatenado:", concatenado)
print("Ordenado:", ordenado)
