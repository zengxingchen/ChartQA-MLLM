import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8']
subjects = ['Math', 'Science', 'Art', 'History', 'Physical Education']
data = np.array([
    [20, 25, 30, 15, 10],
    [22, 20, 25, 18, 15],
    [18, 28, 22, 17, 15],
    [25, 20, 20, 25, 10],
    [20, 30, 15, 25, 10],
    [23, 20, 22, 20, 15],
    [20, 25, 25, 20, 10],
    [25, 15, 20, 25, 15]
])

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.5

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8F33']

# Create stacked bar chart
bottoms = np.zeros(len(categories))
for i in range(data.shape[1]):
    ax.barh(categories, data[:, i], left=bottoms, height=bar_width, color=colors[i], label=subjects[i])
    bottoms += data[:, i]

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Add title and labels
ax.set_title('Student Performance by Subject', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Grades')

# Show plot
plt.tight_layout()
plt.show()