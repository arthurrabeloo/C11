import pandas as pd
import matplotlib.pyplot as plt

df_space = pd.read_csv('space.csv', sep=';')

# limpeza e filtragem
df_space.columns = df_space.columns.str.strip()
df_space['Status Mission'] = df_space['Status Mission'].str.strip()
df_space['Company Name'] = df_space['Company Name'].str.strip()

df_success = df_space[df_space['Status Mission'] == 'Success']

success_counts = df_success['Company Name'].value_counts()
top_5_companies = success_counts.head(5)

plt.style.use('seaborn-v0_8-whitegrid')

plt.figure(figsize=(10, 6))
bars = plt.bar(top_5_companies.index, top_5_companies.values, color='teal')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center', va='bottom', fontsize=10)

plt.title('Top 5 Empresas com Mais Lançamentos Espaciais de Sucesso', fontsize=14, fontweight='bold')
plt.xlabel('Empresa', fontsize=12)
plt.ylabel('Contagem de Lançamentos de Sucesso', fontsize=12)
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()