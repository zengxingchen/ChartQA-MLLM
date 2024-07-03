
import matplotlib.pyplot as plt

# Data for the chart
cities = [
    'Tokyo', 'New York', 'London', 'Paris', 'Moscow', 'Sydney', 
    'Cairo', 'Rio de Janeiro', 'New Delhi', 'Beijing', 
    'Toronto', 'Berlin', 'Rome', 'Istanbul', 'Mexico City'
]

average_rainfall = [
    1530, 1250, 620, 650, 710, 1170, 24, 1200, 800, 570, 
    830, 570, 870, 870, 700
]

# Color scheme
colors = [
    '#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99',
    '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a',
    '#ffff99', '#b15928', '#8dd3c7', '#ffffb3', '#bebada'
]

# Set the figure size for better clarity or visual appeal
plt.figure(figsize=(16, 10))

# Change the direction of the chart from vertical to horizontal
plt.barh(cities, average_rainfall, color=colors, height=0.6)

# Set y-axis limits to start from a specific value other than zero
plt.xlim(500, 1600)

# Add labels and title to the chart
plt.xlabel('Average Annual Rainfall (mm)')
plt.title('Average Annual Rainfall in Major Cities')

# Display the chart
plt.show()