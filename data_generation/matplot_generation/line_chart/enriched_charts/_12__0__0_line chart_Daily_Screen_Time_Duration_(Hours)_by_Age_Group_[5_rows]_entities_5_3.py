import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 31)]
co2_levels = [410.1, 412.5, 414.8, 417.2, 420.3, 422.6, 421.4, 419.8, 418.6, 420.7, 423.1, 424.9, 426.2, 428.5, 429.8, 431.1, 433.0, 432.2, 434.0, 435.5, 436.8, 438.3, 439.6, 441.2, 442.5, 443.9, 445.1, 446.7, 448.3, 449.9]

# Creating the line chart
plt.figure(figsize=(14, 7))  # Adjust the width and height of the chart
plt.plot(days, co2_levels, marker='D', color='#1f77b4', label='Daily CO2 Levels')  # Specific color code

# Annotation for a notable CO2 level
plt.annotate('Significant Rise', xy=(30, 449.9), xytext=(25, 445),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Day of the Month')
plt.ylabel('CO2 Levels (ppm)')
plt.title('Daily CO2 Levels in June - 2023')
plt.legend(loc='upper left')
plt.grid(True)

# Display the chart
plt.show()