
import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 31)]
books_read = [1, 2, 1, 3, 2, 4, 3, 4, 5, 3, 6, 5, 4, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15]

# Creating the line chart
plt.figure(figsize=(10, 8))  # Change the width and height of the chart
plt.plot(days, books_read, marker='s', color='#1f77b4', label='Books Read')  # Specific color code

# Annotation for the highest book read day
plt.annotate('Most Books Read', xy=(30, 15), xytext=(25, 13),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Day of the Month')
plt.ylabel('Books Read')
plt.title('Books Read in June - 2023')
plt.legend(loc='upper left')
plt.grid(True)

# Display the chart
plt.show()