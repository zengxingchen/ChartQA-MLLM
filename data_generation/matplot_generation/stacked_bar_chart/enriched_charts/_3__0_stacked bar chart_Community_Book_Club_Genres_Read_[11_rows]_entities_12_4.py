
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
product_x = [100, 140, 130, 160]
product_y = [90, 110, 120, 130]
product_z = [80, 100, 110, 120]

bar_width = 0.35  # Change the bar width
fig, ax = plt.subplots(figsize=(10, 7))  # Change the figure size

# Location of bars on x-axis
ind = np.arange(len(quarters))

# Stacked bar chart
plt.bar(ind, product_x, width=bar_width, color='#4CAF50', label='Product X')
plt.bar(ind, product_y, width=bar_width, bottom=product_x, color='#FF9800', label='Product Y')
plt.bar(ind, product_z, width=bar_width, bottom=np.add(product_x, product_y), color='#2196F3', label='Product Z')

# Labels and Titles
ax.set_ylabel('Units Sold')
ax.set_title('Quarterly Units Sold of Different Products')
ax.set_xticks(ind)
ax.set_xticklabels(quarters)
ax.set_xlabel('Quarter')

# Legend
plt.legend(loc='upper left')

# Adding numerical labels
for i in range(len(quarters)):
    plt.text(i, product_x[i] / 2, str(product_x[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(i, product_x[i] + product_y[i] / 2, str(product_y[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(i, product_x[i] + product_y[i] + product_z[i] / 2, str(product_z[i]), ha='center', va='center', color='white', fontweight='bold')

# Display the chart
plt.show()