
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Astronomy & Space Exploration', 'Philosophy & Ethics', 'Culture & Society']
subcategories = ['Exoplanets', 'Asteroids', 'Black Holes', 'Galaxies', 'Stars', 'Morality', 'Existentialism', 'Logic', 'Epistemology', 'Ethics', 'Globalization', 'Traditions', 'Languages', 'Religion', 'Media']
values1 = [10, 15, 20, 10, 25, 30, 20, 25, 15, 35, 20, 25, 30, 15, 20]
values2 = [25, 20, 30, 35, 25, 20, 40, 35, 45, 25, 30, 35, 25, 20, 35]
values3 = [65, 65, 50, 55, 50, 50, 40, 40, 40, 40, 50, 40, 45, 65, 45]

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5']

# Bar width
barWidth = 0.35

# Creating the figure
fig, ax = plt.subplots(figsize=(12, 10))

# Stacked bar chart
bars1 = np.add(values1, values2).tolist()
bars2 = np.add(bars1, values3).tolist()

ax.bar(subcategories, values1, color=colors, edgecolor='grey', width=barWidth)
ax.bar(subcategories, values2, bottom=values1, color=colors, edgecolor='grey', width=barWidth)
ax.bar(subcategories, values3, bottom=bars1, color=colors, edgecolor='grey', width=barWidth)

# Title and labels
plt.title('Interests in Various Fields of Study', pad=20)
plt.ylabel('Percentage')
plt.xlabel('Fields of Study')
plt.legend(categories, loc='upper right', bbox_to_anchor=(1.15, 1))

# Rotate x labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()