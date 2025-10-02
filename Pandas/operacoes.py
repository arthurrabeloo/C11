import pandas as pd

#criando os dicionarios com indices diferentes para testar as operações indice a indice
dic = {'a': 10,'b': 20,'c': 30}
dic2 = {'a': 10,'b': 20,'d': 40}

#criando as series
series = pd.Series(dic)
series2 = pd.Series(dic2)

#operações com series
print(series + series2)
print(series - series2) # esse formato de operaçao so funciona quando todos os indices sao iguais

print(series.add(series2, fill_value=0)) # fazendo soma elemento a elemento com valor padrao
print(series.sub(series2, fill_value=0)) # fazendo subtracao elemento a elemento com valor padrao
# fill value seta os valores dos indices que cada series nao tem como 0, para operação funcionar
