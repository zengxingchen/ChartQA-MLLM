
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
temperatures = [30, 32, 45, 55, 65, 75, 85, 84, 75, 60, 45, 35]

# Creating the line chart
plt.figure(figsize=(14, 7))

plt.plot(months, temperatures, color="#FF6347", marker='o')  # Using a specific color code

# Annotating the highest and lowest temperatures
plt.annotate('Highest\n85°F', xy=("July", 85), xytext=("July", 90),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), ha='center')
plt.annotate('Lowest\n30°F', xy=("January", 30), xytext=("January", 25),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Average Temperatures", fontsize=18, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Temperature (°F)", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.6, color='grey')

# Show the plot
plt.show()