import numpy as np

matriz = np.arange(12).reshape(3, 4)
print("Matriz:\n", matriz)

linhas, colunas = matriz.shape
print("Linhas:", linhas, "/ Colunas:", colunas)

total = linhas * colunas
print("Total de elementos:", total)

if total % 2 == 0:
    print("PAR")
else:
    print("ÍMPAR")
