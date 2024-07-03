
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [500, 450, 600, 700, 650, 800, 850, 900, 750, 650, 550, 500]

# Color codes for each bar
colors = ['#1F77B4', '#AEC7E8', '#FF7F0E', '#FFBB78', '#2CA02C', '#98DF8A', '#D62728', '#FF9896', '#9467BD', '#C5B0D5', '#8C564B', '#C49C94']

# Bar width
bar_width = 0.4

# Create vertical bar chart
plt.figure(figsize=(12, 6))
bar_container = plt.bar(months, sales, color=colors, width=bar_width)

# Add data labels
for bar in bar_container:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height}', ha='center', va='bottom')

# Title and labels
plt.title('Monthly Sales Figures')
plt.xlabel('Month')
plt.ylabel('Sales ($)')

# Customize the grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()