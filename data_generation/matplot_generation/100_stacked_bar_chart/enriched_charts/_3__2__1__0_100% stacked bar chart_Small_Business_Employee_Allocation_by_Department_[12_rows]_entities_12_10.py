
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10']
physical_health = [20, 15, 10, 25, 30, 35, 25, 20, 15, 30]
mental_health = [30, 35, 25, 20, 15, 25, 35, 30, 20, 25]
nutrition = [25, 30, 35, 30, 20, 15, 20, 25, 40, 25]
wellness = [25, 20, 30, 25, 35, 25, 20, 25, 25, 20]

# Stack bar chart data
data = np.array([physical_health, mental_health, nutrition, wellness])
data_cum = data.cumsum(axis=0)

# Bar width
bar_width = 0.5

# Colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))

categories_pos = np.arange(len(categories))

for i, (colname, color) in enumerate(zip(['Physical Health', 'Mental Health', 'Nutrition', 'Wellness'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories_pos, widths, left=starts, height=bar_width, label=colname, color=color)

# Adding labels
ax.set_yticks(categories_pos)
ax.set_yticklabels(categories)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
ax.set_xlabel('Percentage')
ax.set_title('Weekly Health & Wellness Data')

plt.show()