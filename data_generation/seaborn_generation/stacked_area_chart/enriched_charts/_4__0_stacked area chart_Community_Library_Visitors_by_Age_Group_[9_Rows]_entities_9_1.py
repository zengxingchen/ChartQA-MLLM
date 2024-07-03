
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [i for i in range(2000, 2021)],
    'Science': [250 + i*15 for i in range(21)],
    'Research': [400 + i*20 for i in range(21)],
    'Innovation': [300 + i*15 for i in range(21)],
    'Education': [200 + i*15 for i in range(21)],
    'Publications': [100 + i*10 for i in range(21)],
}
df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Sector', value_name='Contribution')

df_melted['Cumulative'] = df_melted.groupby('Year')['Contribution'].cumsum()

plt.figure(figsize=(14, 8))
colors = ["#3498DB", "#E74C3C", "#2ECC71", "#9B59B6", "#F1C40F"]

for i, sector in enumerate(df_melted['Sector'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Sector'] == sector]['Cumulative'], color=colors[i], label=sector)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Sector'] == df_melted['Sector'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Sector'] == sector]['Cumulative'], 
                         color=colors[i], label=sector)

last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
science_last_value = last_year_data[last_year_data['Sector'] == 'Science']['Cumulative'].values[0]
plt.text(df['Year'].max(), science_last_value - 200, "Science", verticalalignment='center', horizontalalignment='center', color="white", fontsize=10)

plt.title("Contributions to Science and Research Over Time")
plt.xlabel("Year")
plt.ylabel("Contribution Index")
plt.legend(loc='upper left')
sns.despine()
plt.show()