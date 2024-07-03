
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Bangkok', 'Moscow',
          'Dubai', 'Istanbul', 'Lagos', 'Paris', 'Jakarta', 'London',
          'Hanoi', 'Buenos Aires', 'Chongqing', 'Dhaka', 'Karachi', 'Guangzhou']
populations = [37.4, 30.3, 27.0, 22.0, 20.4, 21.8, 20.5, 19.2, 20.1, 18.8,
               10.5, 12.5, 3.4, 15.5, 14.3, 11.0, 10.5, 9.0, 8.0, 15.2,
               16.4, 21.0, 16.0, 15.3]

# Modify the color scheme using specific color codes
colors = ['#FF6347', '#FFD700', '#FF69B4', '#7FFFD4', '#8A2BE2',
          '#5F9EA0', '#7FFF00', '#D2691E', '#FF7F50', '#6495ED',
          '#DC143C', '#00FFFF', '#00008B', '#008B8B', '#B8860B',
          '#A9A9A9', '#006400', '#BDB76B', '#8B008B', '#556B2F',
          '#FF8C00', '#9932CC', '#8B0000', '#E9967A']

# Change width of bars
bar_width = 0.5

# Change width and height of the chart
plt.figure(figsize=(14, 8))

# Horizontal bar chart
plt.barh(y=cities, width=populations, color=colors, height=bar_width)

# Adding labels to the bars
for i, population in enumerate(populations):
    plt.text(population + 0.5, i, str(population), va='center')

# Change the topic, headline and data type of the chart
plt.xlabel('Population (Millions)')
plt.title('City Populations: A Comparative Study')
plt.xlim(min(populations) - 5, max(populations) + 5)  # Adjust the x-axis to fit the text

# Show the plot
plt.show()