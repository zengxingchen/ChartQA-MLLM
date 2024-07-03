
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
stars_observed = [5, 7, 9, 10, 12, 15, 18, 20, 23, 25, 28, 30, 32, 35, 37, 40, 42, 45, 47, 50, 52, 55, 57, 60, 63, 65, 68, 70, 73, 75, 78, 80, 82, 85, 87, 90, 92, 95, 97, 100]
new_planets_discovered = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20]

# Create a scatterplot
plt.figure(figsize=(16, 12))
plt.scatter(days, stars_observed, c="#3498DB", label="Stars Observed")
plt.scatter(days, new_planets_discovered, c="#E74C3C", label="New Planets Discovered")

# Customize the chart
plt.title("Astronomy Observations Over Time", pad=20)
plt.xlabel("Days of Observation")
plt.ylabel("Count")
plt.legend(loc='upper right')
plt.grid(True)

# Show the scatterplot
plt.show()