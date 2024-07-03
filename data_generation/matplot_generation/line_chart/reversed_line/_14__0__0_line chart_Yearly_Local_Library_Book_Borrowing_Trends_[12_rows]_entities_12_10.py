
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
vitamin_c_intake = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115]

# Creating the line chart
plt.figure(figsize=(10, 5))

plt.plot(months, vitamin_c_intake, color="#32CD32", marker='o')

# Annotating the highest and lowest vitamin C intake
plt.annotate('Highest\n115mg', xy=("December", 115), xytext=("December", 120),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), ha='center')
plt.annotate('Lowest\n60mg', xy=("January", 60), xytext=("January", 55),
             arrowprops=dict(facecolor='#1E90FF', shrink=0.05), ha='center')

# Title and labels
plt.title("Average Monthly Vitamin C Intake in a Year", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Vitamin C Intake (mg)", fontsize=12)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.7, color='grey')

# Inverting the y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()