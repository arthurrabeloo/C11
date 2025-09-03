import numpy as np

# Carrega o dataset
ds = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Filtra empresa SpaceX
mask_spacex = ds[1:, 1] == "SpaceX"

# Pega os custos correspondentes e converte para float
ds_cost = ds[1:, 6].astype(float)

# Aplica a máscara e pega o máximo
max_cost = ds_cost[mask_spacex].max()

print(max_cost)