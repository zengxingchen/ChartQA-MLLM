import matplotlib.pyplot as plt
import numpy as np

# Data for the percentage stacked bar chart
labels = ['USA', 'China', 'India', 'Germany', 'Brazil']
years = ['2000', '2010', '2020']
data = np.array([
    [25, 30, 35],   # USA
    [30, 25, 20],   # China
    [20, 20, 25],   # India
    [15, 10, 10],   # Germany
    [10, 15, 10]    # Brazil
])

data_cum = data.cumsum(axis=1)

# Colors for each year
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 7))

# Plot bars
for i, (colname, color) in enumerate(zip(years, colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    ax.barh(labels, widths, left=starts, height=0.5, label=colname, color=color)

# Add labels, title, legend, and format
ax.set_xlabel('Percentage')
ax.set_title('Population Distribution by Country and Year')
ax.legend(ncol=len(years), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

# Show plot
plt.tight_layout()
plt.show()