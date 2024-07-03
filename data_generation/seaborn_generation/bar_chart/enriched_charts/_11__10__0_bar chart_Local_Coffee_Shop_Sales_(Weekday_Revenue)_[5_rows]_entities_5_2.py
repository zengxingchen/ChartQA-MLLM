
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'City': ['New York', 'Los Angeles', 'Tokyo', 'London', 'Paris', 'Beijing', 'Sydney', 'Cape Town', 'Mumbai', 'Mexico City'],
    'Population_2018': [8500000, 4000000, 9200000, 8900000, 2150000, 21500000, 5200000, 4500000, 18400000, 9200000],
    'Population_2019': [8550000, 4050000, 9250000, 8950000, 2200000, 22000000, 5250000, 4550000, 18500000, 9250000],
    'Population_2020': [8600000, 4100000, 9300000, 9000000, 2250000, 22500000, 5300000, 4600000, 18600000, 9300000]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars=['City'], var_name='Year', value_name='Population')

plt.figure(figsize=(12, 8))

ax = sns.barplot(
    data=df_melted,
    x='Population',
    y='City',
    hue='Year',
    palette=['#3498db', '#e74c3c', '#2ecc71'],
    dodge=True
)

ax.bar_label(ax.containers[0], padding=3)
plt.xlabel('Population')
plt.ylabel('City')
plt.title('Annual Population of Major Cities')
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()