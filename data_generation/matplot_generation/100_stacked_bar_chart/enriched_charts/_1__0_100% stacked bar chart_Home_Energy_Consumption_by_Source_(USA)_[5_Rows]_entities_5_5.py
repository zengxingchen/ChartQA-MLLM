
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Mental Health', 'Physical Health', 'Nutrition', 'Exercise', 'Sleep']
A = np.array([20, 15, 25, 10, 30])
B = np.array([30, 25, 35, 40, 20])
C = np.array([25, 30, 20, 30, 25])
D = np.array([25, 30, 20, 20, 25])

# Stack the data
data = np.vstack([A, B, C, D])
data_cum = data.cumsum(axis=0)

# Colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

# Plot settings
fig, ax = plt.subplots(figsize=(14, 8))

# Bar width
bar_width = 0.4

# Create the stacked bar chart
for i, (colname, color) in enumerate(zip(['A', 'B', 'C', 'D'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=bar_width, label=colname, color=color)

# Add labels
ax.set_xlabel('Percentage')
ax.set_title('Health & Psychology: Distribution of Factors')
ax.legend(loc='lower right')

plt.show()