
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
temperatures = [5, 6, 10, 15, 20, 25, 28, 27, 22, 16, 10, 6]

plt.figure(figsize=(12, 6))  # Change width and height of the chart

# Plotting the line chart
plt.plot(months, temperatures, color="#ff6347", marker='o')  # Using a specific color code and marker for data points

# Adding annotations for specific points
plt.annotate('Warm Season Begins', xy=('May', 20), xytext=('March', 18),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Peak Temperature', xy=('July', 28), xytext=('September', 30),
             arrowprops=dict(facecolor='purple', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Average Monthly Temperature Fluctuations in City X')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')

# Show the chart
plt.show()