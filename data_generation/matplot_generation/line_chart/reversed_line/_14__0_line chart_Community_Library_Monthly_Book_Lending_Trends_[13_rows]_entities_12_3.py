
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
pollution_levels = [
    35, 30, 25, 20, 15, 12, 10, 15, 20, 25, 30, 35
]

# Create the plot
plt.figure(figsize=(14, 7))  # Change the size of the chart
plt.plot(months, pollution_levels, marker='s', color="#2E86C1", linewidth=3)  # Change color and add markers

# Annotations
for i, level in enumerate(pollution_levels):
    plt.annotate(level, (months[i], level), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#E74C3C")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Month')
plt.ylabel('Pollution Level (AQI)')
plt.title('Monthly Pollution Levels in a City', pad=20)
plt.grid(True)
plt.gca().invert_yaxis()  # Invert y axis

# Show the plot
plt.show()