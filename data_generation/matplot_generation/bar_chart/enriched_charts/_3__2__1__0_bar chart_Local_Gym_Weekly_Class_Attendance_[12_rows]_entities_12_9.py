
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Bangkok', 'Moscow',
          'Dubai', 'Istanbul', 'Lagos', 'Paris', 'Jakarta', 'London',
          'Hanoi', 'Buenos Aires', 'Cape Town', 'Sydney', 'Rio de Janeiro',
          'Los Angeles', 'Toronto', 'San Francisco', 'Berlin', 'Singapore',
          'Hong Kong', 'Johannesburg']
temperatures = [16, 25, 17, 20, 27, 18, 14, 16, 22, 12, 28, 5,
                30, 15, 26, 11, 27, 10, 24, 19, 17, 18, 24, 19,
                9, 14, 8, 27, 23, 16]

# Modify the color scheme using specific color codes
colors = ['#4B0082', '#8A2BE2', '#5F9EA0', '#7FFF00', '#D2691E', '#FF7F50',
          '#6495ED', '#DC143C', '#00FFFF', '#00008B', '#008B8B', '#B8860B',
          '#006400', '#8B008B', '#556B2F', '#FF8C00', '#9932CC', '#8B0000',
          '#E9967A', '#8FBC8F', '#483D8B', '#2F4F4F', '#00CED1', '#9400D3',
          '#FF1493', '#1E90FF', '#B22222', '#FFFAF0', '#228B22', '#DAA520']

# Change width of bars
bar_width = 0.5

# Change width and height of the chart
plt.figure(figsize=(10, 16))

# Change the direction of chart (vertical bar chart)
plt.barh(y=cities, width=temperatures, color=colors, height=bar_width)

# Add data labels
for i, temp in enumerate(temperatures):
    plt.text(temp + 0.5, i, str(temp), va='center')

# Change the topic, headline, and data type of the chart
plt.xlabel('Average Temperature (°C)')
plt.title('Average Annual Temperatures in Major Cities')
plt.xlim(0, max(temperatures) + 2)  # Adjust the x-axis to fit the text
plt.tight_layout()

# Show the plot
plt.show()