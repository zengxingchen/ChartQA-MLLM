
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
region_a = [20, 15, 25, 30, 22, 18, 27, 33]
region_b = [30, 35, 25, 20, 28, 32, 23, 17]
region_c = [25, 30, 30, 25, 27, 29, 30, 25]
region_d = [25, 20, 20, 25, 23, 21, 20, 25]

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
fig, ax = plt.subplots(figsize=(12, 6))
width = 0.5

ax.barh(categories, region_a_perc, color='#FF5733', edgecolor='white', height=width)
ax.barh(categories, region_b_perc, left=region_a_perc, color='#33FF57', edgecolor='white', height=width)
ax.barh(categories, region_c_perc, left=region_a_perc + region_b_perc, color='#3357FF', edgecolor='white', height=width)
ax.barh(categories, region_d_perc, left=region_a_perc + region_b_perc + region_c_perc, color='#FFFF33', edgecolor='white', height=width)

# Add labels and title
ax.set_xlabel('Percentage')
ax.set_title('Quarterly Market Share by Region', pad=20)
ax.legend(['Region A', 'Region B', 'Region C', 'Region D'], bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the chart
plt.tight_layout()
plt.show()