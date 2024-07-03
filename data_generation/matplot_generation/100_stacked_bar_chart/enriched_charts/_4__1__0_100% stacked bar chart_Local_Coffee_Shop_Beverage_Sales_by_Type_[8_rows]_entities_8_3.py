
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Science Fiction', 'Romance', 'Historical Fiction', 'Fantasy', 'Mystery']
years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
data = np.array([
    [25, 20, 30, 35, 25, 20, 30, 35],
    [35, 30, 25, 20, 25, 30, 20, 15],
    [30, 25, 20, 15, 35, 25, 20, 25],
    [10, 20, 15, 25, 10, 15, 25, 15],
    [0, 5, 10, 5, 5, 10, 5, 10]
])

# Colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']

# Plotting
fig, ax = plt.subplots(figsize=(10, 12))
width = 0.6

# Stacking bars vertically
for i in range(len(data)):
    if i == 0:
        ax.bar(years, data[i], color=colors[i], edgecolor='white', width=width)
    else:
        ax.bar(years, data[i], bottom=np.sum(data[:i], axis=0), color=colors[i], edgecolor='white', width=width)

# Title and labels
ax.set_title('Book Genre Popularity Over Years (2018-2025)', fontsize=16, pad=20)
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Years')
ax.legend(categories, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Show plot
plt.tight_layout()
plt.show()