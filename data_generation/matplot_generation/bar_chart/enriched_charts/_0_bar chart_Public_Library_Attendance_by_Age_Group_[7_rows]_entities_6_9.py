
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [6, 7, 10, 13, 17, 20, 23, 22, 19, 14, 10, 7]

# Colors for each bar
colors = ['#FF5733', '#FF8D33', '#FFC133', '#FFE333', '#E3FF33', '#A8FF33', '#63FF33', '#33FF57', '#33FFAB', '#33FFE3', '#33C8FF', '#338FFF']

# Create a horizontal bar chart
plt.figure(figsize=(10, 8))  # Change the figure size (width x height)
bar_height = 0.6  # Change the bar height
plt.barh(months, temperatures, color=colors, height=bar_height)

# Setting the title and labels
plt.title('Average Monthly Temperatures for Metropolis')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Month')

# Adjust the limits if necessary
plt.xlim([0, max(temperatures) + 5])

# Display the chart
plt.tight_layout()
plt.show()