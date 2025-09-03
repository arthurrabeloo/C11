aluno = {}

# lendo as entradas
aluno["nome"] = input("Digite o nome do aluno: ")
aluno["media"] = float(input("Digite a média do aluno: "))

# verificando a situação
if aluno["media"] >= 50:
    aluno["situacao"] = "AP"  # Aprovado
else:
    aluno["situacao"] = "RP"  # Reprovado

# mostrando o dicionário completo
print("Dados do aluno:")
print(aluno)
