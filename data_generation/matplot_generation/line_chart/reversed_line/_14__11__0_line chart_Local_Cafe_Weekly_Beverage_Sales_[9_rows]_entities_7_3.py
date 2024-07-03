
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weight = [80, 78, 76, 74, 72, 70, 72, 74, 76, 78, 79, 81]

plt.figure(figsize=(12, 6))  # Change width and height of the chart

# Plotting the line chart
plt.plot(months, weight, color="#FF5733", marker='o')  # Using a specific color code and marker for data points

# Adding annotations for specific points
plt.annotate('Reached Target Weight', xy=('June', 70), xytext=('April', 73),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Weight Increase', xy=('December', 81), xytext=('October', 82),
             arrowprops=dict(facecolor='purple', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Weight Trend for Fitness Journey')
plt.xlabel('Month')
plt.ylabel('Weight (kg)')

plt.gca().invert_yaxis()  # Invert the y-axis

# Show the chart
plt.show()