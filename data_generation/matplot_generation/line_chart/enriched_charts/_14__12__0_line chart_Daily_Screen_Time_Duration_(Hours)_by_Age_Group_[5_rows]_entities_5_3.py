
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
values = [0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0]

# Creating the line chart
plt.figure(figsize=(10, 5))  # Change the width and height of the chart
plt.plot(months, values, marker='o', color='#1f77b4', label='Monthly Music Stream Count')  # Specific color code

# Annotation for the highest and lowest values
plt.annotate('Highest', xy=('December', 3.0), xytext=('November', 3.1),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))
plt.annotate('Lowest', xy=('January', 0.8), xytext=('February', 0.9),
             arrowprops=dict(facecolor='#2ca02c', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Month')
plt.ylabel('Stream Count (Millions)')
plt.title('Monthly Music Stream Count for 2023')
plt.legend(loc='upper left')
plt.grid(True)
plt.gca().invert_yaxis()

# Display the chart
plt.show()