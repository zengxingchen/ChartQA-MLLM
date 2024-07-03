
import matplotlib.pyplot as plt

# Define data
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia",
    "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville",
    "Fort Worth", "Columbus", "Charlotte"
]

population = [
    8419000, 3980000, 2706000, 2323000, 1686000, 1584000, 1547000, 1422000,
    1343000, 1027000, 993000, 902000, 874000, 889000, 872000
]

area = [
    789, 1214, 606, 1707, 1340, 347, 1360, 964, 882, 469, 1226, 2265, 909, 579, 796
]

average_temperature = [
    10.2, 17.1, 11.7, 20.8, 23.9, 12.2, 20.9, 16.7, 18.9, 15.2, 20.4, 21.8, 18.6, 12.3, 15.9
]

# Create a figure with specified width and height
fig, ax = plt.subplots(figsize=(14, 8))

# Bubble sizes as a fraction of area (adjust the scaling as needed)
sizes = [area[i] / 2 for i in range(len(area))]

# Scatter plot (using population as weight for bubble size)
scatter = ax.scatter(
    population, average_temperature, s=sizes, alpha=0.6,
    color=['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3333',
           '#FF33FF', '#57FFC8', '#FFC857', '#33FFFA', '#DD33FF',
           '#3FFFA5', '#A53FFF', '#3FA5FF', '#FFA53F', '#FF3FA5']
)

# Customize the appearance
ax.set_title('City Populations, Land Areas, and Average Temperatures')
ax.set_xlabel('Population')
ax.set_ylabel('Average Temperature (°C)')
ax.grid(True)

# Adding the names of the cities to the bubbles
for i, txt in enumerate(cities):
    ax.annotate(txt, (population[i], average_temperature[i]))

plt.show()