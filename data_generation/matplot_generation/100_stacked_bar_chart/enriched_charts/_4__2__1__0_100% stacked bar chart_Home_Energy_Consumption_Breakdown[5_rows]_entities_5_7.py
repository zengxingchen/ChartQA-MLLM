
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Country1', 'Country2', 'Country3', 'Country4', 'Country5', 'Country6', 'Country7', 'Country8', 'Country9', 'Country10']
infrastructure = [25, 30, 20, 35, 40, 30, 25, 35, 40, 30]
science = [35, 25, 30, 20, 15, 25, 30, 20, 25, 30]
military = [20, 25, 25, 30, 35, 30, 30, 25, 20, 25]
health = [15, 10, 15, 10, 5, 10, 10, 15, 10, 10]
education = [5, 10, 10, 5, 5, 5, 5, 5, 5, 5]

# Colors
colors = ['#4B8BBE', '#306998', '#FFE873', '#FFD43B', '#646464']

# Plot
bar_width = 0.5
fig, ax = plt.subplots(figsize=(10, 10))

# Stacked bar chart
ax.bar(categories, infrastructure, color=colors[0], edgecolor='white', width=bar_width)
ax.bar(categories, science, bottom=np.array(infrastructure), color=colors[1], edgecolor='white', width=bar_width)
ax.bar(categories, military, bottom=np.array(infrastructure)+np.array(science), color=colors[2], edgecolor='white', width=bar_width)
ax.bar(categories, health, bottom=np.array(infrastructure)+np.array(science)+np.array(military), color=colors[3], edgecolor='white', width=bar_width)
ax.bar(categories, education, bottom=np.array(infrastructure)+np.array(science)+np.array(military)+np.array(health), color=colors[4], edgecolor='white', width=bar_width)

# Title and labels
ax.set_ylabel('Percentage')
ax.set_title('Government Spending Distribution by Sector in Various Countries', pad=20)
ax.legend(['Infrastructure', 'Science', 'Military', 'Health', 'Education'], bbox_to_anchor=(1.05, 1), loc='upper left')

# Show plot
plt.tight_layout()
plt.show()