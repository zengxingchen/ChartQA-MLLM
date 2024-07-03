
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Bangkok', 'Moscow',
          'Dubai', 'Istanbul', 'Lagos', 'Paris', 'Jakarta', 'London',
          'Hanoi', 'Buenos Aires', 'Sydney', 'Toronto', 'Berlin', 'Madrid',
          'Rome', 'Seoul', 'Kuala Lumpur', 'Cape Town', 'Santiago', 'Singapore']
temperatures = [16, 25, 16, 19, 27, 17, 12, 17, 22, 13, 29, 4,
                28, 15, 27, 12, 27, 11, 24, 18, 21, 9, 10, 14,
                20, 18, 30, 22, 16, 27]

# Modify the color scheme using specific color codes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4']

# Change width of bars
bar_width = 0.4

# Change width and height of the chart
plt.figure(figsize=(14, 10))

# Change the direction of chart (vertical bar chart)
plt.bar(x=cities, height=temperatures, color=colors, width=bar_width)

# Change the band width for bars
for i, temp in enumerate(temperatures):
    plt.text(i, temp + 0.5, str(temp), ha='center')

# Change the topic, headline and data type of the chart
plt.ylabel('Average Temperature (°C)')
plt.title('Average City Temperatures Around the World')
plt.ylim(0, max(temperatures) + 5)  # Adjust the y-axis to fit the text
plt.xticks(rotation=90)

# Show the plot
plt.show()