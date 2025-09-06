import pandas as pd

dic = {'Java' : 16.25, 'C' : 16.04, 'Python' : 9.85}
dic2 = {'C' : 16.21, 'Python' : 12.12, 'Java' : 11.68} # criando os dicionarios para ser usados como seriers

#criando as series
series1 = pd.Series(dic)
series2 = pd.Series(dic2)

print(series1.sum()) # fazendo a soma da series1 completa
print(series2.sum()) # fazendo a soma da series2 completa