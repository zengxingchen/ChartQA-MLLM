
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8']
product_a = [120, 150, 130, 160, 170, 140, 155, 165]
product_b = [80, 90, 95, 110, 100, 85, 115, 120]
product_c = [60, 70, 75, 85, 95, 90, 80, 105]

bar_width = 0.35
fig, ax = plt.subplots(figsize=(10, 8))

# Location of bars on x-axis
ind = np.arange(len(quarters))

# Stacked bar chart (vertical)
plt.bar(ind, product_a, width=bar_width, color='#FF5733')
plt.bar(ind, product_b, width=bar_width, bottom=product_a, color='#33FF57')
plt.bar(ind, product_c, width=bar_width, bottom=np.add(product_a, product_b), color='#3357FF')

# Labels and Titles
ax.set_ylabel('Sales Revenue (in millions)')
ax.set_title('Quarterly Sales Revenue of Three Products')
ax.set_xticks(ind)
ax.set_xticklabels(quarters)
ax.set_xlabel('Quarter')

# Legend
plt.legend(['Product A', 'Product B', 'Product C'], loc='upper left')

# Numerical labels on bars
for i in range(len(quarters)):
    plt.text(i, product_a[i] / 2, str(product_a[i]), ha='center', va='center', color='white')
    plt.text(i, product_a[i] + product_b[i] / 2, str(product_b[i]), ha='center', va='center', color='white')
    plt.text(i, product_a[i] + product_b[i] + product_c[i] / 2, str(product_c[i]), ha='center', va='center', color='white')

# Display the chart
plt.show()