
import matplotlib.pyplot as plt
import numpy as np

# Data
activities = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
work = [30, 35, 40, 25, 30, 10, 5]
exercise = [10, 5, 5, 10, 5, 20, 15]
leisure = [20, 25, 20, 25, 30, 30, 30]
sleep = [30, 25, 25, 30, 25, 30, 40]
others = [10, 10, 10, 10, 10, 10, 10]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Stacked bar chart
ax.barh(activities, work, color='#FF5733', edgecolor='white')
ax.barh(activities, exercise, left=np.array(work), color='#33FF57', edgecolor='white')
ax.barh(activities, leisure, left=np.array(work) + np.array(exercise), color='#3357FF', edgecolor='white')
ax.barh(activities, sleep, left=np.array(work) + np.array(exercise) + np.array(leisure), color='#FF33A1', edgecolor='white')
ax.barh(activities, others, left=np.array(work) + np.array(exercise) + np.array(leisure) + np.array(sleep), color='#FFFF33', edgecolor='white')

# Labels and title
ax.set_xlabel('Percentage (%)')
ax.set_title('Daily Activities Breakdown')

# Legend
ax.legend(['Work', 'Exercise', 'Leisure', 'Sleep', 'Others'], bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()