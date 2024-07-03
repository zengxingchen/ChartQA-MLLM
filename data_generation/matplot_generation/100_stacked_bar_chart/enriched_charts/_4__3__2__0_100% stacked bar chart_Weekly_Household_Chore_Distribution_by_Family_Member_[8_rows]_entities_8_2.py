
import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2000, 2025)
walking = [30, 32, 35, 37, 40, 43, 45, 47, 50, 52, 55, 57, 60, 62, 65, 68, 70, 72, 75, 77, 80, 82, 85, 87, 90]
running = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
cycling = [55, 52, 48, 45, 41, 37, 34, 31, 27, 24, 20, 17, 13, 10, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Plot
fig, ax = plt.subplots(figsize=(12, 10))

bar_width = 0.5

p1 = ax.bar(years, walking, color='#FF5733', edgecolor='white', width=bar_width)
p2 = ax.bar(years, running, bottom=walking, color='#33FF57', edgecolor='white', width=bar_width)
p3 = ax.bar(years, cycling, bottom=np.array(walking) + np.array(running), color='#3357FF', edgecolor='white', width=bar_width)

ax.set_ylabel('Percentage')
ax.set_title('Physical Activity Distribution Over Time', pad=20)
ax.legend((p1[0], p2[0], p3[0]), ('Walking', 'Running', 'Cycling'), loc='upper right', bbox_to_anchor=(1.15, 1))

plt.show()