
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Country': ['USA', 'China', 'India', 'Germany', 'Brazil', 'UK', 'Japan', 'France', 'Australia', 'Canada'],
    '2000': [30, 15, 10, 20, 25, 18, 12, 23, 11, 19],
    '2005': [25, 20, 15, 15, 25, 22, 17, 28, 16, 24],
    '2010': [20, 25, 20, 10, 25, 28, 22, 18, 21, 29],
    '2015': [15, 30, 25, 5, 25, 32, 27, 13, 26, 34],
    '2020': [10, 35, 30, 10, 15, 40, 35, 8, 31, 39]
}

categories = list(data['Country'])
values = np.array([data[year] for year in ['2000', '2005', '2010', '2015', '2020']])

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.7
x = np.arange(len(categories))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']

bottom_values = np.zeros(len(categories))

for i, year in enumerate(['2000', '2005', '2010', '2015', '2020']):
    ax.bar(x, values[i], bar_width, bottom=bottom_values, color=colors[i], label=year)
    bottom_values += values[i]

ax.set_ylabel('Percentage')
ax.set_title('Trends in Tech Adoption by Country (2000-2020)', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
ax.set_ylim(0, 100)

plt.tight_layout()
plt.show()