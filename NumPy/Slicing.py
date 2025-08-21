import numpy as np
#slicing(fatiamento)

# criando um numpy array de duas dimensões
mtz = np.arange(1,10,1).reshape(3,3) # de 1 a 9 pulando de 1 em 1 (reshape serve pra montar a matriz, nesse caso 3 por 3)
print(mtz)

# extraindo apenas uma linha(terceira linha)
print(mtz[2]) #se passar somente 1 argumento dentro do colchetes, extrai somente a linha defininida (começa em 0)

# extraindo apenas uma coluna(segunda e terceira coluna)
print(mtz[:,1:]) # 2 pontos pra pegar todas as linhas virgula o numero da coluna e o dois pontos na frente do 1 pra pegar da coluna 2 pra frente
