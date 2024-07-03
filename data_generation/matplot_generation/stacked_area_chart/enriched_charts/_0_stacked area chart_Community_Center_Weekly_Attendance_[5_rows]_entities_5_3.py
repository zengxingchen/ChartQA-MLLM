
import matplotlib.pyplot as plt
import pandas as pd

# Data for the stacked area chart
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
product_a = [20000, 22000, 23000, 24000, 26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000]
product_b = [15000, 16000, 17000, 17500, 18000, 19000, 19500, 20000, 21000, 22000, 23000, 24000]
product_c = [5000, 5500, 5800, 6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800]

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(10, 6)) # Modify figure size
ax.stackplot(months, product_a, product_b, product_c, colors=['#FFC300', '#FF5733', '#C70039'])

# Customize the chart with a title and labels
ax.set_title('Monthly Revenue from Different Products (in USD)', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Revenue', fontsize=12)

# Assign annotation/text label on the chart.
for i in range(len(months)):
    ax.text(i, product_a[i] + product_b[i] + product_c[i], f"{product_a[i] + product_b[i] + product_c[i]:,}", ha='center', va='bottom')

# Show the figure
plt.tight_layout()
plt.show()