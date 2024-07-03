
import matplotlib.pyplot as plt
import numpy as np

categories = ['USA', 'Canada', 'UK', 'Australia', 'Germany', 'France', 'Japan', 'China', 'India', 'Brazil', 'South Africa', 'Russia', 'Mexico', 'South Korea', 'Italy']
walking = [25, 20, 30, 35, 28, 32, 25, 30, 35, 28, 32, 25, 30, 35, 28]
running = [30, 25, 20, 15, 22, 18, 25, 20, 25, 22, 18, 25, 20, 15, 22]
swimming = [15, 20, 25, 25, 20, 25, 20, 25, 15, 25, 20, 20, 25, 25, 20]
cycling = [30, 35, 25, 25, 30, 25, 30, 25, 25, 25, 30, 30, 25, 25, 30]

# Data
data = np.array([walking, running, swimming, cycling])
data_cum = data.cumsum(axis=0)

# Color scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

fig, ax = plt.subplots(figsize=(10, 6))

ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=0).max())

# Plot bars
for i, (colname, color) in enumerate(zip(['Walking', 'Running', 'Swimming', 'Cycling'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    rects = ax.barh(categories, widths, left=starts, height=0.7, label=colname, color=color)

# Add a legend and title
ax.legend(ncol=4, bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', fontsize='small')
ax.set_title('Preferred Exercise Activities by Country', pad=20)

plt.show()