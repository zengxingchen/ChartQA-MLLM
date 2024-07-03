
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2018', '2019', '2020', '2021', '2022']
part_a = np.array([25, 30, 35, 40, 45])
part_b = np.array([45, 40, 35, 30, 25])
part_c = np.array([30, 30, 30, 30, 30])

# Calculate percentages
total = part_a + part_b + part_c
part_a_perc = part_a / total * 100
part_b_perc = part_b / total * 100
part_c_perc = part_c / total * 100

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))

bar_width = 0.5

bars1 = ax.barh(categories, part_a_perc, color='#FF5733', edgecolor='white', height=bar_width, label='Part A')
bars2 = ax.barh(categories, part_b_perc, left=part_a_perc, color='#33FF57', edgecolor='white', height=bar_width, label='Part B')
bars3 = ax.barh(categories, part_c_perc, left=part_a_perc + part_b_perc, color='#3357FF', edgecolor='white', height=bar_width, label='Part C')

# Add labels
ax.set_xlabel('Percentage')
ax.set_title('Economic Sector Distribution Over Years')
ax.legend(loc='upper right')

# Show plot
plt.tight_layout()
plt.show()