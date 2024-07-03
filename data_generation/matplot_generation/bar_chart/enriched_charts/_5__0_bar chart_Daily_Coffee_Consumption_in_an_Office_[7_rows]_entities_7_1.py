
import matplotlib.pyplot as plt

# Data
dates = [
    '01-Jan', '02-Jan', '03-Jan', '04-Jan', '05-Jan', '06-Jan', '07-Jan', '08-Jan', '09-Jan', '10-Jan',
    '11-Jan', '12-Jan', '13-Jan', '14-Jan', '15-Jan', '16-Jan', '17-Jan', '18-Jan', '19-Jan', '20-Jan',
    '21-Jan', '22-Jan', '23-Jan', '24-Jan', '25-Jan', '26-Jan', '27-Jan', '28-Jan', '29-Jan', '30-Jan', '31-Jan'
]
rainfall = [
    5, 3, 4, 0, 8, 7, 5, 6, 9, 3, 4, 6, 8, 9, 10, 2, 4, 6, 8, 7, 5, 6, 9, 3, 4, 5, 6, 8, 10, 11, 7
]

# Color codes for each bar
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4'
]

# Bar width
bar_width = 0.5

# Create vertical bar chart
plt.figure(figsize=(12, 6))
bar_container = plt.bar(dates, rainfall, color=colors, width=bar_width)

# Add data labels
for bar in bar_container:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height} mm', ha='center', va='bottom')
    
# Title and labels
plt.title('Daily Rainfall in January')
plt.xlabel('Date')
plt.ylabel('Rainfall (mm)')

# Set y-axis limits
plt.ylim(0, 12)

# Customize the grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()