
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sales = [1500, 1400, 1600, 1800, 1700, 1600, 1500, 1550, 1650, 1750, 1850, 1950]

# Creating the line chart
plt.figure(figsize=(12, 6))  # Modifying width and height of the chart

plt.plot(months, sales, color="#4682B4", marker='o')  # Using a specific color code

# Annotating the highest and lowest sales
plt.annotate('Highest\n1950 Units', xy=("December", 1950), xytext=("December", 1980),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05), ha='center')
plt.annotate('Lowest\n1400 Units', xy=("February", 1400), xytext=("February", 1370),
             arrowprops=dict(facecolor='#6495ED', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Sales Data in Units", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales Units", fontsize=12)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')

# Invert y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()