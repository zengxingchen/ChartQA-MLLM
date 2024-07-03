
import matplotlib.pyplot as plt

# Definition of data points - as much data points as possible from the table
years = ['2016', '2017', '2018', '2019', '2020']
coal = [30, 28, 25, 23, 22]
natural_gas = [34, 35, 36, 37, 34]
renewables = [20, 22, 24, 26, 28]
nuclear = [12, 12, 11, 10, 12]
oil = [4, 3, 4, 4, 4]

# Colors for the data series for better clarity
colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e']

# Create a figure and a set of subplots - modify width and height of the chart
fig, ax = plt.subplots(figsize=(10, 8))

# Change the width of bars (here it's the height because this is a horizontal bar chart)
bar_height = 0.8

# Stacking bars horizontally
ax.barh(years, coal, color=colors[0], edgecolor='white', height=bar_height, label='Coal')
ax.barh(years, natural_gas, left=coal, color=colors[1], edgecolor='white', height=bar_height, label='Natural Gas')
ax.barh(years, renewables, left=[i+j for i,j in zip(coal, natural_gas)], color=colors[2], edgecolor='white', height=bar_height, label='Renewables')
ax.barh(years, nuclear, left=[i+j+k for i,j,k in zip(coal, natural_gas, renewables)], color=colors[3], edgecolor='white', height=bar_height, label='Nuclear')
ax.barh(years, oil, left=[i+j+k+l for i,j,k,l in zip(coal, natural_gas, renewables, nuclear)], color=colors[4], edgecolor='white', height=bar_height, label='Oil')

# Labeling the chart
ax.set_xlabel('Percentage (%)')
ax.set_title('Electricity Generation by Energy Source (2016-2020)')

# Displaying the legend
ax.legend()

# Show the plot
plt.show()