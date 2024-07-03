
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [i for i in range(2000, 2021)],
    'DigitalTechnology': [300 + i*40 for i in range(21)],
    'Automation': [250 + i*30 for i in range(21)],
    'ResearchAndDevelopment': [500 + i*20 for i in range(21)],
    'Infrastructure': [400 + i*30 for i in range(21)],
    'MarketExpansion': [600 + i*30 for i in range(21)],
}
df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Sector', value_name='Expenditure')

df_melted['Cumulative'] = df_melted.groupby('Year')['Expenditure'].cumsum()

plt.figure(figsize=(20, 14))
colors = ["#1F77B4", "#FF7F0E", "#2CA02C", "#D62728", "#9467BD"]

for i, sector in enumerate(df_melted['Sector'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Sector'] == sector]['Cumulative'], color=colors[i], label=sector)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Sector'] == df_melted['Sector'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Sector'] == sector]['Cumulative'], 
                         color=colors[i], label=sector)

last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
digital_technology_last_value = last_year_data[last_year_data['Sector'] == 'DigitalTechnology']['Cumulative'].values[0]
plt.text(df['Year'].max(), digital_technology_last_value - 400, "Digital Technology", verticalalignment='center', horizontalalignment='center', color="white", fontsize=12)

plt.title("Investment in Business & Entrepreneurship Over Time", fontsize=20, pad=40)
plt.xlabel("Year", fontsize=16)
plt.ylabel("Investment Index", fontsize=16)
plt.legend(loc='upper left')
sns.despine()
plt.show()