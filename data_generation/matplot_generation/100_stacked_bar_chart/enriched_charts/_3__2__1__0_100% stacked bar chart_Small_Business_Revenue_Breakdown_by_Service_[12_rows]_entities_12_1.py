
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12']
science = [20, 25, 30, 25, 20, 30, 25, 25, 20, 30, 25, 25]
math = [30, 20, 25, 25, 35, 25, 30, 20, 25, 20, 25, 30]
english = [25, 30, 20, 30, 20, 25, 20, 30, 25, 25, 30, 20]
history = [25, 25, 25, 20, 25, 20, 25, 25, 30, 25, 20, 25]

# Stack the data
data = np.array([science, math, english, history])
data_cum = data.cumsum(axis=0)

# Parameters
category_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']
bar_width = 0.6

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

for i, (colname, color) in enumerate(zip(['Science', 'Math', 'English', 'History'], category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=bar_width, label=colname, color=color)

# Title and labels
ax.set_title('Subject Distribution Across Grades', loc='center')
ax.set_xlabel('Percentage')
ax.set_ylabel('Grades')
ax.legend(ncol=1, bbox_to_anchor=(1, 0.5), loc='center left')

plt.tight_layout()
plt.show()