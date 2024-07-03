
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
avg_temperatures = [
    5, 6, 10, 14, 18, 22, 26, 25, 20, 15, 10, 6
]

# Create the plot
plt.figure(figsize=(12, 6))  # Change the size of the chart
plt.plot(months, avg_temperatures, marker='o', color="#FF5733", linewidth=2)  # Change color and add markers

# Annotations
for i, temp in enumerate(avg_temperatures):
    plt.annotate(temp, (months[i], temp), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#337AB7")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Monthly Temperatures in a City')
plt.grid(True)

# Show the plot
plt.show()