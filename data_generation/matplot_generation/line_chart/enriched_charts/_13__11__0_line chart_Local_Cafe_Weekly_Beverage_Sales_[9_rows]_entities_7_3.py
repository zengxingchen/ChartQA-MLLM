
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
revenue_growth = [80, 75, 85, 95, 105, 110, 120, 118, 115, 110, 95, 90]

plt.figure(figsize=(16, 8))  # Change width and height of the chart

# Plotting the line chart
plt.plot(months, revenue_growth, color="#ff5733", marker='o')  # Using a specific color code and marker for data points

# Adding annotations for specific points
plt.annotate('New Product Launch', xy=('March', 85), xytext=('January', 100),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Highest Growth', xy=('July', 120), xytext=('September', 130),
             arrowprops=dict(facecolor='purple', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Quarterly Revenue Growth of Company Z')
plt.xlabel('Month')
plt.ylabel('Revenue Growth (million $)')

# Inverse the y-axis
plt.gca().invert_yaxis()

# Show the chart
plt.show()