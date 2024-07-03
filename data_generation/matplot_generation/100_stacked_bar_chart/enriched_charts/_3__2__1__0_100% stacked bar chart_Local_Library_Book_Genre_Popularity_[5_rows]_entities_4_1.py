
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
cardio = [25, 30, 20, 25, 15, 20]
strength = [35, 25, 30, 20, 25, 20]
flexibility = [20, 25, 25, 30, 35, 40]
endurance = [20, 20, 25, 25, 25, 20]

# Data preparation
data = np.array([cardio, strength, flexibility, endurance])
data_cum = data.cumsum(axis=0)

category_colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

fig, ax = plt.subplots(figsize=(10, 7))
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=0).max())

# Plot bars
for i, (colname, color) in enumerate(zip(['Cardio', 'Strength Training', 'Flexibility', 'Endurance'], category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(labels, widths, left=starts, height=0.5, label=colname, color=color)

# Add labels
ax.legend(ncol=len(category_colors), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
plt.title('Distribution of Physical Activity Types by Age Group', pad=20)

plt.show()