
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2024', '2025', '2026', '2027', '2028']
stocks = [25, 30, 35, 40, 45]
bonds = [35, 30, 25, 20, 15]
real_estate = [20, 25, 30, 35, 40]
gold = [20, 15, 10, 5, 0]

# Stack data
data = np.array([stocks, bonds, real_estate, gold])
data_cum = data.cumsum(axis=0)

# Bar width
bar_width = 0.8

# Colors
colors = ['#1f77b4', '#ffbb78', '#2ca02c', '#d62728']

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 10))

# Plot bars
for i, (colname, color) in enumerate(zip(['Stocks', 'Bonds', 'Real Estate', 'Gold'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.bar(years, widths, bottom=starts, width=bar_width, label=colname, color=color)

# Add legend
ax.legend(ncol=2, bbox_to_anchor=(1, 1), loc='upper left')

# Add title and labels
ax.set_title('Investment Distribution Over Time (2024-2028)', fontsize=14, pad=20)
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Year')

plt.show()