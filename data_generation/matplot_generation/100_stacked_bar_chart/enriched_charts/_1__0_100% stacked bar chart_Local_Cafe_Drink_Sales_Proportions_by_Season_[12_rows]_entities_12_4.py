
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F']
science = np.array([10, 20, 30, 25, 15, 20])
technology = np.array([20, 30, 25, 20, 25, 30])
engineering = np.array([30, 25, 20, 30, 35, 30])
mathematics = np.array([40, 25, 25, 25, 25, 20])

# Normalize data to 100%
totals = science + technology + engineering + mathematics
science = science / totals * 100
technology = technology / totals * 100
engineering = engineering / totals * 100
mathematics = mathematics / totals * 100

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.85

bars1 = ax.barh(categories, science, color=colors[0], edgecolor='white', height=bar_width)
bars2 = ax.barh(categories, technology, left=science, color=colors[1], edgecolor='white', height=bar_width)
bars3 = ax.barh(categories, engineering, left=science+technology, color=colors[2], edgecolor='white', height=bar_width)
bars4 = ax.barh(categories, mathematics, left=science+technology+engineering, color=colors[3], edgecolor='white', height=bar_width)

# Add labels
ax.set_xlabel('Percentage (%)')
ax.set_title('Distribution of STEM Subjects by Groups')

# Legend
ax.legend(['Science', 'Technology', 'Engineering', 'Mathematics'], loc='lower right')

plt.show()