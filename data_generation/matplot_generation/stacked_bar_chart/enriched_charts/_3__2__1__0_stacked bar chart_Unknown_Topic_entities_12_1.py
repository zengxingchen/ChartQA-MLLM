
import matplotlib.pyplot as plt

# Definition of data points
years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
fruits = [15, 18, 20, 22, 24, 26, 28, 30]
vegetables = [10, 12, 14, 16, 18, 20, 22, 24]
grains = [25, 28, 30, 32, 34, 36, 38, 40]
protein = [20, 22, 25, 27, 29, 31, 33, 35]
dairy = [10, 11, 12, 13, 14, 15, 16, 17]

# Colors for the data series for better clarity
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1']

# Create a figure and a set of subplots - modify width and height of the chart
fig, ax = plt.subplots(figsize=(12, 10))

# Change the width of bars
bar_width = 0.7

# Stacking bars vertically
ax.bar(years, fruits, color=colors[0], edgecolor='white', width=bar_width, label='Fruits')
ax.bar(years, vegetables, bottom=fruits, color=colors[1], edgecolor='white', width=bar_width, label='Vegetables')
ax.bar(years, grains, bottom=[i+j for i,j in zip(fruits, vegetables)], color=colors[2], edgecolor='white', width=bar_width, label='Grains')
ax.bar(years, protein, bottom=[i+j+k for i,j,k in zip(fruits, vegetables, grains)], color=colors[3], edgecolor='white', width=bar_width, label='Protein')
ax.bar(years, dairy, bottom=[i+j+k+l for i,j,k,l in zip(fruits, vegetables, grains, protein)], color=colors[4], edgecolor='white', width=bar_width, label='Dairy')

# Labeling the chart
ax.set_ylabel('Percentage (%)')
ax.set_title('Dietary Composition by Food Type (2016-2023)', pad=20)

# Displaying the legend
ax.legend(loc='upper left')

# Adding numerical labels
for i, (f, v, g, p, d) in enumerate(zip(fruits, vegetables, grains, protein, dairy)):
    total = f + v + g + p + d
    ax.text(i, total + 2, str(total), ha='center')

# Show the plot
plt.tight_layout()
plt.show()