
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
temperatures = [5, 7, 10, 15, 20, 25, 30, 29, 24, 18, 12, 6]

# Creating the line chart
plt.figure(figsize=(10, 5))  # Modifying width and height of the chart

plt.plot(months, temperatures, color="#FFA07A", marker='o')  # Using a specific color code

# Annotating the highest and lowest temperatures
plt.annotate('Highest\n30°C', xy=("July", 30), xytext=("July", 32),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05), ha='center')
plt.annotate('Lowest\n5°C', xy=("January", 5), xytext=("January", 3),
             arrowprops=dict(facecolor='#6495ED', shrink=0.05), ha='center')

# Title and labels
plt.title("Average Monthly Temperatures in a Year", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Temperature (°C)", fontsize=12)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')

# Show the plot
plt.show()