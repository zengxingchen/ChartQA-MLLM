
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [i for i in range(2000, 2021)],
    'Flights': [250 + i*15 for i in range(21)],
    'Hotels': [400 + i*20 for i in range(21)],
    'Tours': [300 + i*15 for i in range(21)],
    'Transport': [200 + i*15 for i in range(21)],
    'Food': [100 + i*10 for i in range(21)],
}
df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Sector', value_name='Expenditure')

df_melted['Cumulative'] = df_melted.groupby('Year')['Expenditure'].cumsum()

plt.figure(figsize=(16, 10))
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#FFC300"]

for i, sector in enumerate(df_melted['Sector'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Sector'] == sector]['Cumulative'], color=colors[i], label=sector)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Sector'] == df_melted['Sector'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Sector'] == sector]['Cumulative'], 
                         color=colors[i], label=sector)

last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
flights_last_value = last_year_data[last_year_data['Sector'] == 'Flights']['Cumulative'].values[0]
plt.text(df['Year'].max(), flights_last_value - 200, "Flights", verticalalignment='center', horizontalalignment='center', color="white", fontsize=12)

plt.title("Expenditure on Travel & Adventure Over Time", fontsize=16, pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Expenditure Index", fontsize=14)
plt.legend(loc='upper right')
sns.despine()
plt.show()