
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [-2, -1, 4, 10, 15, 20, 22, 21, 17, 11, 5, -1]

# Color codes for each bar
colors = ['#FF5733', '#FF8D33', '#FFC433', '#EFFF33', '#B0FF33', '#6AFF33', '#33FF57', '#33FFDA', '#33D2FF', '#3385FF', '#6B33FF', '#D433FF']

# Bar width
bar_width = 0.6

# Create horizontal bar chart
plt.figure(figsize=(10, 8))
bar_container = plt.barh(months, temperatures, color=colors, height=bar_width)

# Add data labels
for bar in bar_container:
    width = bar.get_width()
    label_x_pos = width if width > 0 else width - 5
    plt.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width} °C', va='center')
    
# Title and labels
plt.title('Average Monthly Temperatures')
plt.xlabel('Temperature (°C)')
plt.ylabel('Month')

# Customize the grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show plot
plt.show()