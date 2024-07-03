
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Reading', 'Writing', 'Math', 'Science', 'History', 'Geography', 'Physical Education', 'Arts', 'Music', 'Technology']
A = [20, 30, 25, 25, 30, 20, 25, 30, 20, 25]
B = [30, 25, 20, 25, 20, 30, 25, 20, 30, 25]
C = [25, 20, 30, 25, 30, 30, 25, 25, 25, 25]
D = [25, 25, 25, 25, 20, 20, 25, 25, 25, 25]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

# Plotting
barWidth = 0.5
fig, ax = plt.subplots(figsize=(12, 8))

# Create stacked bar chart
bars1 = np.add(A, B).tolist()
bars2 = np.add(bars1, C).tolist()

ax.barh(categories, A, color=colors[0], edgecolor='white', height=barWidth, label='A')
ax.barh(categories, B, left=A, color=colors[1], edgecolor='white', height=barWidth, label='B')
ax.barh(categories, C, left=bars1, color=colors[2], edgecolor='white', height=barWidth, label='C')
ax.barh(categories, D, left=bars2, color=colors[3], edgecolor='white', height=barWidth, label='D')

# Add title and labels
ax.set_title('Student Performance in Different Subjects', fontsize=16, pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Subjects')

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))

# Show plot
plt.show()