
times = ["Real", "Barça", "Atletico de Madrid", "PSG", "City"]

# a) 3 primeiros
print("3 primeiros colocados:", times[:3])

# b) ultimos 2
print("Últimos 2 colocados:", times[-2:])

# c) em ordem alfabetico
print("Times em ordem alfabética:", sorted(times))

# d) Posição do Barcelona
posicao_barca = times.index("Barça") + 1
print(f"O Barcelona está na {posicao_barca}ª posição")
