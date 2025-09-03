# lista para armazenar as pessoas e pesos
pessoas = []

# inserindo os dados
for i in range(3):
    nome = input("Digite o nome da pessoa: ")
    peso = float(input("Digite o peso (em kg): "))
    pessoas.append((nome, peso))  # armazena como tupla

# usando a primeira pessoa da lista
mais_pesada = pessoas[0]
mais_leve = pessoas[0]

# procurando a mais pesada e a mais leve
for pessoa in pessoas:
    if pessoa[1] > mais_pesada[1]:
        mais_pesada = pessoa
    if pessoa[1] < mais_leve[1]:
        mais_leve = pessoa

# resultado
print(f"Pessoa mais pesada: {mais_pesada[0]} ({mais_pesada[1]} kg)")
print(f"Pessoa mais leve: {mais_leve[0]} ({mais_leve[1]} kg)")

#professor nao sei se esta certo da forma que fiz, mas foi o que consegui