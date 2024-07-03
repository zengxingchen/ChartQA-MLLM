
import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 31)]
number_of_visitors = [50, 55, 53, 52, 54, 58, 61, 63, 67, 69, 68, 70, 72, 74, 73, 76, 78, 77, 79, 81, 80, 83, 84, 86, 85, 87, 90, 89, 91, 93]

# Creating the line chart
plt.figure(figsize=(14, 8))  # Change the width and height of the chart
plt.plot(days, number_of_visitors, marker='o', color='#1f77b4', label='Daily Visitors')  # Specific color code

# Annotation for a significant day
plt.annotate('Surge', xy=(30, 93), xytext=(25, 90),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Day of the Month')
plt.ylabel('Number of Visitors')
plt.title('Daily Visitors in a Museum - June 2023', pad=20)
plt.legend(loc='upper left')
plt.grid(True)

# Display the chart
plt.show()