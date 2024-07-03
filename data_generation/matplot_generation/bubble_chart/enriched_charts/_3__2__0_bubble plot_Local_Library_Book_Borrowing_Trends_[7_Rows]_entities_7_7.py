
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
books_read = [5000000, 3500000, 2500000, 2000000, 1500000, 
              1400000, 1300000, 1200000, 1100000, 1000000, 
              950000, 900000, 850000, 800000, 750000,
              700000, 650000, 600000, 550000, 500000,
              450000, 400000, 350000, 300000, 250000]

# Bubble sizes - magnify the books read for better visibility in the chart
sizes = [books * 0.001 for books in books_read]

# Bubble colors - use a color gradient related to the population values
colors = ['#FFA07A' if pop < 1000000 else '#20B2AA' if pop < 5000000 else '#8A2BE2' for pop in population]

# Plot
fig, ax = plt.subplots(figsize=(18, 12))
bubble = ax.scatter(population, cities, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

# Chart title and labels
ax.set_title('Books Read vs Population in Major US Cities', fontsize=20, pad=30)
ax.set_xlabel('Population', fontsize=16)
ax.set_ylabel('Cities', fontsize=16)

# Show grid
ax.grid(True)

# Add legend for size (books read)
for books in sorted(set(books_read), reverse=True):
    ax.scatter([], [], c='k', alpha=0.3, s=books * 0.001, label=str(books) + ' books')
ax.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Books Read', loc='upper left')

# Show plot
plt.tight_layout()
plt.show()