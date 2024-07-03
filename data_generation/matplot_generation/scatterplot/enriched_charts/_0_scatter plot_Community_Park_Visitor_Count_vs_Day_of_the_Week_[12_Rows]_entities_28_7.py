
import matplotlib.pyplot as plt

# Data
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "Seattle",
    "Denver", "Washington", "Boston", "San Jose", "Austin"
]
temperatures = [5, 16, 7, 18, 20, 7, 16, 15, 15, 8, 7, 7, 5, 14, 16]
rainfall = [75, 50, 70, 90, 25, 80, 65, 40, 80, 115, 40, 70, 90, 50, 75]

# Scatter plot
fig, ax = plt.subplots(figsize=(12, 6))  # Change the width and height of the chart
scatter = ax.scatter(
    temperatures,
    rainfall,
    alpha=0.7,
    c=[
        '#FF6347', '#4682B4', '#FFA07A', '#20B2AA', '#8470FF',
        '#FF69B4', '#8A2BE2', '#00FA9A', '#CD3333', '#FF4500',
        '#DA70D6', '#1E90FF', '#32CD32', '#800080', '#40E0D0'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Average Monthly Temperature vs Average Monthly Rainfall')
ax.set_xlabel('Average Temperature (°C)')
ax.set_ylabel('Average Monthly Rainfall (mm)')

# Adding the city names as labels next to each point
for i, city in enumerate(cities):
    ax.annotate(city, (temperatures[i], rainfall[i]), fontsize=8)

plt.show()