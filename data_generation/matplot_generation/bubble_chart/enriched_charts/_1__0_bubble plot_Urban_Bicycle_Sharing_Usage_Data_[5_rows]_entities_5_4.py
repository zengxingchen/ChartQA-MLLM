
import matplotlib.pyplot as plt

# Define data points
cities = ['Paris', 'London', 'Rome', 'New York', 'Tokyo', 'Bangkok', 'Sydney', 'Dubai', 'Singapore', 'Hong Kong', 'Los Angeles', 'Barcelona', 'Istanbul', 'Amsterdam', 'Berlin', 'Cape Town', 'Toronto', 'Rio de Janeiro', 'Moscow', 'Dubai']
avg_rainfall = [53, 47, 60, 98, 105, 150, 86, 10, 178, 156, 26, 72, 85, 66, 45, 52, 77, 101, 70, 10]
avg_temp = [15.5, 14.3, 18.1, 12.6, 16.2, 28.2, 18.5, 28.9, 27.8, 24.0, 18.3, 17.8, 15.2, 12.3, 10.2, 17.3, 9.1, 25.1, 5.4, 28.9]
tourist_arrivals = [17.44, 19.10, 10.32, 13.40, 13.98, 22.67, 9.23, 16.33, 18.50, 9.03, 9.50, 9.09, 14.72, 9.72, 7.23, 1.93, 4.97, 2.33, 5.82, 16.33]  # in millions

# Normalize tourist arrivals for bubble sizes
size_factor = 70
sizes = [p * size_factor for p in tourist_arrivals]

# Define colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Create the plot
plt.figure(figsize=(16,12))
plt.scatter(avg_rainfall, avg_temp, s=sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=0.5)

# Create labels and title
plt.title('Average Rainfall vs. Average Temperature with Tourist Arrivals Bubble Sizes', pad=20)
plt.xlabel('Average Monthly Rainfall (mm)')
plt.ylabel('Average Temperature (°C)')

# Add city labels to the bubbles
for i, city in enumerate(cities):
    plt.text(avg_rainfall[i], avg_temp[i], city, ha='center', va='center', fontsize=8)

# Show the plot
plt.tight_layout()
plt.show()