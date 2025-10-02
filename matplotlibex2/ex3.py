import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_countries = pd.read_csv('paises (1).csv', sep=';')

df_countries.columns = df_countries.columns.str.strip()

col_gdp = 'GDP ($ per capita)'
col_infant_mortality = 'Infant mortality (per 1000 births)'

df_countries_scatter = df_countries[[col_gdp, col_infant_mortality]].copy()
df_countries_scatter.dropna(inplace=True)

gdp = df_countries_scatter[col_gdp]
mortality = df_countries_scatter[col_infant_mortality]

plt.style.use('seaborn-v0_8-whitegrid')

plt.figure(figsize=(10, 6))

plt.scatter(gdp, mortality, alpha=0.6, color='purple', s=50)

z = np.polyfit(gdp, mortality, 1) # Grau 1 para uma linha reta
p = np.poly1d(z)
corr = np.corrcoef(gdp, mortality)[0, 1]

plt.plot(gdp, p(gdp), "r--", label=f"Linha de Tendência (r={corr:.2f})")
plt.legend()

plt.title('Relação entre PIB per Capita e Mortalidade Infantil', fontsize=14, fontweight='bold')
plt.xlabel('PIB ($ per capita)', fontsize=12)
plt.ylabel('Mortalidade Infantil (por 1000 nascimentos)', fontsize=12)

plt.text(0.65, 0.9, f'Correlação (r): {corr:.2f} (Forte e Negativa)', transform=plt.gca().transAxes, fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

plt.tight_layout()
plt.show()