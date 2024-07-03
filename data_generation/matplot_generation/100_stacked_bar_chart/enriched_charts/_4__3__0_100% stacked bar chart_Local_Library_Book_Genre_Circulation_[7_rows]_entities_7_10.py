
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
fig, ax = plt.subplots(figsize=(10, 10))  # Changed the size of the chart
width = 0.6  # Changed width of bars

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plotting
for i, category in enumerate(categories):
    bottom = data_percent[:, :i].sum(axis=1)
    ax.bar(grades, data_percent[:, i], bottom=bottom, width=width, color=colors[i], label=category)  # Changed to vertical bar

# Title and labels
ax.set_title('Subject Performance Distribution Across Grades', fontsize=16, pad=20)  # Changed title and its position
ax.set_ylabel('Percentage')
ax.set_xlabel('Grades')

# Legend
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1))

plt.show()