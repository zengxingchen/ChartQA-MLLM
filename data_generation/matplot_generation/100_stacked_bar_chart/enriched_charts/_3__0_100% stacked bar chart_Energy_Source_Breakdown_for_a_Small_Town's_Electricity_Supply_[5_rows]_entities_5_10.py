
import matplotlib.pyplot as plt
import numpy as np

# Data
topics = ['Climate Change Awareness', 'Renewable Energy Adoption', 'Carbon Footprint Reduction', 
          'Recycling Initiatives', 'Wildlife Conservation Efforts', 'Sustainable Agriculture', 
          'Water Conservation', 'Deforestation Prevention', 'Pollution Control', 'Green Building Practices']
group_a = [35, 40, 20, 25, 30, 30, 25, 35, 30, 40]
group_b = [30, 35, 25, 20, 25, 30, 35, 20, 25, 30]
group_c = [25, 15, 30, 35, 20, 20, 25, 25, 30, 20]
group_d = [10, 10, 25, 20, 25, 20, 15, 20, 15, 10]

# Stacking the groups
group_a = np.array(group_a)
group_b = np.array(group_b)
group_c = np.array(group_c)
group_d = np.array(group_d)

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.7
y = np.arange(len(topics))

ax.barh(y, group_a, color=colors[0], edgecolor='white', height=bar_width)
ax.barh(y, group_b, left=group_a, color=colors[1], edgecolor='white', height=bar_width)
ax.barh(y, group_c, left=group_a + group_b, color=colors[2], edgecolor='white', height=bar_width)
ax.barh(y, group_d, left=group_a + group_b + group_c, color=colors[3], edgecolor='white', height=bar_width)

# Labels and title
ax.set_xlabel('Percentage')
ax.set_title('Environmental Efforts by Category')
ax.set_yticks(y)
ax.set_yticklabels(topics)
ax.legend(['Group A', 'Group B', 'Group C', 'Group D'], loc='lower right')

plt.tight_layout()
plt.show()