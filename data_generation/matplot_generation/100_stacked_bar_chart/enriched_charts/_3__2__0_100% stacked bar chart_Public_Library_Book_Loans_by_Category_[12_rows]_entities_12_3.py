import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2018', '2019', '2020', '2021', '2022']
science = np.array([15, 20, 10, 25, 20])
technology = np.array([25, 30, 35, 20, 25])
engineering = np.array([35, 25, 30, 35, 30])
mathematics = np.array([25, 25, 25, 20, 25])

# Calculate percentages
totals = science + technology + engineering + mathematics
science_percentage = science / totals * 100
technology_percentage = technology / totals * 100
engineering_percentage = engineering / totals * 100
mathematics_percentage = mathematics / totals * 100

# Plot
fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.8
categories_pos = np.arange(len(categories))

p1 = ax.barh(categories_pos, science_percentage, color='#1f77b4', edgecolor='white', height=bar_width, label='Science')
p2 = ax.barh(categories_pos, technology_percentage, left=science_percentage, color='#ff7f0e', edgecolor='white', height=bar_width, label='Technology')
p3 = ax.barh(categories_pos, engineering_percentage, left=science_percentage + technology_percentage, color='#2ca02c', edgecolor='white', height=bar_width, label='Engineering')
p4 = ax.barh(categories_pos, mathematics_percentage, left=science_percentage + technology_percentage + engineering_percentage, color='#d62728', edgecolor='white', height=bar_width, label='Mathematics')

# Add labels, title, legend, and adjust layout
ax.set_xlabel('Percentage')
ax.set_title('STEM Fields Enrollment (2018-2022)')
ax.set_yticks(categories_pos)
ax.set_yticklabels(categories)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()