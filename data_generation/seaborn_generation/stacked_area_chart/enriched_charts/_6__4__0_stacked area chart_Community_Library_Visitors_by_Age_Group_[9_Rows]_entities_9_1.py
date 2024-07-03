
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [i for i in range(2000, 2021)],
    'Technology': [500 + i*20 for i in range(21)],
    'Healthcare': [600 + i*30 for i in range(21)],
    'Finance': [700 + i*10 for i in range(21)],
    'Energy': [800 + i*20 for i in range(21)],
    'Manufacturing': [900 + i*20 for i in range(21)],
}
df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Sector', value_name='Investment')

df_melted['Cumulative'] = df_melted.groupby('Year')['Investment'].cumsum()

plt.figure(figsize=(16, 9))
colors = ["#1ABC9C", "#E74C3C", "#3498DB", "#9B59B6", "#F39C12"]

for i, sector in enumerate(df_melted['Sector'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Sector'] == sector]['Cumulative'], color=colors[i], label=sector)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Sector'] == df_melted['Sector'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Sector'] == sector]['Cumulative'], 
                         color=colors[i], label=sector)

last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
technology_last_value = last_year_data[last_year_data['Sector'] == 'Technology']['Cumulative'].values[0]
plt.text(df['Year'].max(), technology_last_value - 200, "Technology", verticalalignment='center', horizontalalignment='center', color="white", fontsize=10)

plt.title("Investment in Various Sectors Over Time", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Investment Index")
plt.legend(loc='upper right')
sns.despine()
plt.show()