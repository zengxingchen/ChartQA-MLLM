
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023']
product_a = np.array([20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000, 31000])
product_b = np.array([15000, 16000, 15500, 17000, 18000, 19000, 18500, 20000, 21000, 22000, 21500, 23000])
service_c = np.array([10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000])

# Plot
fig, ax = plt.subplots(figsize=(12, 10))  # Change width and height of the chart

bar_width = 0.5  # Change width of bars

# Stacked bars (vertical version)
bar1 = ax.bar(quarters, product_a, width=bar_width, color='#FF6347')
bar2 = ax.bar(quarters, product_b, width=bar_width, bottom=product_a, color='#4682B4')
bar3 = ax.bar(quarters, service_c, width=bar_width, bottom=product_a+product_b, color='#32CD32')

# Labels and title
ax.set_ylabel('Revenue in USD', fontsize=14)
ax.set_xlabel('Quarter', fontsize=14)
ax.set_title('Quarterly Revenue Sources for a Company', fontsize=16, pad=20)

# Legend
ax.legend((bar1[0], bar2[0], bar3[0]), ('Product A', 'Product B', 'Service C'))

# Numerical labels for each bar
for bars in [bar1, bar2, bar3]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + height/2, f'{int(height)}', va='center', ha='center', fontsize=10, color='white')

plt.tight_layout()  # Adjust layout to fit everything properly
plt.show()