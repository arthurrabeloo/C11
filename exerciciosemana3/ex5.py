import numpy as np

np.random.seed(10)
matriz = np.random.randint(1, 51, size=(4,4))

media_linhas = np.mean(matriz, axis=1)
media_colunas = np.mean(matriz, axis=0)

print("\nMédias das linhas:", media_linhas)
print("Médias das colunas:", media_colunas)

print("\nMaior média das linhas:", np.max(media_linhas))
print("Maior média das colunas:", np.max(media_colunas))

valores, contagens = np.unique(matriz, return_counts=True)
print("\nContagem de cada número:")
for v, c in zip(valores, contagens):
    print(f"Valor {v}: {c} vez(es)")

print("\nNúmeros que aparecem 2 vezes:", valores[contagens == 2])
