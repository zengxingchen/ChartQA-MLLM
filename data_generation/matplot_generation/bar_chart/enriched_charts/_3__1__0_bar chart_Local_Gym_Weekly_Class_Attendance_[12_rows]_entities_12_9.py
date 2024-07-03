
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Bangkok', 'Moscow',
          'Dubai', 'Istanbul', 'Lagos', 'Paris', 'Jakarta', 'London',
          'Hanoi', 'Buenos Aires', 'Cape Town', 'Sydney', 'Rio de Janeiro',
          'Los Angeles', 'Toronto']
coffee_consumption = [3.4, 0.6, 2.5, 5.8, 0.7, 1.2, 2.0, 3.1, 0.3, 4.5, 0.9, 4.2,
                      1.5, 2.3, 0.5, 5.0, 1.0, 3.8, 0.8, 4.0, 2.6, 3.6, 5.2, 3.9, 4.1]

# Modify the color scheme using specific color codes
colors = ['#A93226', '#884EA0', '#2471A3', '#17A589', '#229954',
          '#D4AC0D', '#CA6F1E', '#CD6155', '#AF7AC5', '#5499C7',
          '#48C9B0', '#52BE80', '#F4D03F', '#DC7633', '#EC7063',
          '#BB8FCE', '#5DADE2', '#76D7C4', '#58D68D', '#F7DC6F',
          '#F0B27A', '#F1948A', '#D98880', '#C39BD3', '#7FB3D5']

# Change width of bars
bar_width = 0.5

# Change width and height of the chart
plt.figure(figsize=(14, 8))

# Change the direction of chart (horizontal bar chart)
plt.barh(y=cities, width=coffee_consumption, color=colors, height=bar_width)

# Change the band height for bars
for i, coffee in enumerate(coffee_consumption):
    plt.text(coffee + 0.1, i, str(coffee), va='center')

# Change the topic, headline, and data type of the chart
plt.xlabel('Average Annual Coffee Consumption (kg per capita)')
plt.title('Average Annual Coffee Consumption in Cities Around the World')
plt.xlim(0, max(coffee_consumption) + 1)  # Adjust the x-axis to fit the text

# Show the plot
plt.tight_layout()
plt.show()