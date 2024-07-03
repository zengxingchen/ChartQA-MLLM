
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Country': ['USA', 'China', 'India', 'Germany', 'Brazil', 'UK', 'Canada', 'Japan', 'Australia', 'Russia', 'France', 'Italy'],
    '2020': [5, 8, 7, 4, 6, 5, 3, 4, 2, 7, 6, 5],
    '2021': [10, 12, 13, 8, 11, 10, 8, 9, 6, 12, 11, 9],
    '2022': [15, 18, 19, 13, 17, 15, 14, 19, 11, 18, 16, 14],
    '2023': [20, 25, 25, 20, 22, 28, 25, 23, 21, 27, 26, 22]
}

categories = list(data.keys())[1:]
countries = data['Country']
values = np.array([data[cat] for cat in categories])

fig, ax = plt.subplots(figsize=(10, 12))

width = 0.7
indices = np.arange(len(countries))

bottom = np.zeros(len(countries))
colors = ['#FF7F50', '#87CEEB', '#3CB371', '#DA70D6']

for i, category in enumerate(categories):
    ax.bar(indices, values[i], bottom=bottom, width=width, label=category, color=colors[i % len(colors)])
    bottom += values[i]

ax.set_xticks(indices)
ax.set_xticklabels(countries, rotation=45, ha='right')
ax.set_ylabel('Percentage (%)')
ax.set_title('Percentage Distribution of Internet Usage (2020-2023)', pad=20)
ax.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()