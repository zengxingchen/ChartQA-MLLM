
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Bangkok', 'Moscow',
          'Dubai', 'Istanbul', 'Lagos', 'Paris', 'Jakarta', 'London',
          'Hanoi', 'Buenos Aires', 'Sydney', 'Toronto', 'Berlin', 'Madrid',
          'Rome', 'Seoul', 'Kuala Lumpur', 'Cape Town', 'Santiago', 'Singapore',
          'San Francisco', 'Rio de Janeiro', 'Chicago', 'Vancouver', 'Athens']
temperatures = [16, 25, 16, 19, 27, 17, 12, 17, 22, 13, 29, 4,
                28, 15, 27, 12, 27, 11, 24, 18, 21, 9, 10, 14,
                20, 18, 30, 22, 16, 27, 18, 26, 8, 7, 19]

# Modify the color scheme using specific color codes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Change width of bars
bar_width = 0.6

# Change width and height of the chart
plt.figure(figsize=(12, 16))

# Change the direction of chart to horizontal bar chart
plt.barh(y=cities, width=temperatures, color=colors, height=bar_width)

# Change the band height for bars
for i, temp in enumerate(temperatures):
    plt.text(temp + 0.5, i, str(temp), va='center')

# Change the topic, headline, and data type of the chart
plt.xlabel('Average Temperature (°C)')
plt.title('Average City Temperatures for Travel & Adventure')
plt.xlim(min(temperatures) - 5, max(temperatures) + 5)  # Adjust the x-axis to fit the text

# Show the plot
plt.show()