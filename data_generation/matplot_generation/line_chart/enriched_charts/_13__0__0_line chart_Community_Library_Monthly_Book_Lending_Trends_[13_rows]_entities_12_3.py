
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
calories = [
    2000, 2100, 2050, 2200, 2250, 2150, 2300, 2350, 2250, 2400,
    2450, 2350, 2500, 2550, 2450, 2600, 2650, 2550, 2700, 2750,
    2650, 2800, 2850, 2750, 2900, 2950, 2850, 3000, 3050, 2950
]

# Create the plot
plt.figure(figsize=(16, 8))  # Change the size of the chart
plt.plot(days, calories, marker='o', color="#FF6347", linewidth=2)  # Change color and add markers

# Annotations
for i, cal in enumerate(calories):
    plt.annotate(f"{cal} kcal", (days[i], cal), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#4682B4")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Day')
plt.ylabel('Calories Intake (kcal)')
plt.title('Daily Calorie Intake for a Month')
plt.grid(True)

# Invert y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()