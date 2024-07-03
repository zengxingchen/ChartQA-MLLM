
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023']
healthy_eating = np.array([13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000])
exercise = np.array([15000, 16000, 15500, 17000, 17500, 18500, 19000, 20000, 20500, 21500, 22000, 23000])
work_life_balance = np.array([12000, 13000, 12500, 13500, 14000, 15000, 15500, 16000, 16500, 17000, 17500, 18000])

# Plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change width and height of the chart

bar_height = 0.6  # Change height of bars

# Stacked bars (horizontal version)
bar1 = ax.barh(quarters, healthy_eating, height=bar_height, color='#ff9999')
bar2 = ax.barh(quarters, exercise, left=healthy_eating, height=bar_height, color='#66b3ff')
bar3 = ax.barh(quarters, work_life_balance, left=healthy_eating+exercise, height=bar_height, color='#99ff99')

# Labels and title
ax.set_xlabel('Hours Spent', fontsize=14)
ax.set_ylabel('Quarter', fontsize=14)
ax.set_title('Quarterly Hours Spent on Wellness Activities over Three Years', fontsize=16, pad=20)

# Legend
ax.legend((bar1[0], bar2[0], bar3[0]), ('Healthy Eating', 'Exercise', 'Work-Life Balance'))

# Numerical labels for each bar
for bars in [bar1, bar2, bar3]:
    for bar in bars:
        width = bar.get_width()
        ax.text(bar.get_width() + bar.get_x(), bar.get_y() + bar.get_height()/2, f'{int(width)}', va='center', ha='left', fontsize=10)

plt.tight_layout()  # Adjust layout to fit everything properly
plt.show()