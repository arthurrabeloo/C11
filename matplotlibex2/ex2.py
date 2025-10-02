import pandas as pd
import matplotlib.pyplot as plt

df_countries = pd.read_csv('paises.csv', sep=';')

# Limpar o nome das colunas
df_countries.columns = df_countries.columns.str.strip()
column_name = 'Pop. Density (per sq. mi.)'

data_for_hist = df_countries[column_name].dropna()

plt.style.use('seaborn-v0_8-whitegrid')

plt.figure(figsize=(10, 6))

plt.hist(data_for_hist, bins=30, color='darkorange', edgecolor='black', alpha=0.7)

plt.title('Histograma da Densidade Populacional (por milha quadrada)', fontsize=14, fontweight='bold')
plt.xlabel('Densidade Populacional (Pop. Density (per sq. mi.))', fontsize=12)
plt.ylabel('Frequência (Contagem de Países)', fontsize=12)
plt.grid(axis='y', alpha=0.5)

plt.tight_layout()
plt.show()