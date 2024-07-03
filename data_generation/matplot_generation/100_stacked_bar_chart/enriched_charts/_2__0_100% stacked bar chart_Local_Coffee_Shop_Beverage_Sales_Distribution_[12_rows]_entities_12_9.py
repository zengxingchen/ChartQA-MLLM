
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['History', 'Science', 'Math', 'English']
groups = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']
data = np.array([
    [20, 30, 25, 25],
    [15, 35, 30, 20],
    [25, 25, 20, 30],
    [30, 10, 25, 35],
    [10, 20, 35, 35]
])

# Calculate percentage data
data_percentage = data / data.sum(axis=1)[:, None] * 100

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33']

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))
width = 0.8  # Width of the bars
x = np.arange(len(groups))

for i in range(len(categories)):
    ax.barh(x, data_percentage[:, i], left=np.sum(data_percentage[:, :i], axis=1), color=colors[i], edgecolor='white', height=width)

# Labels and title
ax.set_yticks(x)
ax.set_yticklabels(groups)
ax.set_xlabel('Percentage')
ax.set_title('Student Performance by Subject')

# Legend
ax.legend(categories, loc='upper right', bbox_to_anchor=(1.15, 1))

plt.show()