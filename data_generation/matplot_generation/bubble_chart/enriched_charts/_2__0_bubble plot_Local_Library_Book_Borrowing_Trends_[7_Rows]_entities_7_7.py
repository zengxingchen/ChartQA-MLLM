
import matplotlib.pyplot as plt

# Data
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
          "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
          "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
          "Detroit", "El Paso", "Seattle", "Denver", "Washington D.C.",
          "Boston", "Nashville", "Oklahoma City", "Las Vegas", "Portland"]
population = [8419000, 3980000, 2716000, 2328000, 1690000, 
              1584000, 1547000, 1424000, 1341000, 1035000, 
              993000, 903000, 902000, 898000, 873000,
              670000, 681000, 745000, 727000, 705000,
              692000, 693000, 655000, 651000, 653000]
internet_users = [7890000, 3500000, 2500000, 2100000, 1600000, 
                  1450000, 1400000, 1300000, 1250000, 980000, 
                  900000, 820000, 810000, 800000, 780000,
                  600000, 620000, 690000, 670000, 650000,
                  640000, 650000, 610000, 600000, 610000]

# Bubble sizes - magnify the internet users for better visibility in the chart
sizes = [users * 0.001 for users in internet_users]

# Bubble colors - use a color gradient related to the population values
colors = ['#00BFFF' if pop < 1000000 else '#32CD32' if pop < 5000000 else '#FF4500' for pop in population]

# Plot
fig, ax = plt.subplots(figsize=(16, 10))
bubble = ax.scatter(population, cities, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

# Chart title and labels
ax.set_title('Internet Users vs Population in Major US Cities', fontsize=18, pad=20)
ax.set_xlabel('Population', fontsize=14)
ax.set_ylabel('Cities', fontsize=14)

# Show grid
ax.grid(True)

# Add legend for size (internet users)
for users in sorted(set(internet_users), reverse=True):
    ax.scatter([], [], c='k', alpha=0.3, s=users * 0.001, label=str(users) + ' users')
ax.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Internet Users', loc='lower right')

# Show plot
plt.tight_layout()
plt.show()