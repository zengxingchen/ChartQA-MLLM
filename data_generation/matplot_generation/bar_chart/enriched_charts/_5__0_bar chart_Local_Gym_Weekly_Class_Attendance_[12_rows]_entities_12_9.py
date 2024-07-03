
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Bangkok', 'Moscow',
          'Dubai', 'Istanbul', 'Lagos', 'Paris', 'Jakarta', 'London',
          'Hanoi', 'Buenos Aires', 'Sydney', 'Cape Town', 'Toronto', 
          'Berlin', 'Los Angeles', 'Rome']
temperatures = [16, 25, 16, 19, 27, 17, 12, 17, 22, 13, 29, 4,
                28, 15, 27, 12, 27, 11, 24, 18, 20, 14, 8, 
                10, 22, 16]

# Modify the color scheme using specific color codes
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6',
          '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845',
          '#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F',
          '#581845', '#DAF7A6', '#FFC300', '#FF5733', '#C70039',
          '#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6',
          '#FFC300']

# Change width of bars
bar_width = 0.7

# Change width and height of the chart
plt.figure(figsize=(12, 9))

# Change the direction of chart (vertical bar chart)
plt.bar(x=cities, height=temperatures, color=colors, width=bar_width)

# Change the y-axis limits to start from a specific value other than zero
plt.ylim(5, 30)

# Annotate each bar with its value
for i, temp in enumerate(temperatures):
    plt.text(i, temp + 0.5, str(temp), ha='center')

# Change the topic, headline and data type of the chart
plt.ylabel('Average Temperature (°C)')
plt.title('City Temperatures: A Climate Overview')
plt.xticks(rotation=90)

# Show the plot
plt.show()