
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Bangkok', 'Moscow',
          'Dubai', 'Istanbul', 'Lagos', 'Paris', 'Jakarta', 'London',
          'Hanoi', 'Buenos Aires', 'Cape Town', 'Sydney', 'Rio de Janeiro',
          'Los Angeles', 'Toronto']
rainfall = [1530, 900, 1160, 1450, 2300, 850, 700, 1300, 30, 1250, 1700, 800,
            150, 920, 1650, 740, 2100, 750, 1900, 1250, 700, 1250, 1220, 450, 930]

# Modify the color scheme using specific color codes
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6',
          '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845',
          '#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F',
          '#581845', '#DAF7A6', '#FFC300', '#FF5733', '#C70039',
          '#900C3F', '#581845', '#DAF7A6', '#FFC300', '#FF5733']

# Change width of bars
bar_width = 0.6

# Change width and height of the chart
plt.figure(figsize=(14, 8))

# Change the direction of chart (horizontal bar chart)
plt.barh(y=cities, width=rainfall, color=colors, height=bar_width)

# Change the band height for bars
for i, rain in enumerate(rainfall):
    plt.text(rain + 20, i, str(rain), va='center')

# Change the topic, headline, and data type of the chart
plt.xlabel('Average Annual Rainfall (mm)')
plt.title('Rainfall in Major Cities Around the World')
plt.xlim(0, max(rainfall) + 200)  # Adjust the x-axis to fit the text

# Set the y-axis limits to truncate the chart
plt.ylim(0, len(cities))  # Adjust the y-axis to fit the text

# Show the plot
plt.tight_layout()
plt.show()