# conjunto de smartphones da loja a
loja_a = {"iPhone 14", "Galaxy S23", "Xiaomi 13", "Motorola Edge 30"}

# conjunto de smartphones da loja b
loja_b = {"Galaxy S23", "Xiaomi 13", "Iphone 16", "iPhone 13"}

# modelos disponíveis no total
todos_modelos = loja_a.union(loja_b)
print("Modelos disponíveis no total:", todos_modelos)

# modelos disponíveis em ambas as lojas
modelos_iguais = loja_a.intersection(loja_b)
print("Modelos disponíveis nas duas lojas:", modelos_iguais)
