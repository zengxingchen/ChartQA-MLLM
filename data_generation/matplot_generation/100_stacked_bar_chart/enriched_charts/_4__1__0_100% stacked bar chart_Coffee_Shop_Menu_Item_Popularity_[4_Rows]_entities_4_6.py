
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
values1 = np.array([22, 26, 29, 32, 35, 38, 42, 46, 50, 55, 60, 65, 70, 75, 80])
values2 = np.array([28, 34, 24, 32, 20, 17, 12, 7, 5, 6, 7, 9, 12, 15, 18])
values3 = np.array([12, 17, 19, 15, 24, 27, 30, 33, 25, 15, 10, 5, 3, 2, 1])
values4 = np.array([38, 23, 28, 21, 21, 18, 16, 14, 20, 24, 23, 21, 15, 8, 1])

# Normalize data to 100% for each category
totals = values1 + values2 + values3 + values4
values1 = values1 / totals * 100
values2 = values2 / totals * 100
values3 = values3 / totals * 100
values4 = values4 / totals * 100

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

bar_width = 0.8
x = np.arange(len(categories))

ax.bar(x, values1, color='#1f77b4', edgecolor='white', width=bar_width, label='Value1')
ax.bar(x, values2, bottom=values1, color='#ff7f0e', edgecolor='white', width=bar_width, label='Value2')
ax.bar(x, values3, bottom=values1+values2, color='#2ca02c', edgecolor='white', width=bar_width, label='Value3')
ax.bar(x, values4, bottom=values1+values2+values3, color='#d62728', edgecolor='white', width=bar_width, label='Value4')

# Customizations
ax.set_ylabel('Percentage')
ax.set_title('Popularity of Sports Activities by Category', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()