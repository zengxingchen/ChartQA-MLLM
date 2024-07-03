
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Recycling', 'Renewable Energy', 'Pollution Reduction', 'Wildlife Conservation', 'Climate Action']
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
data = np.array([
    [20, 25, 30, 35, 40],
    [15, 20, 25, 30, 35],
    [25, 20, 15, 20, 25],
    [10, 15, 20, 25, 30],
    [30, 20, 10, 15, 20]
])

# Normalize data to 100%
data_percentage = data / data.sum(axis=0) * 100

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.7
x = np.arange(len(years))

bottoms = np.zeros(len(years))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF']

for i in range(len(categories)):
    ax.barh(x, data_percentage[i], left=bottoms, height=bar_width, color=colors[i], label=categories[i])
    bottoms += data_percentage[i]

ax.set_xlabel('Percentage')
ax.set_title('Environmental Initiatives Over 5 Years')
ax.set_yticks(x)
ax.set_yticklabels(years)
ax.legend(loc='lower right', bbox_to_anchor=(1.05, 0))

plt.tight_layout()
plt.show()