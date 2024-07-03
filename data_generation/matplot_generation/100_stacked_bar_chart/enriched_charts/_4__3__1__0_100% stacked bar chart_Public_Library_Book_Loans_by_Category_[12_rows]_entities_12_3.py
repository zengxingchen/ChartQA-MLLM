import matplotlib.pyplot as plt
import numpy as np

data = {
    'Country': ['USA', 'Canada', 'Germany', 'UK', 'Japan', 'South Korea', 'Australia', 'India', 'China', 'France', 'Brazil', 'Mexico', 'Spain', 'Italy', 'Russia'],
    'Food': [25, 20, 30, 15, 35, 25, 20, 25, 20, 30, 25, 20, 25, 30, 25],
    'Transport': [20, 25, 20, 30, 25, 30, 35, 20, 25, 20, 25, 30, 25, 20, 30],
    'Health': [30, 35, 25, 25, 20, 20, 30, 30, 25, 30, 25, 25, 30, 25, 20],
    'Entertainment': [25, 20, 25, 30, 20, 25, 15, 25, 30, 20, 25, 25, 20, 25, 25]
}

categories = list(data.keys())[1:]
countries = data['Country']
values = np.array([data[category] for category in categories])

values_cum = values.cumsum(axis=0)
category_colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00']

fig, ax = plt.subplots(figsize=(12, 8))

ax.set_ylim(0, np.sum(values, axis=0).max())
ax.set_ylabel('Percentage')
ax.set_xlabel('Country')
ax.set_title('Resource Allocation by Country', pad=20)

bar_width = 0.8

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    heights = values[i]
    starts = values_cum[i] - heights
    ax.bar(countries, heights, bottom=starts, width=bar_width, label=colname, color=color)

ax.legend(ncol=len(categories), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.xticks(rotation=45, ha='right')
plt.show()