
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Sports & Fitness', 'Entertainment & Leisure', 'Science & Nature', 'Health & Psychology', 'Future Technologies & Society', 
              'Food & Nutrition', 'Education & Learning', 'Politics & Governance', 'Art & Design', 'Economics & Finance']
values1 = [22, 25, 20, 30, 28, 20, 25, 30, 22, 25]
values2 = [28, 20, 25, 30, 22, 28, 25, 20, 28, 25]
values3 = [30, 25, 35, 20, 25, 22, 30, 25, 30, 20]
values4 = [20, 30, 20, 20, 25, 30, 20, 25, 20, 30]

# Bar width
bar_width = 0.5

# Create stacked bar chart
fig, ax = plt.subplots(figsize=(10, 12))

# Stack bars
p1 = ax.bar(categories, values1, color='#ff9999', width=bar_width)
p2 = ax.bar(categories, values2, bottom=values1, color='#66b3ff', width=bar_width)
p3 = ax.bar(categories, values3, bottom=np.add(values1, values2), color='#99ff99', width=bar_width)
p4 = ax.bar(categories, values4, bottom=np.add(np.add(values1, values2), values3), color='#ffcc99', width=bar_width)

# Title and labels
ax.set_title('Distribution of Interests by Category', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Categories')

# Legend
ax.legend((p1[0], p2[0], p3[0], p4[0]), ('Value1', 'Value2', 'Value3', 'Value4'), loc='best')

# Show plot
plt.show()