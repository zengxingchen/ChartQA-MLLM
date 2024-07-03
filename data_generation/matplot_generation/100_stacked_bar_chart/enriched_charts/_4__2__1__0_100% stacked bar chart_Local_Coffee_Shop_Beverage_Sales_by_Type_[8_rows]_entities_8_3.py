
import matplotlib.pyplot as plt
import numpy as np

# Data
activities = ['Running', 'Cycling', 'Yoga', 'Swimming', 'Gym', 'Hiking', 'Dancing']
work = [15, 20, 10, 25, 30, 20, 15]
exercise = [20, 10, 25, 20, 15, 20, 25]
leisure = [10, 15, 15, 10, 10, 10, 10]
sleep = [50, 45, 40, 35, 35, 40, 40]
others = [5, 10, 10, 10, 10, 10, 10]

# Plotting
fig, ax = plt.subplots(figsize=(8, 12))

# Stacked bar chart
bar_width = 0.5
ax.bar(activities, work, width=bar_width, color='#4CAF50', edgecolor='white')
ax.bar(activities, exercise, bottom=np.array(work), width=bar_width, color='#FF9800', edgecolor='white')
ax.bar(activities, leisure, bottom=np.array(work) + np.array(exercise), width=bar_width, color='#2196F3', edgecolor='white')
ax.bar(activities, sleep, bottom=np.array(work) + np.array(exercise) + np.array(leisure), width=bar_width, color='#9C27B0', edgecolor='white')
ax.bar(activities, others, bottom=np.array(work) + np.array(exercise) + np.array(leisure) + np.array(sleep), width=bar_width, color='#FFC107', edgecolor='white')

# Labels and title
ax.set_ylabel('Percentage (%)')
ax.set_title('Physical Activities Breakdown', pad=20)

# Legend
ax.legend(['Work', 'Exercise', 'Leisure', 'Sleep', 'Others'], bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()