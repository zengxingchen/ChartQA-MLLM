
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
stress_level = [
    90, 89, 88, 87, 86, 85, 84, 83, 82, 81,
    80, 79, 78, 77, 76, 75, 74, 73, 72, 71,
    70, 69, 68, 67, 66, 65, 64, 63, 62, 61
]

# Create the plot
plt.figure(figsize=(16, 10))  # Change the size of the chart
plt.plot(days, stress_level, marker='s', color="#FF4500", linewidth=2)  # Change color and add markers

# Annotations
for i, level in enumerate(stress_level):
    plt.annotate(level, (days[i], level), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#1E90FF")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Day')
plt.ylabel('Stress Level')
plt.title('Daily Stress Level Over a Month', pad=20, fontsize=14)
plt.grid(True)

# Show the plot
plt.show()