
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2015', '2016', '2017', '2018', '2019']
red_meat = [20, 25, 30, 35, 40]
white_meat = [30, 25, 20, 15, 10]
vegetables = [25, 20, 15, 20, 25]
fruits = [15, 20, 25, 20, 15]
dairy = [10, 10, 10, 10, 10]

# Stack data
data = np.array([red_meat, white_meat, vegetables, fruits, dairy])
data_cum = data.cumsum(axis=0)

# Color scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6

for i, color in enumerate(colors):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(categories, heights, bottom=starts, width=bar_width, color=color)

# Add title and labels
ax.set_title('Yearly Food Consumption Distribution', pad=20)
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Years')

# Add legend
ax.legend(['Red Meat', 'White Meat', 'Vegetables', 'Fruits', 'Dairy'], bbox_to_anchor=(1.05, 1), loc='upper left')

# Show plot
plt.tight_layout()
plt.show()