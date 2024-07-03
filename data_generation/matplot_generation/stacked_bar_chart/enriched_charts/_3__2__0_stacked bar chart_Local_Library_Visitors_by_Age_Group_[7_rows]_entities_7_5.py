
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Vegetables': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240],
    'Fruits': [100, 105, 110, 120, 130, 135, 140, 150, 160, 170],
    'Dairy': [80, 85, 90, 95, 100, 110, 115, 120, 125, 130],
    'Grains': [90, 95, 100, 105, 110, 120, 125, 130, 135, 140]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 10))

bars1 = ax.barh(df['Year'], df['Vegetables'], color='#7DCEA0', edgecolor='grey', height=0.7, label='Vegetables')
bars2 = ax.barh(df['Year'], df['Fruits'], left=df['Vegetables'], color='#F5B041', edgecolor='grey', height=0.7, label='Fruits')
bars3 = ax.barh(df['Year'], df['Dairy'], left=df['Vegetables'] + df['Fruits'], color='#85C1E9', edgecolor='grey', height=0.7, label='Dairy')
bars4 = ax.barh(df['Year'], df['Grains'], left=df['Vegetables'] + df['Fruits'] + df['Dairy'], color='#F1948A', edgecolor='grey', height=0.7, label='Grains')

ax.set_xlabel('Consumption (kg)')
ax.set_title('Food Consumption Trends Over Years')
ax.legend(loc='upper right', bbox_to_anchor=(1, 1))

for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width}',
                    xy=(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='center')

plt.show()