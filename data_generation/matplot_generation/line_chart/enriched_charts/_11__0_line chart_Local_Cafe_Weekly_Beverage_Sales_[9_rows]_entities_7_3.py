
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
rainfall = [78, 85, 92, 104, 120, 135, 155, 148, 130, 105, 90, 80]

plt.figure(figsize=(14, 7))  # Change width and height of the chart

# Plotting the line chart
plt.plot(months, rainfall, color="#1f77b4", marker='s')  # Using a specific color code and marker for data points

# Adding annotations for specific points
plt.annotate('Rainy Season Begins', xy=('June', 135), xytext=('April', 150),
             arrowprops=dict(facecolor='green', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Peak Rainfall', xy=('July', 155), xytext=('September', 160),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Average Monthly Rainfall in City Y')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')

# Show the chart
plt.show()