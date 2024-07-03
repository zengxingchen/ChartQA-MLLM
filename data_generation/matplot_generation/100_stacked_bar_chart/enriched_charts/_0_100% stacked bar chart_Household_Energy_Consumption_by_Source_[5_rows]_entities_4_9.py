
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2016', '2017', '2018', '2019', '2020']
data = {
    'Coal': [30, 28, 27, 25, 22],
    'Natural Gas': [25, 27, 28, 30, 33],
    'Renewables': [20, 22, 25, 28, 30],
    'Nuclear': [15, 13, 12, 10, 10],
    'Oil': [10, 10, 8, 7, 5]
}

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.6

# Prepare the bottom values
bottoms = np.zeros(len(years))

# Plot data
for (category, values), color in zip(data.items(), colors):
    ax.barh(years, values, color=color, edgecolor='white', height=bar_width, left=bottoms)
    bottoms += np.array(values)

# Add text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Percentage')
ax.set_title('Energy Source Market Share in Power Generation (2016-2020)')
ax.set_xlim(0, 100)
ax.set_xticks(np.arange(0, 101, 10))
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.8)

# Legend
handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors]
labels = list(data.keys())
ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()