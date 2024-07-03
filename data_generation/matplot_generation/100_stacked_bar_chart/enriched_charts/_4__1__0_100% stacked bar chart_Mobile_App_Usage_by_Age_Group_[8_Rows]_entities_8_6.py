
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Protein', 'Fat', 'Carbohydrate', 'Vitamins']
data = np.array([
    [45, 15, 35, 5],
    [60, 25, 10, 5],
    [30, 20, 40, 10],
    [50, 30, 15, 5],
    [25, 35, 30, 10],
    [55, 10, 25, 10],
    [40, 20, 35, 5],
    [70, 15, 10, 5],
    [35, 30, 30, 5],
    [20, 40, 35, 5]
])

planets = ['Mars', 'Venus', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Mercury', 'Pluto', 'Ceres']

# Normalize data to 100%
data = data / data.sum(axis=1)[:, None] * 100

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']

# Plot
fig, ax = plt.subplots(figsize=(10, 15))

bar_width = 0.6
indices = np.arange(len(planets))

bottoms = np.zeros(len(planets))
for i, category in enumerate(categories):
    ax.bar(indices, data[:, i], bar_width, bottom=bottoms, color=colors[i], label=category)
    bottoms += data[:, i]

# Title and labels
ax.set_title('Nutritional Composition of Various Planets')
ax.set_ylabel('Percentage')
ax.set_xticks(indices)
ax.set_xticklabels(planets, rotation=45, ha='right')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()