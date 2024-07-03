
import matplotlib.pyplot as plt

# Data
data = [
    {'City': 'New York', 'Number of Trips (in millions)': 550, 'Average Trip Length (km)': 10, 'Population (in millions)': 8.399},
    {'City': 'Tokyo', 'Number of Trips (in millions)': 800, 'Average Trip Length (km)': 9, 'Population (in millions)': 9.273},
    {'City': 'Berlin', 'Number of Trips (in millions)': 250, 'Average Trip Length (km)': 12, 'Population (in millions)': 3.644},
    {'City': 'London', 'Number of Trips (in millions)': 500, 'Average Trip Length (km)': 13, 'Population (in millions)': 8.982},
    {'City': 'Paris', 'Number of Trips (in millions)': 300, 'Average Trip Length (km)': 11, 'Population (in millions)': 2.141}
]

# Extracting data for plotting
cities = [item['City'] for item in data]
trips = [item['Number of Trips (in millions)'] for item in data]
trip_lengths = [item['Average Trip Length (km)'] for item in data]
populations = [item['Population (in millions)'] for item in data]

# Bubble sizes, scale population for better visualization
bubble_sizes = [pop * 70 for pop in populations]

# Create a bubble chart
fig, ax = plt.subplots()

# Scatter plot, with the bubble sizes and also add color variation
scatter = ax.scatter(trips, trip_lengths, s=bubble_sizes, alpha=0.5, c=populations, cmap='viridis', edgecolor='black', linewidth=1)

# Title and labels
ax.set_title('City Trip Data')
ax.set_xlabel('Number of Trips (in millions)')
ax.set_ylabel('Average Trip Length (km)')

# Adding city names as annotations
for i, city in enumerate(cities):
    ax.annotate(city, (trips[i], trip_lengths[i]))

# Add a color bar which maps values to colors.
cbar = plt.colorbar(scatter, shrink=0.5)
cbar.set_label('Population (in millions)')

# Show the plot
plt.show()