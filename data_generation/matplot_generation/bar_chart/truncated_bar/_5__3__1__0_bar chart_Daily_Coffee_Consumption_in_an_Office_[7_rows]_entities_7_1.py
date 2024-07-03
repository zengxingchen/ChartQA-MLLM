
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [32, 35, 42, 48, 55, 65, 72, 70, 60, 50, 40, 35]

# Color codes for each bar
colors = ['#FF5733', '#FF6F33', '#FF8D33', '#FFAA33', '#FFC433', '#FFE033', '#EFFF33', '#B0FF33', '#6AFF33', '#33FF57', '#33FFB2', '#33FFD2']

# Bar width
bar_width = 0.5

# Create vertical bar chart
plt.figure(figsize=(12, 6))
bar_container = plt.bar(months, temperatures, color=colors, width=bar_width)

# Add data labels
for bar in bar_container:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}', ha='center', va='bottom')

# Title and labels
plt.title('Average Monthly Temperatures in 2023')
plt.ylabel('Temperature (°F)')
plt.xlabel('Month')

# Customize the grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits to truncate the chart
plt.ylim(30, 75)

# Show plot
plt.show()