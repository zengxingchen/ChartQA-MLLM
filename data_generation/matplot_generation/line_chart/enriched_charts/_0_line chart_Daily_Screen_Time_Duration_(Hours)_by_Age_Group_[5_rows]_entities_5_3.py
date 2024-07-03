
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
revenue = [2000, 2200, 2100, 1850, 1950, 2100, 2300, 2400, 2050, 2000, 2200, 2600]

# Creating the line chart
plt.figure(figsize=(10, 5))  # Change the width and height of the chart
plt.plot(months, revenue, marker='o', color='#007acc', label='Monthly Revenue')  # Specific color code

# Annotation for the highest revenue month
plt.annotate('Highest', xy=('December', 2600), xytext=('November', 2500),
             arrowprops=dict(facecolor='#d62728', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Monthly Revenue for Small Business - 2023')
plt.legend()
plt.grid(True)

# Display the chart
plt.show()