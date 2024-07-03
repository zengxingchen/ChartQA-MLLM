
import matplotlib.pyplot as plt

# Data
days = [str(i) for i in range(1, 31)]
precipitation = [5.2, 4.8, 6.1, 7.4, 5.0, 5.6, 6.2, 4.7, 5.8, 6.5, 5.4, 7.0, 4.9, 5.5, 6.0, 6.8, 5.1, 5.7, 6.3, 4.5, 6.6, 5.3, 5.9, 4.6, 6.4, 4.4, 6.7, 5.0, 5.6, 6.1]

# Color codes for each bar
colors = ['#8B0000', '#FF4500', '#FFD700', '#ADFF2F', '#32CD32', '#00FA9A', '#00CED1', '#4682B4', '#1E90FF', '#4169E1', '#6A5ACD', '#7B68EE',
          '#BA55D3', '#EE82EE', '#DDA0DD', '#EE82EE', '#BA55D3', '#8A2BE2', '#4B0082', '#800080', '#9400D3', '#9932CC', '#8B0000', '#FF4500', 
          '#FFD700', '#ADFF2F', '#32CD32', '#00FA9A', '#00CED1', '#4682B4']

# Bar width
bar_width = 0.6

# Create vertical bar chart
plt.figure(figsize=(12, 8))
bar_container = plt.bar(days, precipitation, color=colors, width=bar_width)

# Add data labels
for bar in bar_container:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.1, f'{height}', ha='center', va='bottom')

# Title and labels
plt.title('Daily Precipitation in June (mm)')
plt.xlabel('Day')
plt.ylabel('Precipitation (mm)')

# Customize the grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits
plt.ylim(4, 8)

# Show plot
plt.show()