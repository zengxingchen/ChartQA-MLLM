
import matplotlib.pyplot as plt

# Definition of data points
years = ['2016', '2017', '2018', '2019', '2020']
fruits = [15, 18, 20, 22, 25]
vegetables = [20, 22, 24, 26, 28]
grains = [30, 28, 27, 26, 24]
dairy = [25, 26, 25, 24, 23]
protein = [10, 11, 12, 12, 13]

# Colors for the data series for better clarity
colors = ['#FF6347', '#4682B4', '#FFD700', '#8A2BE2', '#00FA9A']

# Create a figure and a set of subplots - modify width and height of the chart
fig, ax = plt.subplots(figsize=(12, 6))

# Change the width of bars
bar_width = 0.7

# Stacking bars vertically
ax.bar(years, fruits, color=colors[0], edgecolor='white', width=bar_width, label='Fruits')
ax.bar(years, vegetables, bottom=fruits, color=colors[1], edgecolor='white', width=bar_width, label='Vegetables')
ax.bar(years, grains, bottom=[i+j for i,j in zip(fruits, vegetables)], color=colors[2], edgecolor='white', width=bar_width, label='Grains')
ax.bar(years, dairy, bottom=[i+j+k for i,j,k in zip(fruits, vegetables, grains)], color=colors[3], edgecolor='white', width=bar_width, label='Dairy')
ax.bar(years, protein, bottom=[i+j+k+l for i,j,k,l in zip(fruits, vegetables, grains, dairy)], color=colors[4], edgecolor='white', width=bar_width, label='Protein')

# Labeling the chart
ax.set_ylabel('Percentage (%)')
ax.set_title('Diet Composition by Food Group (2016-2020)')

# Displaying the legend
ax.legend(loc='upper right')

# Show the plot
plt.show()