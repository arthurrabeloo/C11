import pandas as pd
#quando for criar uma series é necessário passar um indice e depois o valor
indices = ['a', 'b', 'c']
valores = [10, 20, 30]

series = pd.Series(index=indices, data = valores) # criamos duas listas para criar uma series
print(series)
print(type(series)) # usando o type para ver se a "ide" entendeu como series

dic = {'a': 10, 'b': 20, 'c': 30} # outra forma de criar uma series
series2 = pd.Series(dic) #criando como dicionarios
print(series2)
print(type(series2))
print(series['a']) # quando eu quero ver um valor dentro da "chave"(indice) a
