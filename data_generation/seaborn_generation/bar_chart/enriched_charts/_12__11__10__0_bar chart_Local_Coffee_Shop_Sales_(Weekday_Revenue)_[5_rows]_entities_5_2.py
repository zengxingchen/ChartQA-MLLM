
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'City': ['New York', 'Los Angeles', 'Tokyo', 'London', 'Paris', 'Beijing', 'Sydney', 'Cape Town', 'Mumbai', 'Mexico City'],
    'Total_Tourists_2018': [55000000, 30000000, 15000000, 42000000, 38000000, 20000000, 25000000, 12000000, 6000000, 18000000],
    'Total_Tourists_2019': [56000000, 31000000, 16000000, 43000000, 39000000, 21000000, 26000000, 13000000, 7000000, 19000000],
    'Total_Tourists_2020': [57000000, 32000000, 17000000, 44000000, 40000000, 22000000, 27000000, 14000000, 8000000, 20000000]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars=['City'], var_name='Year', value_name='Total_Tourists')

plt.figure(figsize=(10, 12))

ax = sns.barplot(
    data=df_melted,
    x='City',
    y='Total_Tourists',
    hue='Year',
    palette=['#ff9999', '#66b3ff', '#99ff99'],
    dodge=True
)

ax.bar_label(ax.containers[0], padding=3)
plt.ylabel('Total Tourists')
plt.xlabel('City')
plt.title('Annual Tourist Arrivals in Major Cities')
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()