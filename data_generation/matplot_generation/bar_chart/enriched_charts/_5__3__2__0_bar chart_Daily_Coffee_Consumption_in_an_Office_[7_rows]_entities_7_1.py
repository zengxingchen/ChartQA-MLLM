
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
calories = [2200, 2100, 2300, 2400, 2350, 2450, 2500, 2550, 2400, 2300, 2200, 2100]

# Color codes for each bar
colors = ['#4CAF50', '#FF5722', '#03A9F4', '#E91E63', '#FFEB3B', '#009688', '#9C27B0', '#FFC107', '#795548', '#8BC34A', '#3F51B5', '#F44336']

# Bar width
bar_width = 0.4

# Create vertical bar chart
plt.figure(figsize=(12, 6))
bar_container = plt.bar(months, calories, color=colors, width=bar_width)

# Add data labels
for bar in bar_container:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height}', ha='center', va='bottom')

# Title and labels
plt.title('Monthly Average Calorie Intake in 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Calories')

# Customize the grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits to start from a specific value
plt.ylim(2000, 2600)

# Show plot
plt.show()