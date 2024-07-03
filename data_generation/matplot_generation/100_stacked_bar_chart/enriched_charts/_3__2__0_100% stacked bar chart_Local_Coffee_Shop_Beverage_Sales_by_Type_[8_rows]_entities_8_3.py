
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania', 'Antarctica']
segments = {
    'Segment1': [40, 25, 35, 50, 30, 45, 20],
    'Segment2': [30, 50, 45, 20, 30, 20, 40],
    'Segment3': [30, 25, 20, 30, 40, 35, 40]
}
colors = ['#FF6347', '#4682B4', '#3CB371']

# Convert data to a percentage stacked format
data = np.array([segments['Segment1'], segments['Segment2'], segments['Segment3']])
data_cum = data.cumsum(axis=0)

# Plot
fig, ax = plt.subplots(figsize=(10, 7))
category_indices = np.arange(len(categories))

# Horizontal bar chart
for i, (colname, color) in enumerate(zip(segments.keys(), colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(category_indices, widths, left=starts, height=0.5, label=colname, color=color)

# Formatting
ax.set_yticks(category_indices)
ax.set_yticklabels(categories)
ax.invert_yaxis()  # categories read top-to-bottom
ax.set_xlabel('Percentage')
ax.set_title('Regional Distribution of Market Segments')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05))
plt.tight_layout()

plt.show()