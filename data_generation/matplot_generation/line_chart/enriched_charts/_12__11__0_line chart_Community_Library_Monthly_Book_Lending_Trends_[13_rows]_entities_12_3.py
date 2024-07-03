
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
exercise_duration = [
    30, 32, 31, 35, 34, 36, 33, 37, 39, 38,
    40, 42, 41, 43, 45, 44, 46, 48, 47, 49,
    50, 52, 51, 53, 55, 54, 56, 58, 57, 60
]

# Create the plot
plt.figure(figsize=(16, 10))  # Change the size of the chart
plt.plot(days, exercise_duration, marker='o', color="#FF5733", linewidth=2)  # Change color and add markers

# Annotations
for i, duration in enumerate(exercise_duration):
    plt.annotate(duration, (days[i], duration), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#1D8348")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Day')
plt.ylabel('Exercise Duration (minutes)')
plt.title('Daily Exercise Duration Over a Month', pad=20)
plt.grid(True)

# Show the plot
plt.show()