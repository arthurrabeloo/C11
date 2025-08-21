from operator import concat

import numpy as np

arr1 = np.arange(1, 10, 1)
arr2 = np.arange(9, 0, -1)

print(arr1)
print(arr2)

# so funciona se os arrays tiver o mesmo numero de elementos(compatibilidade)
print(arr1 + arr2) # somando elemento indice a indice

#concatenar
print(np.concatenate([arr1, arr2]))