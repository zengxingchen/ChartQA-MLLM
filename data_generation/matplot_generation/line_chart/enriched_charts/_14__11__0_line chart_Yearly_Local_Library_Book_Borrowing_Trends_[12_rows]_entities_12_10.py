
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
rainfall = [120, 100, 80, 60, 40, 30, 50, 70, 90, 110, 130, 150]

# Creating the line chart
plt.figure(figsize=(14, 7))

plt.plot(months, rainfall, color="#8A2BE2", marker='o')  # Using a specific color code

# Annotating the highest and lowest rainfall
plt.annotate('Highest\n150 mm', xy=("December", 150), xytext=("December", 170),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), ha='center')
plt.annotate('Lowest\n30 mm', xy=("June", 30), xytext=("June", 10),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Average Rainfall", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Average Rainfall (mm)", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.6, color='grey')

# Invert the y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()