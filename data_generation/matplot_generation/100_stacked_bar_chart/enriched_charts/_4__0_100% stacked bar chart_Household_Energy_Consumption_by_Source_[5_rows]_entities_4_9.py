
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2016', '2017', '2018', '2019', '2020']
data = {
    'Movies': [35, 38, 40, 42, 44],
    'Music': [25, 23, 22, 20, 18],
    'Gaming': [15, 17, 18, 20, 22],
    'Books': [10, 9, 8, 8, 6],
    'Sports': [15, 13, 12, 10, 10]
}

# Colors
colors = ['#4CAF50', '#FF5722', '#2196F3', '#9C27B0', '#FFC107']

fig, ax = plt.subplots(figsize=(12, 8))

# Bar width
bar_width = 0.7

# Prepare the bottom values
bottoms = np.zeros(len(categories))

# Plot data
for (category, values), color in zip(data.items(), colors):
    ax.bar(categories, values, color=color, edgecolor='white', width=bar_width, bottom=bottoms)
    bottoms += np.array(values)

# Add text for labels, title, and custom y-axis tick labels, etc.
ax.set_ylabel('Percentage')
ax.set_title('Entertainment Preferences Over Time (2016-2020)', pad=20)
ax.set_ylim(0, 100)
ax.set_yticks(np.arange(0, 101, 10))
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.8)

# Legend
handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors]
labels = list(data.keys())
ax.legend(handles, labels, loc='upper left', bbox_to_anchor=(1, 1))

plt.show()