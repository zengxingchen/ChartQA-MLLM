
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
exercise_time = [30, 45, 50, 60, 75, 80, 90, 85, 70, 65, 55, 40]

# Creating the line chart
plt.figure(figsize=(14, 7))

plt.plot(months, exercise_time, color="#32CD32", marker='o')

# Annotating the highest and lowest exercise times
plt.annotate('Highest\n90 minutes', xy=("July", 90), xytext=("July", 95),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), ha='center')
plt.annotate('Lowest\n30 minutes', xy=("January", 30), xytext=("January", 25),
             arrowprops=dict(facecolor='#1E90FF', shrink=0.05), ha='center')

# Title and labels
plt.title("Average Monthly Exercise Time in a Year", fontsize=18, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Average Exercise Time (minutes)", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.7, color='grey')

# Show the plot
plt.show()