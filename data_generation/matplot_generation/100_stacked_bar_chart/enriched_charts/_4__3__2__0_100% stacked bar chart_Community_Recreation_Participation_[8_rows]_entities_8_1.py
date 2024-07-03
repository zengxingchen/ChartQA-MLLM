
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Q1 2023': [25, 45, 30],
    'Q2 2023': [30, 40, 30],
    'Q3 2023': [35, 35, 30],
    'Q4 2023': [40, 30, 30],
    'Q1 2024': [45, 25, 30],
    'Q2 2024': [50, 20, 30],
    'Q3 2024': [55, 15, 30],
    'Q4 2024': [60, 10, 30],
    'Q1 2025': [65, 5, 30],
    'Q2 2025': [70, 0, 30]
}

categories = list(data.keys())
values = np.array(list(data.values()))
group_labels = ['Recycling', 'Renewable Energy', 'Carbon Emissions']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

fig, ax = plt.subplots(figsize=(10, 14))

bar_width = 0.5
bars = np.arange(len(categories))

bottoms = np.zeros(len(categories))

for idx, (group, color) in enumerate(zip(group_labels, colors)):
    ax.bar(bars, values[:, idx], bar_width, bottom=bottoms, label=group, color=color)
    bottoms += values[:, idx]

ax.set_ylabel('Percentage')
ax.set_title('Environmental Impact Metrics (2023-2025)')
ax.set_xticks(bars)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()