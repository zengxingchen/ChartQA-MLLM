
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G', 'Group H']
domestic_travel = [30, 25, 20, 15, 20, 10, 25, 15]
international_travel = [25, 20, 25, 30, 15, 20, 15, 20]
hiking = [10, 15, 10, 20, 25, 30, 15, 20]
camping = [10, 10, 20, 15, 10, 20, 20, 25]
cruise = [15, 20, 15, 10, 15, 10, 15, 10]
others = [10, 10, 10, 10, 15, 10, 10, 10]

data = np.array([domestic_travel, international_travel, hiking, camping, cruise, others])
data_cum = data.cumsum(axis=0)

# Colors
colors = ['#FF5733', '#33FFBD', '#335BFF', '#8D33FF', '#FF33A8', '#33FF57']

# Plotting
fig, ax = plt.subplots(figsize=(10, 12))
bar_height = 0.5

# Create stacked bars
for i, (colname, color) in enumerate(zip(['Domestic Travel', 'International Travel', 'Hiking', 'Camping', 'Cruise', 'Others'], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(labels, heights, bottom=starts, width=bar_height, label=colname, color=color)

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

# Add title and labels
ax.set_title('Travel & Adventure Activities by Group')
ax.set_ylabel('Percentage')
ax.set_xlabel('Group')

plt.show()