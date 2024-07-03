
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
arrivals = [10000, 12000, 15000, 20000, 25000, 35000, 45000, 44000, 38000, 30000, 18000, 12000]

# Creating the line chart
plt.figure(figsize=(12, 6))

plt.plot(months, arrivals, color="#4682B4", marker='o')  # Using a specific color code

# Annotating the highest and lowest arrivals
plt.annotate('Highest\n45000', xy=("July", 45000), xytext=("July", 47000),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), ha='center')
plt.annotate('Lowest\n10000', xy=("January", 10000), xytext=("January", 8000),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Tourist Arrivals", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Number of Arrivals", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.6, color='grey')

# Show the plot
plt.show()