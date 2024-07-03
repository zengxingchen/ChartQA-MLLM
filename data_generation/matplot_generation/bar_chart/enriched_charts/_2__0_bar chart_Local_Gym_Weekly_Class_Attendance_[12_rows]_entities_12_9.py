
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
colors = ['#4B0082', '#483D8B', '#6A5ACD', '#7B68EE', '#9370DB',
          '#8A2BE2', '#9400D3', '#9932CC', '#BA55D3', '#DA70D6',
          '#EE82EE', '#D8BFD8', '#DDA0DD', '#DA70D6', '#FF00FF',
          '#FF1493', '#FF69B4', '#FFB6C1', '#FFC0CB', '#DB7093',
          '#B0E0E6', '#AFEEEE', '#5F9EA0', '#4682B4']

# Change width of bars
bar_width = 0.7

# Change width and height of the chart
plt.figure(figsize=(12, 10))

# Vertical bar chart
plt.bar(x=cities, height=populations, color=colors, width=bar_width)

# Adding labels to the bars
for i, population in enumerate(populations):
    plt.text(i, population + 0.3, str(population), ha='center')

# Change the topic, headline and data type of the chart
plt.ylabel('Population (Millions)')
plt.title('Major City Populations Around the World')
plt.ylim(0, max(populations) + 5)  # Adjust the y-axis to fit the text
plt.xticks(rotation=90)  # Rotate city names for better readability

# Show the plot
plt.show()