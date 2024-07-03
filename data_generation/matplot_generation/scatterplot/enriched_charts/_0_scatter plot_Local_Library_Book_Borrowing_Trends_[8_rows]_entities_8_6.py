
import matplotlib.pyplot as plt

# Data for scatterplot
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
average_temperature_celsius = [5, 7, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6]
number_of_visitors_thousands = [30, 35, 40, 50, 70, 90, 100, 95, 80, 65, 50, 35]

# Size of each point will be proportional to the number of visitors
sizes = [visitors * 10 for visitors in number_of_visitors_thousands]

# Different colors for different temperatures (cooler to warmer)
colors = ['#6495ED', '#7BB8FA', '#89CFF0', '#9ACD32', '#CCCC4D', '#FFD700',
          '#FFA500', '#FF8C00', '#FF7F50', '#F08080', '#CD5C5C', '#8B0000']

# Create scatterplot
plt.figure(figsize=(12, 8))  # increase the width and height of the chart
plt.scatter(months, average_temperature_celsius, s=sizes, c=colors, alpha=0.7)

# Chart details
plt.title('Park Visitors and Average Temperature Over a Year')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.grid(True)

# Show the chart
plt.show()