
import matplotlib.pyplot as plt

# Data points
destinations = [
    'Paris', 'New York', 'Tokyo', 'Rome', 'Sydney', 
    'London', 'Dubai', 'Singapore', 'Barcelona', 'Bangkok'
]

popularity = [
    25.5, 20.0, 15.0, 12.0, 10.0, 
    8.0, 5.0, 2.5, 1.5, 0.5
]

# Colors for each section
colors = [
    '#ff5733', '#33ff57', '#3357ff', '#ff33a6', '#f4d03f',
    '#8e44ad', '#48c9b0', '#f0b27a', '#85c1e9', '#34495e'
]

# Resize the chart
plt.figure(figsize=(14, 8))

# Create the pie chart
plt.pie(popularity, labels=destinations, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Popularity of Travel Destinations in 2023', pad=30)

# Display the chart
plt.show()