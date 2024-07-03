
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [i for i in range(2000, 2022)],
    'Real Estate': [300 + i*10 for i in range(22)],
    'Technology': [200 + i*20 for i in range(22)],
    'Healthcare': [400 + i*20 for i in range(22)],
    'Finance': [500 + i*20 for i in range(22)],
    'Energy': [150 + i*10 for i in range(22)],
}
df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Sector', value_name='Contribution')

df_melted['Cumulative'] = df_melted.groupby('Year')['Contribution'].cumsum()

plt.figure(figsize=(16, 10))
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

for i, sector in enumerate(df_melted['Sector'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Sector'] == sector]['Cumulative'], color=colors[i], label=sector)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Sector'] == df_melted['Sector'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Sector'] == sector]['Cumulative'], 
                         color=colors[i], label=sector)

last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
finance_last_value = last_year_data[last_year_data['Sector'] == 'Finance']['Cumulative'].values[0]
plt.text(df['Year'].max(), finance_last_value - 150, "Finance", verticalalignment='center', horizontalalignment='center', color="white", fontsize=10)

plt.title("Economic Sector Contributions Over Time")
plt.xlabel("Year")
plt.ylabel("Contribution Index")
plt.legend(loc='upper left')
sns.despine()
plt.show()