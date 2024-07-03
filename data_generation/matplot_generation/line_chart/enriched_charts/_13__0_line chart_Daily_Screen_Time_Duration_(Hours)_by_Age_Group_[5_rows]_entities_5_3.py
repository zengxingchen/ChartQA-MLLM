
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
nutrition_scores = [80, 75, 90, 85, 70, 95, 65, 100, 60, 105, 55, 110]

# Creating the line chart
plt.figure(figsize=(12, 6))  # Change the width and height of the chart
plt.plot(months, nutrition_scores, marker='s', color='#ff7f0e', label='Monthly Nutrition Score')  # Specific color code

# Annotation for the highest and lowest nutrition score month
plt.annotate('Highest', xy=('December', 110), xytext=('November', 100),
             arrowprops=dict(facecolor='#1f77b4', shrink=0.05))
plt.annotate('Lowest', xy=('November', 55), xytext=('October', 65),
             arrowprops=dict(facecolor='#d62728', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Month')
plt.ylabel('Nutrition Score')
plt.title('Monthly Nutrition Scores for Health Tracker - 2023')
plt.legend(loc='upper left')
plt.grid(True)

# Invert y-axis
plt.gca().invert_yaxis()

# Display the chart
plt.show()