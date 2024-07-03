
import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023']
fruit_intake = np.array([20, 25, 22, 28, 30, 32, 35, 37, 40, 42, 45, 48])
vegetable_intake = np.array([15, 18, 17, 20, 25, 28, 30, 32, 35, 37, 38, 40])
grain_intake = np.array([30, 35, 33, 40, 38, 42, 45, 48, 50, 53, 55, 58])

fig, ax = plt.subplots(figsize=(14, 8))
bar_height = 0.5

bar1 = ax.barh(quarters, fruit_intake, height=bar_height, color='#1f77b4')
bar2 = ax.barh(quarters, vegetable_intake, height=bar_height, left=fruit_intake, color='#ff7f0e')
bar3 = ax.barh(quarters, grain_intake, height=bar_height, left=fruit_intake + vegetable_intake, color='#2ca02c')

ax.set_xlabel('Intake Amount', fontsize=14)
ax.set_ylabel('Quarter', fontsize=14)
ax.set_title('Quarterly Fruit, Vegetable, and Grain Intake (2021-2023)', fontsize=16, pad=20)

ax.legend((bar1[0], bar2[0], bar3[0]), ('Fruit Intake', 'Vegetable Intake', 'Grain Intake'))

for bar in bar1 + bar2 + bar3:
    width = bar.get_width()
    ax.annotate(f'{width}',
                xy=(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, color='white')

plt.tight_layout()
plt.show()