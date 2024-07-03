
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
revenue_thousands = [
    120, 135, 140, 150, 165, 170, 180, 175, 160, 155, 145, 130
]

# Create the plot
plt.figure(figsize=(16, 8))  # Change the size of the chart
plt.plot(months, revenue_thousands, marker='o', color="#FF5733", linewidth=2)  # Change color and add circle markers

# Annotations
for i, revenue in enumerate(revenue_thousands):
    plt.annotate(revenue, (months[i], revenue), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#C70039")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Month')
plt.ylabel('Revenue (in thousands)')
plt.title('Monthly Revenue Over a Year', pad=20)
plt.grid(True)
plt.gca().invert_yaxis()  # Invert the y-axis

# Show the plot
plt.show()