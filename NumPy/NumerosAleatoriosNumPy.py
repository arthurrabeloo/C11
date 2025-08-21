import numpy as np

#SEMENTE ALEATORIA
np.random.seed(10) # vai gerar os numeros aleatorios mas começando com o 10 sempre
arr = np.random.randint(1, 101, 10) #gera numeros aleatorios de 1(inclusivo) a 101(exclusivo) inteiros aletatorios
print(arr)