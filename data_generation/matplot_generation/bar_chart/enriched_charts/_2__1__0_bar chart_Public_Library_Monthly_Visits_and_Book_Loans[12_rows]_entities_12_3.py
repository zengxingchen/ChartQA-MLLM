
import matplotlib.pyplot as plt

# Data for the chart
destinations = ['Paris', 'London', 'New York', 'Tokyo', 'Sydney', 
                'Dubai', 'Rome', 'Barcelona', 'Amsterdam', 'Bangkok', 
                'Singapore', 'Istanbul', 'Los Angeles', 'Berlin', 'Vienna']
expenditure = [1200, 1150, 1300, 900, 800, 
               1100, 950, 700, 650, 750, 
               1050, 600, 1250, 700, 850]

# Setting colors for each bar
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', 
          '#FF4500', '#1E90FF', '#ADFF2F', '#FF69B4', '#FFA500', 
          '#20B2AA', '#778899', '#8B4513', '#708090', '#CD5C5C']

# Increase the width and height of the chart
plt.figure(figsize=(12, 8))

# Change the direction of the chart to horizontal and modify the bar width
plt.barh(destinations, expenditure, color=colors, height=0.6)

# Customizing the chart with titles and labels
plt.xlabel('Travel Expenditure (USD per person per year)')
plt.title('Annual Travel Expenditure in Various Destinations')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Display the bar chart
plt.show()