
import matplotlib.pyplot as plt
import squarify

# Data points
destinations = [
    'Paris', 'New York', 'Tokyo', 'London', 'Bangkok', 'Dubai', 
    'Singapore', 'Rome', 'Istanbul', 'Barcelona', 'Hong Kong', 
    'Amsterdam', 'Las Vegas', 'Milan', 'Vienna', 'Sydney', 
    'Los Angeles', 'Madrid', 'Moscow', 'Berlin'
]
annual_visitors = [38, 55, 30, 40, 35, 20, 19, 10, 13, 18, 14, 16, 42, 9, 7, 15, 50, 12, 5, 10]
average_cost = [1000, 1200, 1500, 1100, 800, 1600, 1300, 900, 700, 950, 1400, 1000, 900, 850, 1150, 1800, 1300, 950, 1200, 950]

# Color scheme using specific color codes
colors = [
    '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', 
    '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC',
    '#EFC050', '#5B5EA6', '#9B2335', '#DFCFBE', '#55B4B0', 
    '#E15D44', '#7FCDCD', '#BC243C', '#C3447A', '#98B4D4'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(18, 14))

# Creating a treemap
squarify.plot(sizes=annual_visitors, label=destinations, color=colors, alpha=0.8, value=average_cost, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Popular Travel Destinations', fontsize=18, color='darkblue')
plt.suptitle('Annual Visitors (Millions) and Average Trip Cost (USD)', fontsize=22)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()