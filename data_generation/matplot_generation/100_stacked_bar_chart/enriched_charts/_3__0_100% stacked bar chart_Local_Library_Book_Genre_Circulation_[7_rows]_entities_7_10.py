
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Math', 'Science', 'English', 'History', 'Art']
grades = ['Grade 9', 'Grade 10', 'Grade 11', 'Grade 12']
data = np.array([
    [20, 30, 25, 15, 10],
    [22, 28, 23, 17, 10],
    [25, 20, 30, 15, 10],
    [18, 35, 22, 15, 10]
])

# Normalize data to 100%
data_percent = data / data.sum(axis=1)[:, None] * 100

# Plot settings
fig, ax = plt.subplots(figsize=(12, 8))  # Changed the size of the chart
width = 0.6  # Changed width of bars

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']

# Plotting
for i, category in enumerate(categories):
    bottom = data_percent[:, :i].sum(axis=1)
    ax.barh(grades, data_percent[:, i], left=bottom, height=width, color=colors[i], label=category)  # Changed to horizontal bar

# Title and labels
ax.set_title('Subject Performance Distribution Across Grades', fontsize=16)  # Changed title and its position
ax.set_xlabel('Percentage')
ax.set_ylabel('Grades')

# Legend
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.show()