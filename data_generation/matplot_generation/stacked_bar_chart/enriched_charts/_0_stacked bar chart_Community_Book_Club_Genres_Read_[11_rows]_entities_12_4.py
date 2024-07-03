
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
product_a = [120, 150, 130, 160]
product_b = [80, 90, 95, 110]
product_c = [60, 70, 75, 85]

bar_width = 0.5  # Change the bar width
fig, ax = plt.subplots(figsize=(8, 6))  # Change the figure size

# Location of bars on x-axis
ind = np.arange(len(quarters))

# Stacked bar chart
plt.barh(ind, product_a, height=bar_width, color='#FFA07A')
plt.barh(ind, product_b, height=bar_width, left=product_a, color='#20B2AA')
plt.barh(ind, product_c, height=bar_width, left=np.add(product_a, product_b), color='#778899')

# Labels and Titles
ax.set_xlabel('Sales Revenue (in millions)')
ax.set_title('Quarterly Sales Revenue of Three Products')
ax.set_yticks(ind)
ax.set_yticklabels(quarters)
ax.set_ylabel('Quarter')

# Legend
plt.legend(['Product A', 'Product B', 'Product C'])

# Display the chart
plt.show()