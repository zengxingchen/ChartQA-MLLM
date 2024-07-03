
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
ethics = [25, 30, 20, 35, 25, 30, 40, 35, 20, 25]
philosophy = [35, 25, 40, 30, 30, 35, 25, 30, 40, 35]
psychology = [40, 45, 40, 35, 45, 35, 35, 35, 40, 40]

# Stack data
data = np.array([ethics, philosophy, psychology])
data_cum = data.cumsum(axis=0)

# Reorder for horizontal bar chart
categories = np.array(categories)
categories = categories[::-1]
data = data[:, ::-1]
data_cum = data_cum[:, ::-1]

# Color codes
colors = ["#4daf4a", "#377eb8", "#ff7f00"]

fig, ax = plt.subplots(figsize=(10, 8))
bar_width = 0.6

# Create horizontal stacked bar chart
for i, (colname, color) in enumerate(zip(['Ethics', 'Philosophy', 'Psychology'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=bar_width, label=colname, color=color)

ax.set_xlabel('Percentage')
ax.set_ylabel('Category')
ax.set_title('Distribution of Focus Areas in Humanities')
ax.legend(loc='lower right')

plt.tight_layout()
plt.show()