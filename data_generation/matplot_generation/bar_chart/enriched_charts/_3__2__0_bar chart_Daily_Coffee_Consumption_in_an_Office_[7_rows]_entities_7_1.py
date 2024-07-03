
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
calories = [2200, 2100, 2300, 2400, 2350, 2450, 2500, 2550, 2400, 2300, 2200, 2100]

# Color codes for each bar
colors = ['#1E88E5', '#D81B60', '#FFC107', '#43A047', '#FB8C00', '#8E24AA', '#00ACC1', '#F4511E', '#3949AB', '#7CB342', '#FDD835', '#8D6E63']

# Bar width
bar_width = 0.5

# Create horizontal bar chart
plt.figure(figsize=(8, 10))
bar_container = plt.barh(months, calories, color=colors, height=bar_width)

# Add data labels
for bar in bar_container:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f'{width}', ha='left', va='center')

# Title and labels
plt.title('Monthly Average Calorie Intake')
plt.xlabel('Calories')
plt.ylabel('Month')

# Customize the grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show plot
plt.show()