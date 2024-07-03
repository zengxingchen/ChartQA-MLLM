
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Region': ['North', 'South', 'East', 'West', 'Central'],
    'Food': [20, 25, 30, 15, 10],
    'Transport': [25, 20, 10, 30, 15],
    'Entertainment': [30, 15, 25, 20, 30],
    'Utilities': [15, 25, 20, 25, 25],
    'Healthcare': [10, 15, 15, 10, 20]
}

regions = data['Region']
categories = ['Food', 'Transport', 'Entertainment', 'Utilities', 'Healthcare']

data_values = np.array([data[cat] for cat in categories])
data_cumsum = data_values.cumsum(axis=0)

fig, ax = plt.subplots(figsize=(10, 6))

category_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1']

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = data_values[i]
    starts = data_cumsum[i] - widths
    ax.barh(regions, widths, left=starts, height=0.8, label=colname, color=color)

ax.set_xlabel('Percentage')
ax.set_title('Regional Distribution of Expenses')
ax.legend(ncol=len(categories), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.show()