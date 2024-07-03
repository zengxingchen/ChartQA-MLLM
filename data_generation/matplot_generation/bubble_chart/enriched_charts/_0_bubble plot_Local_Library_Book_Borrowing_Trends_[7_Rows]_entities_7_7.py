
import matplotlib.pyplot as plt

# Data
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
          "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
          "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
          "Detroit", "El Paso", "Seattle", "Denver", "Washington D.C."]
temperatures = [12, 18, 10, 20, 23, 14, 20, 18, 19, 16,
                20, 22, 19, 12, 16, 10, 20, 12, 10, 14]
rainfall = [1200, 500, 950, 1350, 250, 1050, 810, 230, 920, 450,
            840, 1170, 880, 990, 1050, 840, 230, 940, 410, 1000]

# Bubble sizes - magnify the rainfalls for better visibility in the chart
sizes = [rain * 3 for rain in rainfall]

# Bubble colors - use a color gradient related to the temperature values
colors = ['#FFB6C1' if temp < 12 else '#FFFF00' if temp < 18 else '#FFA07A' for temp in temperatures]

# Plot
fig, ax = plt.subplots(figsize=(14, 8))
bubble = ax.scatter(temperatures, cities, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

# Chart title and labels
ax.set_title('Average Annual Temperature and Rainfall in Various Cities', fontsize=16)
ax.set_xlabel('Average Annual Temperature (°C)', fontsize=14)
ax.set_ylabel('Cities', fontsize=14)

# Show grid
ax.grid(True)

# Add legend for size (rainfall)
for rain in sorted(set(rainfall), reverse=True):
    ax.scatter([], [], c='k', alpha=0.3, s=rain*3, label=str(rain) + ' mm')
ax.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Rainfall')

# Show plot
plt.tight_layout()
plt.show()