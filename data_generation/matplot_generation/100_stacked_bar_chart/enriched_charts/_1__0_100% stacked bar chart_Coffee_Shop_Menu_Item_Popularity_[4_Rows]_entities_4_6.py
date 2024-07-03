
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
values1 = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
values2 = np.array([30, 35, 25, 30, 20, 15, 10, 5, 0, 5, 10, 15])
values3 = np.array([10, 15, 20, 25, 30, 35, 40, 35, 30, 20, 10, 5])
values4 = np.array([40, 25, 25, 10, 10, 5, 0, 5, 10, 10, 10, 5])

# Normalize data to 100% for each category
totals = values1 + values2 + values3 + values4
values1 = values1 / totals * 100
values2 = values2 / totals * 100
values3 = values3 / totals * 100
values4 = values4 / totals * 100

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.5
x = np.arange(len(categories))

ax.barh(x, values1, color='#FF5733', edgecolor='white', height=bar_width, label='Value1')
ax.barh(x, values2, left=values1, color='#33FF57', edgecolor='white', height=bar_width, label='Value2')
ax.barh(x, values3, left=values1+values2, color='#3357FF', edgecolor='white', height=bar_width, label='Value3')
ax.barh(x, values4, left=values1+values2+values3, color='#F333FF', edgecolor='white', height=bar_width, label='Value4')

# Customizations
ax.set_xlabel('Percentage')
ax.set_title('Distribution of Values across Categories', pad=20)
ax.set_yticks(x)
ax.set_yticklabels(categories)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()