
import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023']
calories_consumed = np.array([2000, 2100, 1900, 2200, 2300, 2100, 2250, 2150, 2050, 2200, 2300, 2400])
steps_taken = np.array([5000, 5500, 6000, 5800, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600])
sleep_hours = np.array([7, 6.5, 7.2, 6.8, 7.1, 7.5, 6.9, 7.3, 7, 7.2, 6.8, 7.1])

fig, ax = plt.subplots(figsize=(12, 10))
bar_width = 0.4

bar1 = ax.bar(quarters, calories_consumed, width=bar_width, color='#4e79a7')
bar2 = ax.bar(quarters, steps_taken, width=bar_width, bottom=calories_consumed, color='#f28e2c')
bar3 = ax.bar(quarters, sleep_hours * 1000, width=bar_width, bottom=calories_consumed + steps_taken, color='#76b7b2')

ax.set_ylabel('Calories, Steps, and Sleep Hours (multiplied by 1000)', fontsize=14)
ax.set_xlabel('Quarter', fontsize=14)
ax.set_title('Quarterly Health Metrics over Three Years', fontsize=16, pad=20)

ax.legend((bar1[0], bar2[0], bar3[0]), ('Calories Consumed', 'Steps Taken', 'Sleep Hours (x1000)'))

for bar in bar1 + bar2 + bar3:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, color='white')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()