
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
temperatures = [5, 6, 10, 13, 17, 20, 22, 30, 24, 18, 11, 7]

plt.figure(figsize=(12, 6))  # Change width and height of the chart

# Plotting the line chart
plt.plot(months, temperatures, color="#FF5733", marker='o')  # Using a specific color code and marker for data points

# Adding annotations for specific points
plt.annotate('Heatwave starts', xy=('July', 22), xytext=('June', 25),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Heatwave ends', xy=('August', 30), xytext=('September', 28),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Average Monthly Temperature in City X')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')

# Show the chart
plt.show()