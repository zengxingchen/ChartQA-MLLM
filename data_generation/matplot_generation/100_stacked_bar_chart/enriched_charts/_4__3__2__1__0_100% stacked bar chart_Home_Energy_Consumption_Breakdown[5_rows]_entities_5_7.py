
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Region': ['North', 'South', 'East', 'West', 'Central'],
    'Air Pollution': [22, 20, 25, 15, 18],
    'Water Pollution': [18, 22, 20, 25, 20],
    'Deforestation': [15, 20, 18, 22, 25],
    'Climate Change': [30, 25, 22, 20, 17],
    'Recycling': [15, 13, 15, 18, 20]
}

regions = data['Region']
categories = ['Air Pollution', 'Water Pollution', 'Deforestation', 'Climate Change', 'Recycling']

data_values = np.array([data[cat] for cat in categories])
data_cumsum = data_values.cumsum(axis=0)

fig, ax = plt.subplots(figsize=(8, 10))

category_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    heights = data_values[i]
    starts = data_cumsum[i] - heights
    ax.bar(regions, heights, bottom=starts, width=0.8, label=colname, color=color)

ax.set_ylabel('Percentage')
ax.set_title('Regional Distribution of Environmental Concerns')
ax.legend(ncol=1, bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')

plt.show()