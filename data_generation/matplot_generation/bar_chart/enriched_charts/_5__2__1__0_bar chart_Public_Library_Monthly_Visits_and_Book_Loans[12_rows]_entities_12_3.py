
import matplotlib.pyplot as plt

# Data for the chart
destinations = ['Paris', 'London', 'New York', 'Tokyo', 'Sydney', 
                'Dubai', 'Rome', 'Barcelona', 'Amsterdam', 'Bangkok', 
                'Singapore', 'Istanbul', 'Los Angeles', 'Berlin', 'Vienna',
                'Madrid', 'Milan', 'Seoul', 'Hong Kong', 'Toronto']
expenditure = [1200, 1150, 1300, 900, 800, 
               1100, 950, 700, 650, 750, 
               1050, 600, 1250, 700, 850,
               950, 980, 920, 870, 1000]

# Setting colors for each bar
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', 
          '#FF4500', '#1E90FF', '#ADFF2F', '#FF69B4', '#FFA500', 
          '#20B2AA', '#778899', '#8B4513', '#708090', '#CD5C5C',
          '#40E0D0', '#EE82EE', '#8A2BE2', '#5F9EA0', '#D2691E']

# Increase the width and height of the chart
plt.figure(figsize=(14, 10))

# Change the direction of the chart to vertical and modify the bar width
plt.bar(destinations, expenditure, color=colors, width=0.6)

# Customizing the chart with titles and labels
plt.ylabel('Travel Expenditure (USD per person per year)')
plt.title('Annual Travel Expenditure in Various Destinations')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Truncate y-axis to start from a specific value
plt.ylim(500, 1400)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the bar chart
plt.show()