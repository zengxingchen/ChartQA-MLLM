
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8']
product_x = [200, 180, 190, 210, 220, 195, 205, 215]
product_y = [130, 140, 135, 125, 145, 150, 160, 155]
product_z = [90, 100, 110, 95, 105, 115, 120, 130]

bar_height = 0.5
fig, ax = plt.subplots(figsize=(12, 8))

# Location of bars on y-axis
ind = np.arange(len(quarters))

# Stacked bar chart (horizontal)
plt.barh(ind, product_x, height=bar_height, color='#FF5733')
plt.barh(ind, product_y, height=bar_height, left=product_x, color='#33FF57')
plt.barh(ind, product_z, height=bar_height, left=np.add(product_x, product_y), color='#3357FF')

# Labels and Titles
ax.set_xlabel('Sales Revenue (in millions)')
ax.set_title('Quarterly Revenue of Three Product Categories')
ax.set_yticks(ind)
ax.set_yticklabels(quarters)
ax.set_ylabel('Quarter')

# Legend
plt.legend(['Product X', 'Product Y', 'Product Z'], loc='upper right')

# Numerical labels on bars
for i in range(len(quarters)):
    plt.text(product_x[i] / 2, i, str(product_x[i]), ha='center', va='center', color='white')
    plt.text(product_x[i] + product_y[i] / 2, i, str(product_y[i]), ha='center', va='center', color='white')
    plt.text(product_x[i] + product_y[i] + product_z[i] / 2, i, str(product_z[i]), ha='center', va='center', color='white')

# Display the chart
plt.show()