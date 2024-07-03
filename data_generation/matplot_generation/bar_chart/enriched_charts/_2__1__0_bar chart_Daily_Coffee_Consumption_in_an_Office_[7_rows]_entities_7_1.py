
import matplotlib.pyplot as plt

# Data
days = [str(i) for i in range(1, 32)]
temperatures = [22, 24, 21, 19, 23, 25, 20, 22, 24, 21, 23, 25, 19, 20, 21, 22, 23, 24, 25, 21, 19, 20, 22, 24, 25, 23, 21, 20, 19, 22, 24]

# Color codes for each bar
colors = ['#FF5733', '#FF8D33', '#FFC433', '#EFFF33', '#B0FF33', '#6AFF33', '#33FF57', '#33FFDA', '#33D2FF', '#3385FF', '#6B33FF', '#D433FF',
          '#FF33B0', '#FF339A', '#FF3364', '#FF3344', '#FF3366', '#FF3380', '#FF33A1', '#FF33C2', '#FF33E3', '#FF33F4', '#FF33B5', '#FF33C7', 
          '#FF33D8', '#FF33E9', '#FF33FB', '#FF33AC', '#FF33BD', '#FF33CE', '#FF33DF']

# Bar width
bar_height = 0.5

# Create horizontal bar chart
plt.figure(figsize=(10, 15))
bar_container = plt.barh(days, temperatures, color=colors, height=bar_height)

# Add data labels
for bar in bar_container:
    width = bar.get_width()
    plt.text(width + 0.5, bar.get_y() + bar.get_height()/2, f'{width}', ha='center', va='bottom')

# Title and labels
plt.title('Daily Temperature in June (°C)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Day')

# Customize the grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show plot
plt.show()