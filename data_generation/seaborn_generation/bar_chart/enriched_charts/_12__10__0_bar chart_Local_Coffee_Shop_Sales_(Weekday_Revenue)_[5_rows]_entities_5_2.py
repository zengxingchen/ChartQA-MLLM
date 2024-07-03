
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'City': ['New York', 'Los Angeles', 'Tokyo', 'London', 'Paris', 'Beijing', 'Sydney', 'Cape Town', 'Mumbai', 'Mexico City'] * 3,
    'Year': ['2019']*10 + ['2020']*10 + ['2021']*10,
    'TouristsArrivals': [50, 45, 60, 55, 53, 48, 42, 30, 28, 25, 40, 35, 50, 47, 45, 42, 35, 25, 23, 20, 60, 55, 70, 65, 63, 58, 50, 40, 38, 35]
}

df = pd.DataFrame(data)

# Seaborn plot
plt.figure(figsize=(10, 12))

# Horizontal bar chart with customized colors and bar width
ax = sns.barplot(
    data=df,
    y='City',
    x='TouristsArrivals',
    hue='Year',
    palette=['#1f77b4', '#ff7f0e', '#2ca02c'],
    dodge=True
)

ax.bar_label(ax.containers[0], padding=3)
ax.bar_label(ax.containers[1], padding=3)
ax.bar_label(ax.containers[2], padding=3)
plt.xlabel('Tourists Arrivals (Millions)')
plt.ylabel('City')
plt.title('Annual Tourists Arrivals by City', pad=20)
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()