
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [i for i in range(2000, 2021)],
    'Vegetables': [550 + i * 20 for i in range(21)],
    'Fruits': [420 + i * 10 for i in range(21)],
    'Grains': [310 + i * 20 for i in range(21)],
    'Dairy': [200 + i * 20 for i in range(21)],
    'Meat': [120 + i * 10 for i in range(21)],
}
df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Category', value_name='Consumption')

df_melted['Cumulative'] = df_melted.groupby('Year')['Consumption'].cumsum()

plt.figure(figsize=(16, 10))
colors = ["#FF6347", "#8A2BE2", "#3CB371", "#FFD700", "#1E90FF"]

for i, category in enumerate(df_melted['Category'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Category'] == category]['Cumulative'], color=colors[i], label=category)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Category'] == df_melted['Category'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Category'] == category]['Cumulative'], 
                         color=colors[i], label=category)

last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
vegetables_last_value = last_year_data[last_year_data['Category'] == 'Vegetables']['Cumulative'].values[0]
plt.text(df['Year'].max(), vegetables_last_value - 300, "Vegetables", verticalalignment='center', horizontalalignment='center', color="black", fontsize=10)

plt.title("Food Consumption Over Time by Category", fontsize=18, pad=30)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Consumption Count", fontsize=14)
plt.legend(loc='upper left')
sns.despine()
plt.show()