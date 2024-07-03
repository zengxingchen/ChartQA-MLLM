
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Semester 1', 'Semester 2', 'Semester 3', 'Semester 4', 'Semester 5']
math = [75, 80, 70, 85, 90]
science = [80, 75, 85, 70, 85]
english = [85, 90, 75, 80, 80]
history = [70, 65, 80, 75, 65]
art = [90, 85, 95, 80, 75]

# Create numpy array for stack bars
data = np.array([math, science, english, history, art])

# Colors for each stack
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FFD700']

# Create vertical stacked bar chart
fig, ax = plt.subplots(figsize=(10, 8))

# Stacked bars
bars = ax.bar(categories, data[0], color=colors[0], width=0.5)
for i in range(1, data.shape[0]):
    bars = ax.bar(categories, data[i], bottom=np.sum(data[:i], axis=0), color=colors[i], width=0.5)

# Add legend and title
ax.legend(['Math', 'Science', 'English', 'History', 'Art'], bbox_to_anchor=(1.05, 1), loc='upper left')
ax.set_title('Average Grades by Semester', fontsize=16, pad=20)

# Show plot
plt.tight_layout()
plt.show()