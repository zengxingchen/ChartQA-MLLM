
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023']
fruits = np.array([14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 19500])
vegetables = np.array([12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500])
dairy = np.array([10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500])

# Plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change width and height of the chart

bar_height = 0.6  # Change height of bars

# Stacked bars (horizontal version)
bar1 = ax.barh(quarters, fruits, height=bar_height, color='#1f77b4')
bar2 = ax.barh(quarters, vegetables, left=fruits, height=bar_height, color='#ff7f0e')
bar3 = ax.barh(quarters, dairy, left=fruits+vegetables, height=bar_height, color='#2ca02c')

# Labels and title
ax.set_xlabel('Revenue (USD)', fontsize=14)
ax.set_ylabel('Quarter', fontsize=14)
ax.set_title('Quarterly Revenue from Food Categories Over Three Years', fontsize=16, pad=20)

# Legend
ax.legend((bar1[0], bar2[0], bar3[0]), ('Fruits', 'Vegetables', 'Dairy'), loc='upper right')

# Add numerical labels
for bars in [bar1, bar2, bar3]:
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, f'{width:.0f}', ha='left', va='center')

plt.tight_layout()  # Adjust layout to fit everything properly
plt.show()