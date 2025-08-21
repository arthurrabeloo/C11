import numpy as np

mtz = np.array([50, 10, 100, 60, 25, 100, 75, 80, 100]).reshape(3, 3)
print(mtz)

print(mtz.sum(axis = 1)) # usando pra somar as linhas da matriz
print(mtz.sum(axis = 0)) # usando pra somar as colunas
print(mtz.sum(axis = 0)[2]) # usando pra somar somente a 3 coluna