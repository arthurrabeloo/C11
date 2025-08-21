import numpy as np
# FUNDOES PARA ESTRUTURAR NUMPY ARRAYS
# Array 1D(1 dimensao) de 1s

arr = np.ones(10) # array de somente 1 com 10 numeros 1s
print(arr)

# Array 2D(duas dimensoes) de 0s com RESHAPE(reformatar)
mtz = np.zeros(10).reshape(5,2) # matriz de array de somente 0 com 10 numeros 0s
mtz2 = np.zeros([2,2]) #forma direta sem usar o reshape
print(mtz)
print(mtz2)

# ARANGE
arr = np.arange(10, 101, 10) # valores de 10 ate 101(ignora o 101, mas nao ignora o 10), pulando de 10 em 10
print(arr)
#menor valor
print(arr.min())
#maior valor
print(arr.max())
#media
print(arr.mean())
# indice de onde se encontra o maior valor
print(arr.argmax())
# indice de onde se encontra o menor valor
print(arr.argmin())
