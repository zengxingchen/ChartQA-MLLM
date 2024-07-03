
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [i for i in range(2000, 2021)],
    'MentalHealth': [500 + i*20 for i in range(21)],
    'PhysicalHealth': [450 + i*15 for i in range(21)],
    'Healthcare': [600 + i*20 for i in range(21)],
    'Wellness': [300 + i*15 for i in range(21)],
    'Research': [200 + i*10 for i in range(21)],
}
df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Sector', value_name='Expenditure')

df_melted['Cumulative'] = df_melted.groupby('Year')['Expenditure'].cumsum()

plt.figure(figsize=(18, 12))
colors = ["#4CAF50", "#FF9800", "#2196F3", "#9C27B0", "#F44336"]

for i, sector in enumerate(df_melted['Sector'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Sector'] == sector]['Cumulative'], color=colors[i], label=sector)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Sector'] == df_melted['Sector'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Sector'] == sector]['Cumulative'], 
                         color=colors[i], label=sector)

last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
mental_health_last_value = last_year_data[last_year_data['Sector'] == 'MentalHealth']['Cumulative'].values[0]
plt.text(df['Year'].max(), mental_health_last_value - 200, "Mental Health", verticalalignment='center', horizontalalignment='center', color="white", fontsize=12)

plt.title("Expenditure on Health & Psychology Over Time", fontsize=16, pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Expenditure Index", fontsize=14)
plt.legend(loc='upper left')
sns.despine()
plt.show()