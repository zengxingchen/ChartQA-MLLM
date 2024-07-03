
import matplotlib.pyplot as plt

# Data
cities = [
    "Paris", "London", "Rome", "New York", "Tokyo",
    "Dubai", "Barcelona", "Singapore", "Bangkok", "Istanbul",
    "Hong Kong", "Sydney", "Los Angeles", "Amsterdam", "Berlin",
    "Las Vegas", "Miami", "Vienna", "Madrid", "San Francisco"
]
average_rent = [
    3000, 3500, 2500, 4500, 4000,
    4200, 2600, 4700, 2000, 1800,
    4800, 3700, 3800, 3200, 2800,
    2900, 3100, 2700, 2400, 4300
]
population_millions = [
    2.14, 8.98, 2.87, 8.4, 9.27,
    3.3, 1.62, 5.7, 10.5, 15.03,
    7.4, 5.23, 3.99, 0.87, 3.65,
    0.65, 0.47, 1.9, 3.22, 0.88
]
quality_of_life_index = [
    80, 78, 75, 85, 82,
    77, 74, 90, 65, 60,
    88, 83, 79, 81, 76,
    70, 72, 87, 73, 84
]

# Bubble sizes - magnify the quality of life index for better visibility in the chart
sizes = [index * 10 for index in quality_of_life_index]

# Bubble colors - use specific color codes for better clarity
colors = [
    '#FF4500' if rent < 2500 else '#FFD700' if rent < 3500 else '#1E90FF'
    for rent in average_rent
]

# Plot
fig, ax = plt.subplots(figsize=(14, 8))
bubble = ax.scatter(average_rent, cities, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

# Chart title and labels
ax.set_title('Quality of Life vs. Rent in Major Cities', fontsize=18, pad=20)
ax.set_xlabel('Average Rent (USD)', fontsize=14)
ax.set_ylabel('Cities', fontsize=14)

# Show grid
ax.grid(True)

# Add legend for size (Quality of Life Index)
for index in sorted(set(quality_of_life_index), reverse=True):
    ax.scatter([], [], c='k', alpha=0.3, s=index * 10, label=str(index))
ax.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Quality of Life Index', loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to avoid overlap
plt.tight_layout()
plt.show()