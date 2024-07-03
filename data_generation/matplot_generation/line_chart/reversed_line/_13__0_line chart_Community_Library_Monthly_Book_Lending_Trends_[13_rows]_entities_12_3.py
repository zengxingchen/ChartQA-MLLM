
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
distance = [
    50, 60, 75, 85, 95, 100, 110, 105, 90, 80, 65, 55
]

# Create the plot
plt.figure(figsize=(14, 8))  # Change the size of the chart
plt.plot(months, distance, marker='s', color="#2E8B57", linewidth=2)  # Change color and add markers

# Annotations
for i, dist in enumerate(distance):
    plt.annotate(dist, (months[i], dist), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#8A2BE2")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Month')
plt.ylabel('Distance (km)')
plt.title('Monthly Running Distance in a Year')
plt.grid(True)

# Show the plot
plt.show()