
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G', 'Group H']
reading = [25, 20, 15, 10, 20, 25, 15, 20]
watching_tv = [15, 30, 25, 20, 10, 20, 25, 15]
playing_sports = [10, 15, 20, 25, 30, 15, 10, 15]
traveling = [20, 10, 10, 10, 20, 15, 15, 20]
cooking = [20, 15, 15, 15, 10, 10, 25, 20]
others = [10, 10, 15, 20, 10, 15, 10, 10]

data = np.array([reading, watching_tv, playing_sports, traveling, cooking, others])
data_cum = data.cumsum(axis=0)

# Colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FFB266']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.5

# Create stacked bars
for i, (colname, color) in enumerate(zip(['Reading', 'Watching TV', 'Playing Sports', 'Traveling', 'Cooking', 'Others'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(labels, widths, left=starts, height=bar_width, label=colname, color=color)

# Add legend
ax.legend(loc='lower right', bbox_to_anchor=(1.0, 1.0))

# Add title and labels
ax.set_title('Entertainment & Leisure Activities by Group')
ax.set_xlabel('Percentage')
ax.set_ylabel('Group')

plt.show()