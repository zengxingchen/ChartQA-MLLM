
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025'],
    'Value_A': [25, 20, 30, 25, 22, 26, 24, 28, 27, 23, 25, 25],
    'Value_B': [30, 25, 20, 25, 28, 22, 26, 24, 23, 27, 25, 25],
    'Value_C': [25, 30, 25, 20, 26, 24, 28, 22, 25, 25, 27, 23],
    'Value_D': [20, 25, 25, 30, 24, 28, 22, 26, 25, 25, 23, 27]
}

categories = data['Category']
values = np.array([data['Value_A'], data['Value_B'], data['Value_C'], data['Value_D']])

values_cum = values.cumsum(axis=0)

category_labels = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(10, 15))

bar_width = 0.4

colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6']

for i, (color, value) in enumerate(zip(colors, values)):
    starts = values_cum[i] - value
    ax.bar(category_labels, value, bottom=starts, width=bar_width, color=color)

ax.set_xticks(category_labels)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.set_ylabel('Percentage')
ax.set_title('Quarterly Distribution of Values by Category (2023-2025)')
ax.legend(['Value A', 'Value B', 'Value C', 'Value D'], bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()