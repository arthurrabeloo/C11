n = int(input("Quantas pessoas deseja cadastrar? "))
soma_idades = 0
mulheres_menos_20 = 0

for i in range(n):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    # soma de idades para média
    soma_idades += idade

    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

# calculo da média
media_idade = soma_idades / n

# resultados
print(f"\nMédia de idade do grupo: {media_idade:.2f}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")
