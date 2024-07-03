
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
revenue = [1800, 1600, 2000, 2200, 2100, 2400, 2300, 2500, 2700, 2600, 3000, 2900]

# Creating the line chart
plt.figure(figsize=(12, 6))  # Change the width and height of the chart
plt.plot(months, revenue, marker='o', color='#ff5733', label='Monthly Revenue')  # Specific color code

# Annotation for the highest revenue month
plt.annotate('Highest', xy=('November', 3000), xytext=('October', 2900),
             arrowprops=dict(facecolor='#33ff57', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Monthly Revenue for a Small Business - 2023', pad=20)
plt.legend(loc='upper right')
plt.grid(True)
plt.gca().invert_yaxis()  # Invert y-axis

# Display the chart
plt.show()