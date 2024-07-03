
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Geothermal'],
    '2010': [4, 3, 2, 1, 1],
    '2011': [5, 4, 2, 2, 1],
    '2012': [6, 4, 3, 1, 1],
    '2013': [6, 5, 3, 1, 1],
    '2014': [7, 6, 4, 2, 1],
    '2015': [7, 5, 3, 1, 2],
    '2016': [8, 6, 4, 2, 2],
    '2017': [9, 5, 4, 1, 1],
    '2018': [7, 6, 4, 2, 2],
    '2019': [8, 7, 5, 2, 1],
    '2020': [9, 6, 4, 2, 1]
}

categories = data['Category']
years = list(data.keys())[1:]

values = np.array([data[year] for year in years]).T

fig, ax = plt.subplots(figsize=(12, 10))

bar_width = 0.75
bar_colors = ['#1e90ff', '#32cd32', '#ff6347', '#ffa500', '#8a2be2']

bottoms = np.zeros(len(years))

for i, (category, color) in enumerate(zip(categories, bar_colors)):
    ax.bar(years, values[i], bar_width, bottom=bottoms, label=category, color=color)
    bottoms += values[i]

ax.set_xlabel('Years')
ax.set_ylabel('Percentage of Renewable Energy Sources (%)')
ax.set_title('Trends in Renewable Energy Sources (2010-2020)', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()