# condicionais no numpy array
import numpy as np

mtz = np.arange(1,10,1).reshape(3,3)
print(mtz>5) # tudo que voce consegue fazer dentro de um if voce pode fazer no print
print(mtz[mtz > 5]) # mostrando os valores que são maiores que 5(colocando dentro dos colchetes mostra os valores)
print(mtz[mtz % 2 == 0]) #mostrando os valores  pares da matriz
