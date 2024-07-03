
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Country': ['USA', 'China', 'India', 'Germany', 'Brazil'],
    '2000': [30, 15, 10, 20, 25],
    '2005': [25, 20, 15, 15, 25],
    '2010': [20, 25, 20, 10, 25],
    '2015': [15, 30, 25, 5, 25],
    '2020': [10, 35, 30, 10, 15]
}

categories = list(data['Country'])
values = np.array([data[year] for year in ['2000', '2005', '2010', '2015', '2020']])

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.85
x = np.arange(len(categories))

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

bottom_values = np.zeros(len(categories))

for i, year in enumerate(['2000', '2005', '2010', '2015', '2020']):
    ax.barh(x, values[i], bar_width, left=bottom_values, color=colors[i], label=year)
    bottom_values += values[i]

ax.set_xlabel('Percentage')
ax.set_title('Changes in Energy Consumption by Country (2000-2020)')
ax.set_yticks(x)
ax.set_yticklabels(categories)
ax.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
ax.set_xlim(0, 100)

plt.tight_layout()
plt.show()