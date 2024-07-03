
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Mexico City',
          'Beijing', 'Osaka', 'Cairo', 'New York', 'Bangkok', 'Moscow',
          'Dubai', 'Istanbul', 'Lagos', 'Paris', 'Jakarta', 'London',
          'Hanoi', 'Buenos Aires', 'Cape Town', 'Sydney', 'Rio de Janeiro',
          'Los Angeles', 'Toronto', 'Seoul', 'Madrid', 'Singapore',
          'San Francisco', 'Auckland', 'Hong Kong', 'Melbourne', 'Rome']
rainfall = [1530, 800, 1160, 1450, 2200, 750, 600, 1300, 20, 1200, 1650, 700,
            100, 820, 1600, 640, 2000, 690, 1800, 1200, 600, 1200, 1170, 380,
            830, 1500, 400, 1800, 500, 1100, 2200, 800, 900]

# Modify the color scheme using specific color codes
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6',
          '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845',
          '#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F',
          '#581845', '#DAF7A6', '#FFC300', '#FF5733', '#C70039',
          '#900C3F', '#581845', '#DAF7A6', '#FFC300', '#FF5733',
          '#C70039', '#900C3F', '#581845', '#DAF7A6', '#FFC300',
          '#FF5733', '#C70039', '#900C3F']

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
plt.title('Average Annual Rainfall in Various Cities Around the World')
plt.xlim(0, max(rainfall) + 200)  # Adjust the x-axis to fit the text

# Truncate the y-axis to start from a specific value other than zero
plt.ylim(10, len(cities) - 1)

# Show the plot
plt.tight_layout()
plt.show()