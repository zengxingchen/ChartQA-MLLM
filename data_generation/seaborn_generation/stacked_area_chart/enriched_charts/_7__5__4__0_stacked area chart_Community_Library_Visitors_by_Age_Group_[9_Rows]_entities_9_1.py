
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [i for i in range(2000, 2021)],
    'Compositions': [300 + i*20 for i in range(21)],
    'Concerts': [450 + i*20 for i in range(21)],
    'Streaming': [250 + i*20 for i in range(21)],
    'Music Lessons': [150 + i*10 for i in range(21)],
    'Merchandise': [100 + i*10 for i in range(21)],
}
df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Sector', value_name='Expenditure')

df_melted['Cumulative'] = df_melted.groupby('Year')['Expenditure'].cumsum()

plt.figure(figsize=(14, 8))
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
concerts_last_value = last_year_data[last_year_data['Sector'] == 'Concerts']['Cumulative'].values[0]
plt.text(df['Year'].max(), concerts_last_value - 100, "Concerts", verticalalignment='center', horizontalalignment='center', color="white", fontsize=12)

plt.title("Music Industry Expenditure Over Time", fontsize=16, pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Expenditure Index", fontsize=14)
plt.legend(loc='upper left')
sns.despine()
plt.show()