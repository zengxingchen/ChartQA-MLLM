
import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 31)]
caloric_intake = [2000, 1950, 1980, 1930, 1900, 1850, 1800, 1820, 1850, 1830, 1800, 1780, 1750, 1730, 1700, 1680, 1650, 1620, 1600, 1580, 1550, 1530, 1500, 1480, 1460, 1440, 1420, 1400, 1380, 1350]

# Creating the line chart
plt.figure(figsize=(14, 8))  # Change the width and height of the chart
plt.plot(days, caloric_intake, marker='o', color='#ff7f0e', label='Daily Caloric Intake')  # Specific color code

# Annotation for a significant day
plt.annotate('Lowest Point', xy=(30, 1350), xytext=(25, 1400),
             arrowprops=dict(facecolor='#1f77b4', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Day of the Month')
plt.ylabel('Caloric Intake (kcal)')
plt.title('Daily Caloric Intake of an Individual - June 2023', pad=20)
plt.legend(loc='upper right')
plt.grid(True)
plt.gca().invert_yaxis()  # Inverting the y-axis

# Display the chart
plt.show()