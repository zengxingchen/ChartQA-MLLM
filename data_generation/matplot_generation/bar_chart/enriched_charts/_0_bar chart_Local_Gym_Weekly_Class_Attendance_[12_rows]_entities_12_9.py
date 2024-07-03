
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Bangkok', 'Moscow',
          'Dubai', 'Istanbul', 'Lagos', 'Paris', 'Jakarta', 'London',
          'Hanoi', 'Buenos Aires']
temperatures = [16, 25, 16, 19, 27, 17, 12, 17, 22, 13, 29, 4,
                28, 15, 27, 12, 27, 11, 24, 18]

# Modify the color scheme using specific color codes
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6',
          '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845',
          '#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F',
          '#581845', '#DAF7A6', '#FFC300', '#FF5733', '#C70039']

# Change width of bars
bar_width = 0.5

# Change width and height of the chart
plt.figure(figsize=(10, 8))

# Change the direction of chart (horizontal bar chart)
plt.barh(y=cities, width=temperatures, color=colors, height=bar_width)

# Change the band width for bars
for i, temp in enumerate(temperatures):
    plt.text(temp, i, str(temp), va='center')

# Change the topic, headline and data type of the chart
plt.xlabel('Average Temperature (°C)')
plt.title('Average City Temperatures Around the World')
plt.xlim(0, max(temperatures) + 5)  # Adjust the x-axis to fit the text

# Show the plot
plt.show()