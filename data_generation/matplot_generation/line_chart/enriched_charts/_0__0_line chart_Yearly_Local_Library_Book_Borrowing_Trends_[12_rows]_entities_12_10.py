
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
rainfall = [78, 65, 92, 105, 120, 135, 160, 145, 130, 115, 95, 85]

# Creating the line chart
plt.figure(figsize=(12, 6))

plt.plot(months, rainfall, color="#4682B4", marker='s')

# Annotating the highest and lowest rainfall
plt.annotate('Highest\n160mm', xy=("July", 160), xytext=("July", 170),
             arrowprops=dict(facecolor='#DC143C', shrink=0.05), ha='center')
plt.annotate('Lowest\n65mm', xy=("February", 65), xytext=("February", 55),
             arrowprops=dict(facecolor='#1E90FF', shrink=0.05), ha='center')

# Title and labels
plt.title("Average Monthly Rainfall in a Year", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Rainfall (mm)", fontsize=12)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.7, color='grey')

# Show the plot
plt.show()