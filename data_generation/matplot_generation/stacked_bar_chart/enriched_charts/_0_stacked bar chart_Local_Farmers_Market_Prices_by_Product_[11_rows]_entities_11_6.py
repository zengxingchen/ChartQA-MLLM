
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022']
product_a = np.array([12000, 13000, 12500, 14500, 15000, 16000, 15500, 16500])
product_b = np.array([15000, 16000, 14000, 17000, 18000, 19000, 19500, 21000])
product_c = np.array([20000, 25000, 24000, 23000, 27000, 29000, 28000, 30000])

# Plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change width and height of the chart

bar_width = 0.5  # Change width of bars

# Stacked bars (horizontal version)
bar1 = ax.barh(quarters, product_a, height=bar_width, color='#1f77b4')
bar2 = ax.barh(quarters, product_b, left=product_a, height=bar_width, color='#ff7f0e')
bar3 = ax.barh(quarters, product_c, left=product_a+product_b, height=bar_width, color='#2ca02c')

# Labels and title
ax.set_xlabel('Sales (USD)', fontsize=14)
ax.set_ylabel('Quarter', fontsize=14)
ax.set_title('Quarterly Sales per Product over Two Years', fontsize=16)

# Legend
ax.legend((bar1[0], bar2[0], bar3[0]), ('Product A', 'Product B', 'Product C'))

plt.show()