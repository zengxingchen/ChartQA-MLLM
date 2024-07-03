
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [1500, 1700, 1650, 1800, 1900, 2100, 2050, 2200, 2300, 2250, 2150, 2400]

# Colors for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e']

# Create a vertical bar chart
plt.figure(figsize=(12, 6))  # Change the figure size (width x height)
bar_width = 0.5  # Change the bar width
plt.bar(months, sales, color=colors, width=bar_width)

# Setting the title and labels
plt.title('Monthly Sales in 2023')
plt.xlabel('Month')
plt.ylabel('Sales ($)')

# Adjust the limits if necessary
plt.ylim([0, max(sales) + 500])

# Display the chart
plt.tight_layout()
plt.show()