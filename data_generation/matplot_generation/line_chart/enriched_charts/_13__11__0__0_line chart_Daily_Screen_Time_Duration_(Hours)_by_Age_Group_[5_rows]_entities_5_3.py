
import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 31)]
number_of_articles_read = [150, 148, 145, 147, 144, 143, 140, 138, 136, 135, 134, 133, 131, 130, 129, 128, 126, 124, 123, 122, 120, 119, 118, 116, 115, 114, 112, 110, 109, 108]

# Creating the line chart
plt.figure(figsize=(16, 9))  # Change the width and height of the chart
plt.plot(days, number_of_articles_read, marker='o', color='#2ca02c', label='Daily Articles Read')  # Specific color code

# Annotation for a significant day
plt.annotate('Sudden Drop', xy=(30, 108), xytext=(25, 110),
             arrowprops=dict(facecolor='#d62728', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Day of the Month')
plt.ylabel('Number of Articles Read')
plt.title('Daily Articles Read in an Online Platform - June 2023', pad=20)
plt.legend(loc='upper right')
plt.grid(True)

# Display the chart
plt.show()