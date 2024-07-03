
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
precipitation = [78, 55, 68, 82, 97, 110, 120, 115, 95, 85, 76, 65]

# Colors for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#9edae5', '#c7c7c7']

# Create a vertical bar chart
plt.figure(figsize=(12, 6))  # Change the figure size (width x height)
bar_width = 0.5  # Change the bar width
plt.bar(months, precipitation, color=colors, width=bar_width)

# Setting the title and labels
plt.title('Monthly Precipitation in Metropolis', pad=20)
plt.ylabel('Average Precipitation (mm)')
plt.xlabel('Month')

# Adjust the limits if necessary
plt.ylim([50, max(precipitation) + 10])

# Display the chart
plt.tight_layout()
plt.show()