
distancia = float(input("Digite a distância da viagem em Km: "))

if distancia <= 200:
    valor_viagem = distancia * 0.50
else:
    valor_viagem = distancia * 0.45

print('O preço da viagem é de: ' + str(valor_viagem))
