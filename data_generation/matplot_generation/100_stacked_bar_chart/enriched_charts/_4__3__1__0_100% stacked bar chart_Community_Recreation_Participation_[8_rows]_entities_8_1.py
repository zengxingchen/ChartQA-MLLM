
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Ethics', 'Aesthetics', 'Logic', 'Metaphysics', 'Epistemology']
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
data = np.array([
    [25, 30, 35, 40, 45],
    [20, 25, 30, 35, 40],
    [30, 25, 20, 25, 30],
    [15, 10, 15, 20, 25],
    [10, 10, 10, 10, 10]
])

# Normalize data to 100%
data_percentage = data / data.sum(axis=0) * 100

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.5
x = np.arange(len(years))

bottoms = np.zeros(len(years))

colors = ['#FF6347', '#FFD700', '#8A2BE2', '#5F9EA0', '#D2691E']

for i in range(len(categories)):
    ax.bar(x, data_percentage[i], bottom=bottoms, width=bar_width, color=colors[i], label=categories[i])
    bottoms += data_percentage[i]

ax.set_ylabel('Percentage')
ax.set_title('Distribution of Philosophy Topics Over 5 Years')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()