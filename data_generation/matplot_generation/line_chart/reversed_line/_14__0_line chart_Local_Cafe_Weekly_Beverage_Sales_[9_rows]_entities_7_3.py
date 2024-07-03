
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
steps = [5000, 6200, 7000, 7500, 8500, 9000, 9500, 8000, 7700, 7200, 6800, 6200]

plt.figure(figsize=(10, 5))  # Change width and height of the chart

# Plotting the line chart
plt.plot(months, steps, color="#1E90FF", marker='s')  # Using a specific color code and marker for data points

# Adding annotations for specific points
plt.annotate('Highest Activity', xy=('July', 9500), xytext=('June', 9600),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Activity Drop', xy=('August', 8000), xytext=('September', 8500),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Average Monthly Steps in City X')
plt.xlabel('Month')
plt.ylabel('Steps Count')

plt.gca().invert_yaxis()  # Invert the y-axis

# Show the chart
plt.show()