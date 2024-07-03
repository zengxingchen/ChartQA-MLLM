
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
running_distance = [
    10.5, 10.2, 9.8, 9.6, 9.5, 9.3, 9.1, 8.9, 8.8, 8.6,
    8.4, 8.3, 8.1, 7.9, 7.8, 7.6, 7.4, 7.3, 7.1, 6.9,
    6.8, 6.6, 6.4, 6.2, 6, 5.9, 5.7, 5.5, 5.4, 5.2
]

# Create the plot
plt.figure(figsize=(16, 9))
plt.plot(days, running_distance, marker='o', color="#FF5733", linewidth=2)

# Annotations
for i, distance in enumerate(running_distance):
    plt.annotate(distance, (days[i], distance), textcoords="offset points", xytext=(0, 5), ha='center', color="#1F618D")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Day')
plt.ylabel('Running Distance (km)')
plt.title('Daily Running Distance Over a Month', pad=20)
plt.grid(True)
plt.gca().invert_yaxis()

# Show the plot
plt.show()