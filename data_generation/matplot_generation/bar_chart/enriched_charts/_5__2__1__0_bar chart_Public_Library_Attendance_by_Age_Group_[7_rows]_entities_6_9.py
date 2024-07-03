
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rainfall = [78, 56, 45, 60, 72, 89, 95, 85, 70, 55, 62, 80]

# Colors for each bar
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF', '#AEC7E8', '#FFBB78']

# Create a vertical bar chart
plt.figure(figsize=(10, 12))  # Change the figure size (width x height)
bar_width = 0.6  # Change the bar width
plt.bar(months, rainfall, color=colors, width=bar_width)

# Setting the title and labels
plt.title('Monthly Average Rainfall')
plt.xlabel('Month')
plt.ylabel('Average Rainfall (mm)')

# Adjust the limits to truncate y-axis
plt.ylim([40, max(rainfall) + 10])

# Display the chart
plt.tight_layout()
plt.show()