import matplotlib.pyplot as plt

# Data for the chart
destinations = ['Paris', 'London', 'New York', 'Tokyo', 'Sydney', 
                'Dubai', 'Rome', 'Barcelona', 'Amsterdam', 'Bangkok', 
                'Singapore', 'Istanbul', 'Los Angeles', 'Berlin', 'Vienna',
                'Venice', 'Prague', 'Madrid', 'Munich', 'Athens',
                'Budapest', 'Lisbon', 'Moscow', 'Copenhagen', 'Dublin',
                'Warsaw', 'Helsinki', 'Oslo', 'Zurich', 'Stockholm',
                'Edinburgh']
expenditure = [1200, 1150, 1300, 900, 800, 
               1100, 950, 700, 650, 750, 
               1050, 600, 1250, 700, 850,
               880, 780, 920, 810, 850,
               670, 760, 890, 710, 750,
               620, 640, 720, 950, 800,
               780]

# Setting colors for each bar
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', 
          '#FF4500', '#1E90FF', '#ADFF2F', '#FF69B4', '#FFA500', 
          '#20B2AA', '#778899', '#8B4513', '#708090', '#CD5C5C',
          '#E9967A', '#8FBC8F', '#2E8B57', '#B22222', '#FF8C00',
          '#8A2BE2', '#9932CC', '#FFD700', '#FF4500', '#1E90FF',
          '#ADFF2F', '#FF69B4', '#FFA500', '#20B2AA', '#778899',
          '#8B4513']

# Increase the width and height of the chart
plt.figure(figsize=(16, 10))

# Change the direction of the chart to vertical and modify the bar width
plt.bar(destinations, expenditure, color=colors, width=0.7)

# Customizing the chart with titles and labels
plt.ylabel('Travel Expenditure (USD per person per year)')
plt.title('Annual Travel Expenditure in Various Destinations', pad=20)
plt.xticks(rotation=90)
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)

# Display the bar chart
plt.tight_layout()
plt.show()