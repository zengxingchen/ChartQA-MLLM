
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'AI': [20, 25, 30, 35, 40],
    'Blockchain': [10, 15, 20, 25, 30],
    'IoT': [30, 25, 20, 15, 10],
    'Quantum Computing': [5, 10, 15, 20, 15],
    '5G': [35, 25, 15, 5, 5]
}

categories = ['AI', 'Blockchain', 'IoT', 'Quantum Computing', '5G']
years = data['Year']
values = np.array([data[cat] for cat in categories])

# Normalize data to 100%
values_percentage = values / values.sum(axis=0) * 100

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.5

bottoms = np.zeros(len(years))
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#4B0082']

for i, (category, color) in enumerate(zip(categories, colors)):
    ax.bar(years, values_percentage[i], bottom=bottoms, label=category, color=color, edgecolor='white', width=bar_width)
    bottoms += values_percentage[i]

ax.set_title('Adoption Rates of Future Technologies Over Years', pad=20)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_yticks(np.arange(0, 101, 10))
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Technologies")
ax.set_ylim(0, 100)

plt.tight_layout()
plt.show()