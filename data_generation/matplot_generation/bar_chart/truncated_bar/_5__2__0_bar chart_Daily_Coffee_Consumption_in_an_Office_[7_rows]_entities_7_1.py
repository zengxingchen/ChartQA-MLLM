
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [500, 450, 600, 700, 650, 800, 850, 950, 750, 650, 550, 500]

# Color codes for each bar
colors = ['#4B0082', '#483D8B', '#6A5ACD', '#7B68EE', '#9370DB', '#8A2BE2', '#9400D3', '#9932CC', '#BA55D3', '#DA70D6', '#EE82EE', '#DDA0DD']

# Bar width
bar_width = 0.6

# Create horizontal bar chart
plt.figure(figsize=(14, 8))
bar_container = plt.barh(months, sales, color=colors, height=bar_width)

# Add data labels
for bar in bar_container:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f'{width}', ha='left', va='center')

# Title and labels
plt.title('Monthly Sales Performance')
plt.xlabel('Sales ($)')
plt.ylabel('Month')

# Customize the grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Set y-axis limits to start from 400
plt.xlim(400, max(sales) + 100)

# Show plot
plt.show()