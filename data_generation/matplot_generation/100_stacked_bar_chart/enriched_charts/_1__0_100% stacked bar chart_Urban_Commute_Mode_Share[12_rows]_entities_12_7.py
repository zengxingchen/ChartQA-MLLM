
import matplotlib.pyplot as plt
import numpy as np

# Data
activities = ['Running', 'Swimming', 'Cycling', 'Yoga', 'Weightlifting', 'Basketball', 'Hiking', 'Tennis', 'Dancing', 'Boxing']
duration = [30, 45, 60, 40, 50, 55, 70, 50, 35, 60]
calories_burned = [300, 400, 500, 200, 350, 450, 600, 400, 250, 500]
heart_rate = [120, 110, 115, 90, 100, 130, 105, 125, 100, 140]

# Normalize data to 100%
total = np.array(duration) + np.array(calories_burned) + np.array(heart_rate)
duration_perc = np.array(duration) / total * 100
calories_burned_perc = np.array(calories_burned) / total * 100
heart_rate_perc = np.array(heart_rate) / total * 100

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.5
bar_positions = np.arange(len(activities))

ax.barh(bar_positions, duration_perc, color='#1f77b4', edgecolor='white', height=bar_width, label='Duration')
ax.barh(bar_positions, calories_burned_perc, left=duration_perc, color='#ff7f0e', edgecolor='white', height=bar_width, label='Calories Burned')
ax.barh(bar_positions, heart_rate_perc, left=duration_perc+calories_burned_perc, color='#2ca02c', edgecolor='white', height=bar_width, label='Heart Rate')

# Labels and title
ax.set_yticks(bar_positions)
ax.set_yticklabels(activities)
ax.set_xlabel('Percentage')
ax.set_title('Physical Activities - Percentage Distribution of Duration, Calories Burned, and Heart Rate')
ax.legend(loc='upper right')

# Display
plt.tight_layout()
plt.show()