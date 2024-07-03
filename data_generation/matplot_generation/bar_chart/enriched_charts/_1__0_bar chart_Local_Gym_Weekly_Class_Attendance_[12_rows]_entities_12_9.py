
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Bangkok', 'Moscow',
          'Dubai', 'Istanbul', 'Lagos', 'Paris', 'Jakarta', 'London',
          'Hanoi', 'Buenos Aires', 'Cape Town', 'Sydney', 'Rio de Janeiro',
          'Los Angeles', 'Toronto']
rainfall = [1530, 800, 1160, 1450, 2200, 750, 600, 1300, 20, 1200, 1650, 700,
            100, 820, 1600, 640, 2000, 690, 1800, 1200, 600, 1200, 1170, 380, 830]

# Modify the color scheme using specific color codes
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6',
          '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845',
          '#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F',
          '#581845', '#DAF7A6', '#FFC300', '#FF5733', '#C70039',
          '#900C3F', '#581845', '#DAF7A6', '#FFC300', '#FF5733']

# Change width of bars
bar_width = 0.7

# Change width and height of the chart
plt.figure(figsize=(12, 10))

# Change the direction of chart (vertical bar chart)
plt.bar(x=cities, height=rainfall, color=colors, width=bar_width)

# Change the band width for bars
for i, rain in enumerate(rainfall):
    plt.text(i, rain + 20, str(rain), ha='center')

# Change the topic, headline, and data type of the chart
plt.ylabel('Average Annual Rainfall (mm)')
plt.title('Average Annual Rainfall in Cities Around the World')
plt.ylim(0, max(rainfall) + 200)  # Adjust the y-axis to fit the text
plt.xticks(rotation=90)  # Rotate city names for better readability

# Show the plot
plt.tight_layout()
plt.show()