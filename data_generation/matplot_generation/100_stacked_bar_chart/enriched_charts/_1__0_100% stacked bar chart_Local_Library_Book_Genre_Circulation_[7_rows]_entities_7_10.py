
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Education', 'Healthcare', 'Infrastructure', 'Defense', 'Social Welfare']
years = ['2020', '2021', '2022']
data = np.array([
    [25, 30, 35],  # Education
    [20, 25, 30],  # Healthcare
    [15, 20, 10],  # Infrastructure
    [10, 10, 15],  # Defense
    [30, 15, 10]   # Social Welfare
])

# Colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Stack data
data_cum = data.cumsum(axis=1)

# Bar chart
fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.4

for i in range(len(categories)):
    ax.barh(years, data[i], left=data_cum[i] - data[i], height=bar_width, color=colors[i], label=categories[i])

# Add legend and labels
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel('Percentage')
ax.set_ylabel('Years')
ax.set_title('Budget Allocation Over Years')

plt.tight_layout()
plt.show()