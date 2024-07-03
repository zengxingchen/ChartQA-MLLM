
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Reading', 'Writing', 'Discussion', 'Presentation'],
    '2010': [5, 3, 2, 1],
    '2011': [6, 4, 2, 2],
    '2012': [7, 4, 3, 1],
    '2013': [6, 5, 3, 1],
    '2014': [8, 6, 4, 2],
    '2015': [7, 5, 3, 1],
    '2016': [8, 6, 4, 2],
    '2017': [9, 5, 4, 1],
    '2018': [7, 6, 4, 2],
    '2019': [8, 7, 5, 2],
    '2020': [9, 6, 4, 2]
}

categories = data['Category']
years = list(data.keys())[1:]

values = np.array([data[year] for year in years]).T

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.85
bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

bottoms = np.zeros(len(years))

for i, (category, color) in enumerate(zip(categories, bar_colors)):
    ax.bar(years, values[i], bar_width, bottom=bottoms, label=category, color=color)
    bottoms += values[i]

ax.set_xlabel('Years')
ax.set_ylabel('Percentage of Activities (%)')
ax.set_title('Trends in Student Engagement Activities (2010-2020)')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()