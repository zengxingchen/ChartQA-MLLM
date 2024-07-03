
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['USA', 'Germany', 'China', 'France', 'India', 'Brazil', 'Canada', 'Australia', 'Japan', 'UK']
renewable = [30, 40, 20, 50, 10, 60, 50, 20, 20, 30]
non_renewable = [50, 40, 70, 30, 80, 30, 40, 70, 50, 50]
nuclear = [20, 20, 10, 20, 10, 10, 10, 10, 30, 20]

# Width and height of the chart
fig, ax = plt.subplots(figsize=(10, 8))

# Width of bars
bar_width = 0.7

# Colors
colors = ['#66c2a5', '#fc8d62', '#8da0cb']

# Stacked bar chart
x = np.arange(len(labels))
ax.barh(x, renewable, color=colors[0], edgecolor='white', height=bar_width, label='Renewable')
ax.barh(x, non_renewable, left=renewable, color=colors[1], edgecolor='white', height=bar_width, label='Non-Renewable')
ax.barh(x, nuclear, left=np.array(renewable) + np.array(non_renewable), color=colors[2], edgecolor='white', height=bar_width, label='Nuclear')

# Labels, title and legend
ax.set_xlabel('Percentage')
ax.set_title('Energy Sources by Country')
ax.set_yticks(x)
ax.set_yticklabels(labels)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()