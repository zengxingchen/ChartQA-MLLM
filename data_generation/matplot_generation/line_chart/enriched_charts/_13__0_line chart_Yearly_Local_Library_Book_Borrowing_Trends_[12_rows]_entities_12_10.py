
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
calories_burned = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]

# Creating the line chart
plt.figure(figsize=(12, 6))  # Modifying width and height of the chart

plt.plot(months, calories_burned, color="#1E90FF", marker='o')  # Using a specific color code

# Annotating the highest and lowest calories burned
plt.annotate('Highest\n750 kcal', xy=("December", 750), xytext=("December", 770),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), ha='center')
plt.annotate('Lowest\n200 kcal', xy=("January", 200), xytext=("January", 180),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Calories Burned in a Year", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Calories Burned (kcal)", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')

# Show the plot
plt.show()