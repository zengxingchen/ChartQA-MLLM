
import matplotlib.pyplot as plt
import numpy as np

# Data
topics = ['Fashion Trends', 'Skincare Products', 'Luxury Brands', 
          'Sustainable Fashion', 'Beauty Standards', 'Makeup Tutorials', 
          'Celebrity Styles', 'Haircare Tips', 'Fitness Fashion', 'Streetwear']
group_a = [20, 25, 15, 30, 20, 35, 25, 30, 20, 15]
group_b = [25, 20, 30, 20, 25, 15, 30, 25, 35, 25]
group_c = [35, 30, 25, 20, 30, 25, 20, 15, 25, 35]
group_d = [20, 25, 30, 30, 25, 25, 25, 30, 20, 25]

# Stacking the groups
group_a = np.array(group_a)
group_b = np.array(group_b)
group_c = np.array(group_c)
group_d = np.array(group_d)

# Colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
bar_width = 0.8
x = np.arange(len(topics))

ax.bar(x, group_a, color=colors[0], edgecolor='white', width=bar_width)
ax.bar(x, group_b, bottom=group_a, color=colors[1], edgecolor='white', width=bar_width)
ax.bar(x, group_c, bottom=group_a + group_b, color=colors[2], edgecolor='white', width=bar_width)
ax.bar(x, group_d, bottom=group_a + group_b + group_c, color=colors[3], edgecolor='white', width=bar_width)

# Labels and title
ax.set_ylabel('Percentage')
ax.set_title('Fashion & Beauty Trends')
ax.set_xticks(x)
ax.set_xticklabels(topics, rotation=45, ha="right")
ax.legend(['Group A', 'Group B', 'Group C', 'Group D'], loc='upper left')

plt.tight_layout()
plt.show()