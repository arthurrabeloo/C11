import numpy as np

ds = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

ds_company = ds[1:, 1]

empresas_unicas, quantidadedes = np.unique(ds_company, return_counts=True) # salvando as empresas e a quantidade

for empresas_unicas, quantidades in zip(empresas_unicas, quantidadedes): # fazendo um for e printando
    print(empresas_unicas, quantidades)