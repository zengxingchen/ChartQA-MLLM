
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = [
    'Employee 1', 'Employee 2', 'Employee 3', 'Employee 4', 
    'Employee 5', 'Employee 6', 'Employee 7', 'Employee 8', 
    'Employee 9', 'Employee 10', 'Employee 11', 'Employee 12'
]
innovation = [30, 25, 20, 15, 20, 10, 15, 25, 20, 10, 30, 15]
adaptability = [25, 30, 20, 10, 15, 20, 30, 25, 10, 15, 20, 25]
leadership = [20, 15, 30, 25, 10, 25, 20, 20, 30, 20, 25, 30]
collaboration = [15, 20, 25, 30, 20, 20, 25, 15, 20, 35, 10, 15]
communication = [10, 10, 5, 20, 35, 25, 10, 15, 20, 20, 15, 15]

# Stack the data
data = np.array([innovation, adaptability, leadership, collaboration, communication])
data_cum = data.cumsum(axis=0)

# Parameters
category_colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']
bar_width = 0.5

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

for i, (colname, color) in enumerate(zip(['Innovation', 'Adaptability', 'Leadership', 'Collaboration', 'Communication'], category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.bar(categories, widths, bottom=starts, width=bar_width, label=colname, color=color)

# Title and labels
ax.set_title('Employee Skills Distribution', loc='center')
ax.set_ylabel('Percentage')
ax.set_xlabel('Employees')
ax.legend(ncol=1, bbox_to_anchor=(1, 1), loc='upper left')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()