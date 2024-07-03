
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Year': [i for i in range(2000, 2021)],
    'Sports': [500 + i * 20 for i in range(21)],
    'Music': [400 + i * 10 for i in range(21)],
    'Travel': [300 + i * 20 for i in range(21)],
    'Education': [200 + i * 20 for i in range(21)],
    'Health': [100 + i * 10 for i in range(21)],
}
df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Category', value_name='Participation')

df_melted['Cumulative'] = df_melted.groupby('Year')['Participation'].cumsum()

plt.figure(figsize=(14, 8))
colors = ["#FFA07A", "#20B2AA", "#9370DB", "#FFD700", "#4682B4"]

for i, category in enumerate(df_melted['Category'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Category'] == category]['Cumulative'], color=colors[i], label=category)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Category'] == df_melted['Category'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Category'] == category]['Cumulative'], 
                         color=colors[i], label=category)

last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
sports_last_value = last_year_data[last_year_data['Category'] == 'Sports']['Cumulative'].values[0]
plt.text(df['Year'].max(), sports_last_value - 250, "Sports", verticalalignment='center', horizontalalignment='center', color="black", fontsize=10)

plt.title("Participation in Activities Over Time by Category", fontsize=16, pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Participation Count", fontsize=14)
plt.legend(loc='upper right')
sns.despine()
plt.show()