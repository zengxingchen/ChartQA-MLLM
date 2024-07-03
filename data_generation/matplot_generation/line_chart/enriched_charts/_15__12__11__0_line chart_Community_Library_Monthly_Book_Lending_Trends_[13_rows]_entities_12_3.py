
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
revenue = [
    60, 59, 57, 58, 55, 53, 52, 50, 49, 47,
    45, 44, 42, 41, 39, 38, 37, 36, 34, 33,
    31, 30, 28, 27, 26, 24, 23, 22, 21, 20
]

# Create the plot
plt.figure(figsize=(14, 8))
plt.plot(days, revenue, marker='o', color="#1f77b4", linewidth=2)

# Annotations
for i, rev in enumerate(revenue):
    plt.annotate(rev, (days[i], rev), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#ff7f0e")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Day')
plt.ylabel('Revenue (Thousands)')
plt.title('Daily Revenue Over a Month', pad=20)
plt.gca().invert_yaxis()
plt.grid(True)

# Show the plot
plt.show()