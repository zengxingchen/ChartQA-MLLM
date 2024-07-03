
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Mars', 'Venus', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
region_a = [10, 25, 30, 35, 20, 25, 30, 15]
region_b = [15, 20, 25, 40, 35, 30, 25, 10]
region_c = [30, 25, 20, 15, 25, 20, 30, 35]
region_d = [45, 30, 25, 10, 20, 25, 15, 40]

# Convert data to numpy arrays for stacking
region_a = np.array(region_a)
region_b = np.array(region_b)
region_c = np.array(region_c)
region_d = np.array(region_d)

# Normalize data to make percentages
total = region_a + region_b + region_c + region_d
region_a_perc = region_a / total * 100
region_b_perc = region_b / total * 100
region_c_perc = region_c / total * 100
region_d_perc = region_d / total * 100

# Plot
fig, ax = plt.subplots(figsize=(10, 8))
width = 0.6

ax.bar(categories, region_a_perc, color='#FF5733', edgecolor='white', width=width)
ax.bar(categories, region_b_perc, bottom=region_a_perc, color='#33FF57', edgecolor='white', width=width)
ax.bar(categories, region_c_perc, bottom=region_a_perc + region_b_perc, color='#3357FF', edgecolor='white', width=width)
ax.bar(categories, region_d_perc, bottom=region_a_perc + region_b_perc + region_c_perc, color='#FFFF33', edgecolor='white', width=width)

# Add labels and title
ax.set_ylabel('Percentage')
ax.set_title('Planetary Exploration Missions Distribution', pad=20)
ax.legend(['Region A', 'Region B', 'Region C', 'Region D'], bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the chart
plt.tight_layout()
plt.show()