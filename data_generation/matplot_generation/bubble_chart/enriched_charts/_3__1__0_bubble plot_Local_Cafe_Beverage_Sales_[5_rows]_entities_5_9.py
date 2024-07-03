
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
running = [15, 20, 25, 30, 35, 40, 45, 50, 55]
swimming = [5, 8, 10, 12, 15, 20, 25, 30, 35]
cycling = [12, 15, 18, 20, 22, 25, 30, 35, 40]
yoga = [8, 12, 16, 20, 25, 30, 35, 40, 45]
gym = [20, 25, 30, 35, 40, 45, 50, 55, 60]
walking = [10, 15, 20, 25, 30, 35, 40, 45, 50]
hiit = [3, 5, 7, 10, 12, 15, 18, 20, 25]

# Bubble sizes
bubble_scale = 50
running_sizes = np.array(running) * bubble_scale
swimming_sizes = np.array(swimming) * bubble_scale
cycling_sizes = np.array(cycling) * bubble_scale
yoga_sizes = np.array(yoga) * bubble_scale
gym_sizes = np.array(gym) * bubble_scale
walking_sizes = np.array(walking) * bubble_scale
hiit_sizes = np.array(hiit) * bubble_scale

fig, ax = plt.subplots(figsize=(18, 12))

# Create scatter points for each category
ax.scatter(years, running, s=running_sizes, color='#FF5733', alpha=0.6, label='Running')
ax.scatter(years, swimming, s=swimming_sizes, color='#33FFBD', alpha=0.6, label='Swimming')
ax.scatter(years, cycling, s=cycling_sizes, color='#3375FF', alpha=0.6, label='Cycling')
ax.scatter(years, yoga, s=yoga_sizes, color='#FF33A8', alpha=0.6, label='Yoga')
ax.scatter(years, gym, s=gym_sizes, color='#33FF57', alpha=0.6, label='Gym')
ax.scatter(years, walking, s=walking_sizes, color='#FF8C33', alpha=0.6, label='Walking')
ax.scatter(years, hiit, s=hiit_sizes, color='#8C33FF', alpha=0.6, label='HIIT')

# Chart title and labels
ax.set_title('Trends in Sports & Fitness Activities Over the Years', fontsize=24, pad=20)
ax.set_xlabel('Year', fontsize=18)
ax.set_ylabel('Number of Participants (in millions)', fontsize=18)

# Legend
ax.legend(loc='upper right', title='Activity')

plt.tight_layout()
plt.show()