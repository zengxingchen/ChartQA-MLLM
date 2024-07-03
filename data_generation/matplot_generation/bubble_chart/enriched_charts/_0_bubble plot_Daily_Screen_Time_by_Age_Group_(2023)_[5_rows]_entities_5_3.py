
import matplotlib.pyplot as plt

# Data for cities, temperature, humidity, and population
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston',
          'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 
          'Dallas', 'San Jose', 'Austin', 'Jacksonville', 
          'Fort Worth', 'Columbus', 'Charlotte']

average_temperature = [16, 17, 11, 20, 23,
                       15, 22, 18, 19, 17,
                       21, 22, 20, 14, 19]

humidity = [65, 63, 75, 80, 45, 69, 60, 70, 65, 63,
            70, 74, 64, 70, 65]

population = [8419000, 3971000, 2706000, 2326000, 1663000,
              1584000, 1547000, 1426000, 1343000, 1027000,
              993000, 912000, 902000, 889000, 885000]

# Normalizing the population size to be suitable for the bubble size
bubble_size = [p / 1000 for p in population]

# Creating the bubble chart
plt.figure(figsize=(12, 8))
for i in range(len(cities)):
    plt.scatter(average_temperature[i],
                humidity[i],
                s=bubble_size[i],  # Bubble sizes
                alpha=0.5,
                label=f'{cities[i]}', # Label for hover
                c=f'#{hex(255 - i * 15 % 255)[2:].ljust(2,"0")}{hex(i * 15 % 255)[2:].ljust(2,"0")}ff')  # Unique color for each city

# Chart title and labels
plt.title('Average Temperature, Humidity, and Population of U.S. Cities')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Humidity (%)')

# Adding legend with just the city names
plt.legend(loc='upper left', title='Cities')

# Show the plot
plt.show()