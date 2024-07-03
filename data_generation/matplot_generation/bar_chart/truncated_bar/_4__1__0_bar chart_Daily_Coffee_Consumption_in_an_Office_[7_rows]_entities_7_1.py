
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [5000, 5200, 5400, 5800, 6100, 6300, 6400, 6200, 6000, 5700, 5500, 5300]

# Color codes for each bar
colors = ['#FF5733', '#FF8D33', '#FFC433', '#EFFF33', '#B0FF33', '#6AFF33', '#33FF57', '#33FFDA', '#33D2FF', '#3385FF', '#6B33FF', '#D433FF']

# Bar width
bar_height = 0.6

# Create horizontal bar chart
plt.figure(figsize=(14, 8))
bar_container = plt.barh(months, revenue, color=colors, height=bar_height)

# Add data labels
for bar in bar_container:
    width = bar.get_width()
    plt.text(width + 100, bar.get_y() + bar.get_height()/2, f'{width}', ha='center', va='center')

# Title and labels
plt.title('Monthly Revenue for the Year', pad=20)
plt.xlabel('Revenue ($)')
plt.ylabel('Month')

# Customize the grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Set y-axis limits
plt.xlim(4500, 7000)

# Show plot
plt.show()