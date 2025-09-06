import pandas as pd

#criando os dicionarios para ser usados como series
dic = {'Java' : 16.25, 'C' : 16.04, 'Python' : 9.85}
dic2 = {'C' : 16.21, 'Python' : 12.12, 'Java' : 11.68}

series1 = pd.Series(dic) # criando a series do primeiro ano
series2 = pd.Series(dic2) # criando a series do segundo ano

print(series1) # imprimindo o resultado da series1
print(series2) # imprimindo o resultado da series2