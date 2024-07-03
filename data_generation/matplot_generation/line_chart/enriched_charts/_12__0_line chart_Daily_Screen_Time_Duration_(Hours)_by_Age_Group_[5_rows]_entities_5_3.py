
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
co2_emission = [5.5, 5.3, 5.2, 5.0, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1]

# Creating the line chart
plt.figure(figsize=(12, 6))  # Change the width and height of the chart
plt.plot(months, co2_emission, marker='s', color='#ff5733', label='Monthly CO2 Emission')  # Specific color code

# Annotation for the highest and lowest emission months
plt.annotate('Highest', xy=('January', 5.5), xytext=('February', 5.6),
             arrowprops=dict(facecolor='#ff5733', shrink=0.05))
plt.annotate('Lowest', xy=('December', 4.1), xytext=('November', 4.2),
             arrowprops=dict(facecolor='#33cc33', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Month')
plt.ylabel('CO2 Emission (Metric Tons)')
plt.title('Monthly CO2 Emission for Urban Area - 2023')
plt.legend(loc='upper right')
plt.grid(True)

# Display the chart
plt.show()