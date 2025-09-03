numero = int(input('Digite seu numero: '))
inicio_intervalo = int(input('Digite seu inicio do intervalo: '))
fim_intervalo = int(input('Digite seu fim do intervalo: '))

for i in range(inicio_intervalo, fim_intervalo + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
