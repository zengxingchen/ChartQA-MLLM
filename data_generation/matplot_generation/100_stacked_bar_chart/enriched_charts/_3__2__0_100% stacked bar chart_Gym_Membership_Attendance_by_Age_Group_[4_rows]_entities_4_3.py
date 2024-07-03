import matplotlib.pyplot as plt
import numpy as np

data = {
    '2019': [35, 25, 20, 10, 10],
    '2020': [40, 20, 25, 5, 10],
    '2021': [45, 30, 15, 5, 5]
}

categories = ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meat']
years = list(data.keys())
values = np.array(list(data.values()))

values_percentage = values / values.sum(axis=0) * 100

bar_width = 0.5
fig, ax = plt.subplots(figsize=(10, 6))

bottom = np.zeros(len(years))

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666']

for i, category in enumerate(categories):
    ax.barh(years, values_percentage[i], bar_width, left=bottom, label=category, color=colors[i])
    bottom += values_percentage[i]

ax.set_xlabel('Percentage')
ax.set_title('Food Consumption Trends (2019-2021)')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()