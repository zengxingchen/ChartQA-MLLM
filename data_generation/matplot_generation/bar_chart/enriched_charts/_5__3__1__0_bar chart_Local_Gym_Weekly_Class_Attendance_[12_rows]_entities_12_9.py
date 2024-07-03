
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Bangkok', 'Moscow',
          'Dubai', 'Istanbul', 'Lagos', 'Paris', 'Jakarta', 'London',
          'Hanoi', 'Buenos Aires', 'Cape Town', 'Sydney', 'Rio de Janeiro',
          'Los Angeles', 'Toronto', 'Berlin', 'Madrid', 'Rome', 'Lisbon']
coffee_consumption = [3.4, 0.6, 2.5, 5.8, 0.7, 1.2, 2.0, 3.1, 0.3, 4.5, 0.9, 4.2,
                      1.5, 2.3, 0.5, 5.0, 1.0, 3.8, 0.8, 4.0, 2.6, 3.6, 5.2, 3.9, 
                      4.1, 4.3, 2.7, 3.0, 2.9]

# Modify the color scheme using specific color codes
colors = ['#1F618D', '#117A65', '#76448A', '#7D3C98', '#C0392B',
          '#F1C40F', '#2980B9', '#D68910', '#16A085', '#7FB3D5',
          '#B9770E', '#2980B9', '#27AE60', '#CA6F1E', '#8E44AD',
          '#27AE60', '#D4AC0D', '#2980B9', '#2E4053', '#D35400',
          '#884EA0', '#76448A', '#7D3C98', '#F1C40F', '#5DADE2',
          '#E67E22', '#48C9B0', '#EC7063', '#AF7AC5', '#52BE80']

# Change width of bars
bar_width = 0.7

# Change width and height of the chart
plt.figure(figsize=(10, 16))

# Change the direction of chart (vertical bar chart)
plt.bar(x=cities, height=coffee_consumption, color=colors, width=bar_width)

# Add text labels to bars
for i, coffee in enumerate(coffee_consumption):
    plt.text(i, coffee + 0.1, str(coffee), ha='center')

# Change the topic, headline, and data type of the chart
plt.ylabel('Average Annual Coffee Consumption (kg per capita)')
plt.title('Coffee Consumption in Major Cities')

# Set y-axis limits to start from a specific value
plt.ylim(0.5, max(coffee_consumption) + 1)  # Starting y-axis from 0.5

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.tight_layout()
plt.show()