
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Banks', 'Investment Firms', 'Insurance', 'Real Estate', 'FinTech', 'Venture Capital', 'Private Equity', 'Hedge Funds']
segments = {
    'Segment1': [30, 25, 45, 20, 35, 25, 30, 35],
    'Segment2': [50, 35, 30, 40, 25, 35, 45, 30],
    'Segment3': [20, 40, 25, 40, 40, 40, 25, 35]
}
colors = ['#FF5733', '#33FF57', '#3357FF']

# Convert data to a percentage stacked format
data = np.array([segments['Segment1'], segments['Segment2'], segments['Segment3']])
data_cum = data.cumsum(axis=0)

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
category_indices = np.arange(len(categories))

# Vertical bar chart
for i, (colname, color) in enumerate(zip(segments.keys(), colors)):
    heights = data[i]
    bottoms = data_cum[i] - heights
    ax.bar(category_indices, heights, bottom=bottoms, width=0.6, label=colname, color=color)

# Formatting
ax.set_xticks(category_indices)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.set_ylabel('Percentage')
ax.set_title('Market Segments in Economics & Finance')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()

plt.show()