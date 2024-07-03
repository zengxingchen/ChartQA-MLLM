import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active']
men = [20, 30, 35, 15]
women = [15, 35, 30, 20]
children = [10, 20, 45, 25]
seniors = [25, 30, 25, 20]

# Stacking the data
data = np.array([men, women, children, seniors])
data_cum = data.cumsum(axis=1)

# Creating the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plotting
category_colors = colors[:len(categories)]
bar_width = 0.5

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    ax.barh(categories, widths, left=starts, height=bar_width, label=colname, color=color)

# Adding labels and title
ax.set_title('Daily Physical Activity Levels by Demographic Group', fontsize=16, pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Demographic Groups')
ax.legend(ncol=len(categories), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

# Adjusting layout
plt.tight_layout()
plt.show()