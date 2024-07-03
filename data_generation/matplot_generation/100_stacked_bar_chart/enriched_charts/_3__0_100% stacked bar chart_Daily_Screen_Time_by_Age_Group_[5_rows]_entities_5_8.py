
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Sports', 'Fitness', 'Wellness']
years = ['2019', '2020', '2021', '2022']
data = np.array([
    [20, 30, 25, 25], 
    [35, 25, 20, 20], 
    [45, 45, 55, 55]
])

# Convert data to percentages
data_cum = np.cumsum(data, axis=0)
data_perc = 100 * data / data_cum[-1]

# Colors
colors = ['#FF6347', '#4682B4', '#3CB371']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6

# Plot bars
for i, (colname, color) in enumerate(zip(categories, colors)):
    starts = data_cum[i] - data[i]
    ax.barh(years, data_perc[i], left=starts, height=bar_width, label=colname, color=color)

# Formatting
ax.set_title('Health & Fitness Trends Over Years', fontsize=16, pad=20)
ax.set_xlabel('Percentage', fontsize=14)
ax.set_ylabel('Years', fontsize=14)
ax.legend(loc='best', fontsize=12)

plt.show()