
import matplotlib.pyplot as plt

# Data
categories = ['Books', 'Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys', 'Sports', 'Beauty', 'Automotive', 'Music', 'Garden', 'Health', 'Pets', 'Office Supplies']
amounts = [52, 80, 35, 65, 30, 55, 40, 45, 60, 25, 20, 75, 32, 38]

# Color codes for each bar
colors = ['#4B0082', '#FF4500', '#2E8B57', '#DC143C', '#9932CC', '#8B4513', '#FF69B4', '#708090', '#BDB76B', '#20B2AA', '#778899', '#CD853F', '#FFB6C1', '#A9A9A9']

# Bar width
bar_width = 0.6

# Create horizontal bar chart
plt.figure(figsize=(14, 8))
bar_container = plt.barh(categories, amounts, color=colors, height=bar_width)

# Add data labels
for bar in bar_container:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f'{width}', ha='left', va='center')

# Title and labels
plt.title('Spending by Category')
plt.xlabel('Amount Spent ($)')
plt.ylabel('Category')

# Customize the grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Set y-axis limits to truncate the bar chart
plt.xlim(20, 85)

# Show plot
plt.tight_layout()
plt.show()