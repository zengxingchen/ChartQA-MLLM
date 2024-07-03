
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Country': ['USA', 'Canada', 'Germany', 'UK', 'Japan', 'South Korea', 'Australia', 'India', 'China', 'France', 'Brazil'],
    'Science': [30, 25, 20, 15, 35, 25, 20, 30, 25, 20, 15],
    'Technology': [35, 30, 25, 20, 25, 35, 30, 25, 30, 25, 25],
    'Engineering': [20, 25, 30, 35, 25, 20, 30, 25, 30, 30, 35],
    'Mathematics': [15, 20, 25, 30, 15, 20, 20, 20, 15, 25, 25]
}

categories = list(data.keys())[1:]
countries = data['Country']
values = np.array([data[category] for category in categories])

values_cum = values.cumsum(axis=0)
category_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

fig, ax = plt.subplots(figsize=(10, 6))

ax.invert_yaxis()
ax.set_xlim(0, np.sum(values, axis=0).max())
ax.set_xlabel('Percentage')
ax.set_ylabel('Country')
ax.set_title('Distribution of STEM Education Focus by Country', pad=20)

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = values[i]
    starts = values_cum[i] - widths
    ax.barh(countries, widths, left=starts, height=0.7, label=colname, color=color)

ax.legend(ncol=len(categories), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.show()