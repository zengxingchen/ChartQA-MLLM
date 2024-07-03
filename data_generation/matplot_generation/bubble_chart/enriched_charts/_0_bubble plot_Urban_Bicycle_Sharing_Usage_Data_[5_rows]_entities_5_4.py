
import matplotlib.pyplot as plt
import numpy as np

# Define data points
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City', 'Beijing', 'Cairo', 'New York', 'Bangkok', 'Los Angeles', 'Moscow', 'Dubai', 'Sydney', 'Cape Town']
sunlight = [4.5, 8.3, 3.8, 4.7, 8.1, 6.4, 6.4, 9.1, 6.0, 5.3, 8.6, 1.7, 10.0, 7.0, 8.3]
max_temps = [30.8, 34.4, 32.2, 28.3, 32.1, 26.5, 31.0, 35.1, 28.9, 35.0, 29.4, 24.3, 41.0, 26.4, 26.0]
populations = [37.4, 30.3, 27.1, 22.0, 20.7, 21.7, 20.4, 20.1, 18.8, 10.5, 13.1, 12.6, 3.4, 5.3, 4.6]  # in millions

# Normalize population for bubble sizes
size_factor = 70
sizes = [p * size_factor for p in populations]

# Define colors
colors = ['#348ABD', '#A60628', '#7A68A6', '#467821', '#CF4457', '#188487', '#E24A33', '#A60628','#30a2da','#fc4f30','#e5ae38','#6d904f','#8b8b8b','#810f7c','#008080']

# Create the plot
plt.figure(figsize=(14,10))
plt.scatter(sunlight, max_temps, s=sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=0.5)

# Create labels and title
plt.title('Average Daily Sunlight vs. Average Max Temp with Population Bubble Sizes')
plt.xlabel('Average Daily Sunlight (hours)')
plt.ylabel('Average Max Temp (°C)')

# Add city labels to the bubbles
for i, city in enumerate(cities):
    plt.text(sunlight[i], max_temps[i], city, ha='center', va='center', fontsize=8)

# Show the plot
plt.tight_layout()
plt.show()