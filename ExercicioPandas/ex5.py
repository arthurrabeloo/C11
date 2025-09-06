import pandas as pd

dic = {'Java' : 16.25, 'C' : 16.04, 'Python' : 9.85}
dic2 = {'C' : 16.21, 'Python' : 12.12, 'Java' : 11.68}

series1 = pd.Series(dic)
series2 = pd.Series(dic2)
crescimento = series2 - series1 # pegando a diferença dos anos

series4 = series2 + (2*crescimento) # fazendo a projeção para daqui a 2 ano
mais_popular = series4.nlargest(1) # pegando qual seria a linguagem mais popular

#imprimindo os resultados
print('O 4 ano seria: ', series4)
print('a linguagem mais popular seria: ', mais_popular)