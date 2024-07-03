
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
innovation_index = [
    45, 48, 50, 52, 55, 60, 62, 65, 70, 75, 78, 80
]

# Create the plot
plt.figure(figsize=(14, 10))  # Change the size of the chart
plt.plot(months, innovation_index, marker='s', color="#2E8B57", linewidth=2)  # Change color and add markers

# Annotations
for i, index in enumerate(innovation_index):
    plt.annotate(f"{index}%", (months[i], index), textcoords="offset points", xytext=(0, 10),
                 ha='center', color="#DC143C")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Month')
plt.ylabel('Innovation Index (%)')
plt.title('Monthly Innovation Index in Future Technologies', pad=20)
plt.grid(True)
plt.gca().invert_yaxis()  # Invert the y-axis

# Show the plot
plt.show()