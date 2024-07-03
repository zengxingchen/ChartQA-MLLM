
import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 31)]
co2_levels = [449.9, 448.3, 446.7, 445.1, 443.9, 442.5, 441.2, 439.6, 438.3, 436.8, 435.5, 434.0, 432.2, 431.1, 429.8, 428.5, 426.2, 424.9, 423.1, 420.7, 418.6, 417.2, 414.8, 412.5, 410.1, 408.5, 406.7, 404.2, 402.1, 400.5]

# Creating the line chart
plt.figure(figsize=(16, 8))  # Adjust the width and height of the chart
plt.plot(days, co2_levels, marker='o', color='#4CAF50', label='Daily CO2 Levels')  # Specific color code

# Annotation for a notable CO2 level
plt.annotate('Significant Drop', xy=(1, 449.9), xytext=(5, 445),
             arrowprops=dict(facecolor='#FF5722', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Day of the Month')
plt.ylabel('CO2 Levels (ppm)')
plt.title('Daily CO2 Levels in Reverse Order - June 2023')
plt.legend(loc='lower right')
plt.grid(True)

# Invert y-axis
plt.gca().invert_yaxis()

# Display the chart
plt.show()