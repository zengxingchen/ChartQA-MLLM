
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
cultural = [30, 35, 25, 20, 20, 15]
adventure = [25, 20, 30, 25, 25, 20]
relaxation = [20, 25, 20, 30, 25, 35]
nature = [25, 20, 25, 25, 30, 30]

# Data preparation
data = np.array([cultural, adventure, relaxation, nature])
data_cum = data.cumsum(axis=0)

category_colors = ['#FF5733', '#33FFBD', '#335BFF', '#FF33A6']

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, len(labels))
ax.set_ylim(0, 100)

# Plot bars
for i, (colname, color) in enumerate(zip(['Cultural', 'Adventure', 'Relaxation', 'Nature'], category_colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(labels, heights, bottom=starts, width=0.6, label=colname, color=color)

# Add labels
ax.legend(ncol=len(category_colors), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
plt.title('Distribution of Travel Experiences by Age Group', pad=20)

plt.show()