
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
running = [25, 20, 15, 30, 10, 20, 25]
cycling = [15, 25, 20, 10, 30, 25, 20]
swimming = [30, 25, 35, 30, 30, 20, 25]
yoga = [30, 30, 30, 30, 30, 35, 30]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

# Stack the data
data = np.array([running, cycling, swimming, yoga])
data_cum = data.cumsum(axis=0)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
category_labels = ['Running', 'Cycling', 'Swimming', 'Yoga']
category_width = 0.5  # Width of each category

for i, color in enumerate(colors):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=category_width, label=category_labels[i], color=color)

# Formatting
ax.set_xlabel('Percentage')
ax.set_title('Weekly Physical Activities Distribution')
ax.legend(ncol=len(category_labels), bbox_to_anchor=(0.5, -0.15), loc='upper center')
plt.show()