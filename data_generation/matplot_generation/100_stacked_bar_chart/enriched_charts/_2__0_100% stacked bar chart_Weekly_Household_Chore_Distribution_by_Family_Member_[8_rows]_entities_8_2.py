
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Art & Design', 'Business & Entrepreneurship', 'Culture & Society', 'Education & Learning', 'Environment & Climate Change']
values1 = [20, 30, 25, 15, 20]
values2 = [25, 20, 30, 25, 30]
values3 = [35, 25, 20, 30, 25]
values4 = [20, 25, 25, 30, 25]

# Bar width
bar_width = 0.6

# Create stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stack bars
p1 = ax.barh(categories, values1, color='#1f77b4', height=bar_width)
p2 = ax.barh(categories, values2, left=values1, color='#ff7f0e', height=bar_width)
p3 = ax.barh(categories, values3, left=np.add(values1, values2), color='#2ca02c', height=bar_width)
p4 = ax.barh(categories, values4, left=np.add(np.add(values1, values2), values3), color='#d62728', height=bar_width)

# Title and labels
ax.set_title('Distribution of Interests by Category', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Categories')

# Legend
ax.legend((p1[0], p2[0], p3[0], p4[0]), ('Value1', 'Value2', 'Value3', 'Value4'), loc='best')

# Show plot
plt.show()