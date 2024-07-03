
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
happiness_index = [
    60, 62, 64, 63, 65, 67, 66, 68, 70, 72,
    71, 73, 75, 74, 76, 78, 77, 79, 81, 80,
    82, 84, 83, 85, 87, 86, 88, 90, 89, 91
]

# Create the plot
plt.figure(figsize=(14, 8))  # Change the size of the chart
plt.plot(days, happiness_index, marker='o', color="#4B0082", linewidth=2)  # Change color and add markers

# Annotations
for i, index in enumerate(happiness_index):
    plt.annotate(index, (days[i], index), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#32CD32")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Day')
plt.ylabel('Happiness Index')
plt.title('Daily Happiness Index Over a Month', pad=20)
plt.grid(True)

# Show the plot
plt.show()