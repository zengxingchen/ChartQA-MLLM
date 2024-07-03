import matplotlib.pyplot as plt
import numpy as np

data = {
    'Country': ['USA', 'China', 'India', 'Germany', 'Brazil', 'UK', 'Canada', 'Japan', 'Australia', 'Russia', 'France', 'Italy'],
    '2020': [15, 20, 10, 5, 8, 12, 7, 9, 6, 13, 11, 10],
    '2021': [20, 25, 15, 10, 12, 18, 13, 14, 11, 18, 16, 14],
    '2022': [25, 30, 20, 15, 18, 22, 19, 19, 17, 23, 21, 18],
    '2023': [30, 25, 25, 20, 22, 28, 25, 23, 21, 27, 26, 22]
}

categories = list(data.keys())[1:]
countries = data['Country']
values = np.array([data[cat] for cat in categories])

fig, ax = plt.subplots(figsize=(12, 8))

width = 0.6
indices = np.arange(len(countries))

bottom = np.zeros(len(countries))
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#1E90FF']

for i, category in enumerate(categories):
    ax.barh(indices, values[i], left=bottom, height=width, label=category, color=colors[i % len(colors)])
    bottom += values[i]

ax.set_yticks(indices)
ax.set_yticklabels(countries)
ax.set_xlabel('Percentage (%)')
ax.set_title('Percentage Distribution of Population Growth (2020-2023)')
ax.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()