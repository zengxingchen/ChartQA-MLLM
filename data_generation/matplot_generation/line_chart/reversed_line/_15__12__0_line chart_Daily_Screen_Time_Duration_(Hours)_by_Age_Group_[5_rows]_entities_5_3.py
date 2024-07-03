
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
student_performance = [78, 80, 82, 79, 81, 83, 85, 84, 87, 86, 88, 90]

# Creating the line chart
plt.figure(figsize=(10, 5))  # Change the width and height of the chart
plt.plot(months, student_performance, marker='o', color='#1f77b4', label='Student Performance Score')  # Specific color code

# Annotation for the highest and lowest performance months
plt.annotate('Lowest', xy=('January', 78), xytext=('February', 77),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))
plt.annotate('Highest', xy=('December', 90), xytext=('November', 91),
             arrowprops=dict(facecolor='#2ca02c', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Month')
plt.ylabel('Student Performance Score')
plt.title('Monthly Student Performance Scores - 2023')
plt.legend(loc='lower right')
plt.grid(True)
plt.gca().invert_yaxis()  # Invert the y-axis

# Display the chart
plt.show()