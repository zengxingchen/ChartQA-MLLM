
import matplotlib.pyplot as plt

# Data
categories = ['Books', 'Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys', 'Sports', 'Beauty', 'Automotive', 'Music', 'Garden', 'Health', 'Pets', 'Office Supplies']
amounts = [45, 75, 30, 60, 25, 50, 35, 40, 55, 20, 15, 70, 28, 33]

# Color codes for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#9edae5', '#c49c94', '#f7b6d2', '#c7c7c7']

# Bar width
bar_width = 0.5

# Create vertical bar chart
plt.figure(figsize=(12, 6))
bar_container = plt.bar(categories, amounts, color=colors, width=bar_width)

# Add data labels
for bar in bar_container:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height}', ha='center', va='bottom')

# Title and labels
plt.title('Expenditure by Category')
plt.xlabel('Category')
plt.ylabel('Amount Spent ($)')

# Customize the grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.tight_layout()
plt.show()