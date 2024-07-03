
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
steps = [10200, 9400, 11200, 10800, 11500, 12200, 12500, 11800, 11600, 11200, 10800, 10400]

# Colors for each bar
colors = ['#FF5733', '#FF8D33', '#FFC133', '#FFE333', '#E3FF33', '#A8FF33', '#63FF33', '#33FF57', '#33FFAB', '#33FFE3', '#33C8FF', '#338FFF']

# Create a horizontal bar chart
plt.figure(figsize=(14, 8))  # Change the figure size (width x height)
bar_height = 0.5  # Change the bar height
plt.barh(months, steps, color=colors, height=bar_height)

# Setting the title and labels
plt.title('Monthly Average Steps Count')
plt.xlabel('Average Steps')
plt.ylabel('Month')

# Adjust the limits if necessary
plt.xlim([0, max(steps) + 2000])

# Display the chart
plt.tight_layout()
plt.show()