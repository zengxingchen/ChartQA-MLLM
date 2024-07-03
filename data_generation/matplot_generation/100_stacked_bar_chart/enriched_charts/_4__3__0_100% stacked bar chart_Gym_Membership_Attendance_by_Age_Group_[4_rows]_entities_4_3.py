
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
reading = [2, 1, 3, 2, 1, 0, 0]
exercising = [1, 1, 2, 2, 1, 2, 1]
working = [6, 8, 5, 6, 8, 4, 2]
relaxing = [1, 2, 2, 2, 3, 6, 9]

# Data formatting
data = np.array([reading, exercising, working, relaxing])
data_cum = data.cumsum(axis=0)
category_colors = ['#FF5733', '#33FF57', '#3357FF', '#FFD133']

# Chart settings
fig, ax = plt.subplots(figsize=(12, 8))
ax.invert_yaxis()
ax.set_xlim(0, np.sum(data, axis=0).max())

# Plotting
for i, (colname, color) in enumerate(zip(['Reading', 'Exercising', 'Working', 'Relaxing'], category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    rects = ax.barh(categories, widths, left=starts, height=0.6, label=colname, color=color)

# Adding text
ax.set_title('Weekly Activity Breakdown', pad=20)
ax.legend(ncol=len(category_colors), bbox_to_anchor=(0.5, -0.1), loc='upper center')
plt.show()