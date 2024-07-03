
import matplotlib.pyplot as plt
import numpy as np

categories = ['School A', 'School B', 'School C', 'School D', 'School E', 'School F', 'School G', 'School H']
reading_scores = [85, 88, 90, 87, 86, 89, 91, 92]
writing_scores = [78, 82, 85, 80, 79, 83, 84, 86]
math_scores = [92, 95, 97, 91, 93, 94, 96, 98]

# Data
data = np.array([reading_scores, writing_scores, math_scores])
data_cum = data.cumsum(axis=0)

# Colors
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))
category_labels = categories
bar_width = 0.5

for i, (colname, color) in enumerate(zip(['Reading', 'Writing', 'Math'], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.barh(category_labels, heights, left=starts, height=bar_width, label=colname, color=color)

ax.set_xlabel('Percentage')
ax.set_title('Student Performance in Various Subjects')
ax.legend(loc='lower right')
plt.show()