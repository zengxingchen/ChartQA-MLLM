
import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
art = [40, 90, 120, 110, 80, 60, 30]
music = [50, 85, 115, 100, 70, 50, 20]
travel = [60, 95, 130, 120, 90, 70, 40]
fashion = [70, 110, 140, 130, 100, 80, 50]

# Bubble sizes
bubble_scale = 200
art_sizes = np.array(art) * bubble_scale
music_sizes = np.array(music) * bubble_scale
travel_sizes = np.array(travel) * bubble_scale
fashion_sizes = np.array(fashion) * bubble_scale

fig, ax = plt.subplots(figsize=(16, 10))  # Set the width and height of the chart

# Create scatter points for each category
ax.scatter(age_groups, art, s=art_sizes, color='#FF5733', alpha=0.6, label='Art')
ax.scatter(age_groups, music, s=music_sizes, color='#33FF57', alpha=0.6, label='Music')
ax.scatter(age_groups, travel, s=travel_sizes, color='#3357FF', alpha=0.6, label='Travel')
ax.scatter(age_groups, fashion, s=fashion_sizes, color='#FF33A6', alpha=0.6, label='Fashion')

# Chart title and labels
ax.set_title('Interests by Age Group and Category', fontsize=20, pad=20)
ax.set_xlabel('Age Group', fontsize=14)
ax.set_ylabel('Interest Level', fontsize=14)

# Legend
ax.legend(loc='upper left', title='Categories')

plt.tight_layout()
plt.show()