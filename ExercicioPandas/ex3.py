import pandas as pd

dic = {'Java' : 16.25, 'C' : 16.04, 'Python' : 9.85}
dic2 = {'C' : 16.21, 'Python' : 12.12, 'Java' : 11.68}

series1 = pd.Series(dic)
series2 = pd.Series(dic2)

print(series2 - series1) # fazendo a diferença do primeiro pro segundo ano, para ver se houve crescimento ou declinio