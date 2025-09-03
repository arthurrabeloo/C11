import numpy as np
import random

campo = np.zeros((2, 2), dtype=int)
linha = random.randint(0, 1)
coluna = random.randint(0, 1)
campo[linha, coluna] = 1


tentativas = 3
acertou = False

for i in range(tentativas):
    print(f"\nTentativa {i+1} de {tentativas}")
    l = int(input("Escolha a linha (0 ou 1): ")) #linhas
    c = int(input("Escolha a coluna (0 ou 1): ")) #colunas

    if campo[l, c] == 1:
        print("Perdeu")
        acertou = True
        break
    else:
        print("vazio")

if not acertou:
    print("Parabéns você ganhou")

# professor só consegui fazer assim, não sei se está certo
