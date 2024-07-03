
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10']
mathematics = [10, 20, 30, 25, 35, 20, 25, 30, 20, 25]
science = [15, 15, 20, 30, 25, 30, 25, 20, 25, 30]
history = [20, 25, 15, 20, 25, 30, 35, 30, 25, 30]
art = [25, 20, 35, 25, 20, 20, 15, 20, 30, 15]

# Colors
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

# Stack the data
data = np.array([mathematics, science, history, art])
data_cum = data.cumsum(axis=0)

# Plot
fig, ax = plt.subplots(figsize=(8, 10))
category_labels = ['Mathematics', 'Science', 'History', 'Art']
category_width = 0.7  # Width of each category

for i, color in enumerate(colors):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(categories, heights, bottom=starts, width=category_width, label=category_labels[i], color=color)

# Formatting
ax.set_ylabel('Percentage')
ax.set_title('Academic Performance by Grade')
ax.legend(ncol=1, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()