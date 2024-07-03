
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023']
football = np.array([14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000])
basketball = np.array([17000, 18000, 17500, 18500, 19500, 20500, 21000, 22000, 22500, 23000, 23500, 24000])
baseball = np.array([25000, 26000, 25500, 26500, 27000, 28000, 27500, 28500, 29000, 29500, 30000, 30500])

# Plot
fig, ax = plt.subplots(figsize=(12, 10))  # Change width and height of the chart

bar_width = 0.4  # Change width of bars

# Stacked bars (vertical version)
bar1 = ax.bar(quarters, football, width=bar_width, color='#3498db')
bar2 = ax.bar(quarters, basketball, bottom=football, width=bar_width, color='#e74c3c')
bar3 = ax.bar(quarters, baseball, bottom=football+basketball, width=bar_width, color='#2ecc71')

# Labels and title
ax.set_ylabel('Revenue (USD)', fontsize=14)
ax.set_xlabel('Quarter', fontsize=14)
ax.set_title('Quarterly Revenue from Different Sports Events over Two Years', fontsize=16)

# Legend
ax.legend((bar1[0], bar2[0], bar3[0]), ('Football', 'Basketball', 'Baseball'))

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to fit everything properly
plt.show()