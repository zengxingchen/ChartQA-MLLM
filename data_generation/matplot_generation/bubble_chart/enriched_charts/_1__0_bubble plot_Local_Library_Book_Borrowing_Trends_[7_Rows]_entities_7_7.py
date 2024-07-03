
import matplotlib.pyplot as plt

# Data
destinations = [
    "Paris", "London", "Rome", "New York", "Tokyo",
    "Dubai", "Barcelona", "Singapore", "Bangkok", "Istanbul",
    "Hong Kong", "Sydney", "Los Angeles", "Amsterdam", "Berlin",
    "Las Vegas", "Miami", "Vienna", "Madrid", "San Francisco"
]
average_hotel_cost = [
    200, 220, 180, 300, 250,
    350, 190, 280, 150, 140,
    290, 240, 260, 230, 210,
    210, 250, 200, 200, 270
]
annual_visitors = [
    30, 28, 25, 33, 29,
    20, 22, 18, 21, 15,
    27, 10, 24, 12, 13,
    40, 22, 8, 17, 14
]
attractions_index = [
    85, 88, 80, 90, 87,
    95, 78, 92, 75, 70,
    83, 84, 86, 81, 76,
    94, 82, 77, 79, 89
]

# Bubble sizes - magnify the attractions index for better visibility in the chart
sizes = [index * 10 for index in attractions_index]

# Bubble colors - use a gradient related to the average hotel cost
colors = [
    '#FF6347' if cost < 200 else '#FFD700' if cost < 250 else '#32CD32'
    for cost in average_hotel_cost
]

# Plot
fig, ax = plt.subplots(figsize=(16, 10))
bubble = ax.scatter(average_hotel_cost, destinations, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

# Chart title and labels
ax.set_title('Popular Tourist Destinations: Average Hotel Cost vs. Visitor Count', fontsize=18, pad=20)
ax.set_xlabel('Average Hotel Cost (USD)', fontsize=14)
ax.set_ylabel('Destinations', fontsize=14)

# Show grid
ax.grid(True)

# Add legend for size (Attractions Index)
for index in sorted(set(attractions_index), reverse=True):
    ax.scatter([], [], c='k', alpha=0.3, s=index * 10, label=str(index))
ax.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Attractions Index', loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to avoid overlap
plt.tight_layout()
plt.show()