
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Q1 2023': [20, 50, 30],
    'Q2 2023': [25, 45, 30],
    'Q3 2023': [30, 40, 30],
    'Q4 2023': [35, 35, 30],
    'Q1 2024': [40, 30, 30],
    'Q2 2024': [45, 25, 30],
    'Q3 2024': [50, 20, 30],
    'Q4 2024': [55, 15, 30]
}

categories = list(data.keys())
values = np.array(list(data.values()))
group_labels = ['Group A', 'Group B', 'Group C']
colors = ['#FF5733', '#33FF57', '#3357FF']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.7
bars = np.arange(len(categories))

bottoms = np.zeros(len(categories))

for idx, (group, color) in enumerate(zip(group_labels, colors)):
    ax.barh(bars, values[:, idx], bar_width, left=bottoms, label=group, color=color)
    bottoms += values[:, idx]

ax.set_xlabel('Percentage')
ax.set_title('Quarterly Performance of Groups (2023-2024)')
ax.set_yticks(bars)
ax.set_yticklabels(categories)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()