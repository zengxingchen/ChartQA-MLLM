
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Region 1', 'Region 2', 'Region 3', 'Region 4', 'Region 5', 'Region 6', 'Region 7', 'Region 8']
product_a = [200, 180, 210, 190, 220, 205, 215, 225]
product_b = [150, 140, 160, 155, 170, 165, 175, 180]
product_c = [100, 110, 105, 115, 120, 130, 125, 135]
product_d = [50, 60, 70, 55, 80, 65, 75, 85]

bar_width = 0.4  # Change the bar width
fig, ax = plt.subplots(figsize=(10, 7))  # Change the figure size

# Location of bars on x-axis
ind = np.arange(len(categories))

# Stacked bar chart
plt.bar(ind, product_a, width=bar_width, color='#FF6347')
plt.bar(ind, product_b, width=bar_width, bottom=product_a, color='#4682B4')
plt.bar(ind, product_c, width=bar_width, bottom=np.add(product_a, product_b), color='#32CD32')
plt.bar(ind, product_d, width=bar_width, bottom=np.add(product_a, np.add(product_b, product_c)), color='#FFD700')

# Labels and Titles
ax.set_ylabel('Revenue (in millions)')
ax.set_title('Regional Revenue Distribution of Four Products')
ax.set_xticks(ind)
ax.set_xticklabels(categories)
ax.set_xlabel('Region')

# Legend
plt.legend(['Product A', 'Product B', 'Product C', 'Product D'], loc='upper left')

# Display the chart
plt.show()