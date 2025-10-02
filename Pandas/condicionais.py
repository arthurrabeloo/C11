import pandas as pd

dic = {'a': 10,'b': 20,'c': 30}
dic2 = {'a': 10,'b': 20,'d': 40}

series = pd.Series(dic)
series2 = pd.Series(dic2)

print(series <= 20) #dessa forma ele so mostra a mascara de ture e false
print(series[series <= 20]) # dessa forma ele mostra apenas os elementos que atendem a condicao