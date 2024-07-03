
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Running', 'Cycling', 'Swimming', 'Gym', 'Yoga']
years = ['2019', '2020', '2021', '2022', '2023']
data = np.array([
    [25, 20, 15, 25, 15],
    [20, 25, 20, 20, 15],
    [30, 15, 20, 25, 10],
    [25, 30, 15, 20, 10],
    [20, 25, 20, 25, 10]
])

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FFBD33']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked bar chart
for i in range(data.shape[1]):
    bottom = np.sum(data[:, :i], axis=1)
    ax.bar(years, data[:, i], bottom=bottom, color=colors[i], edgecolor='white', width=0.6)

# Title and labels
ax.set_title('Physical Activity Distribution by Type (2019-2023)', loc='center', pad=20)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')

# Legend
ax.legend(categories, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()