
import matplotlib.pyplot as plt

# Data
countries = ['France', 'Spain', 'USA', 'China', 'Italy', 'Turkey', 'Mexico', 'Germany', 'Thailand', 'UK', 'Japan', 'Australia']
visitor_counts = [90, 83, 80, 65, 64, 51, 45, 39, 38, 36, 32, 30]

# Color codes for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#9edae5', '#e7969c']

# Bar width
bar_width = 0.6

# Create horizontal bar chart
plt.figure(figsize=(10, 8))
bar_container = plt.barh(countries, visitor_counts, color=colors, height=bar_width)

# Add data labels
for bar in bar_container:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}', ha='center', va='bottom')
    
# Title and labels
plt.title('Number of Tourists Visiting Various Countries (Millions)', pad=20)
plt.xlabel('Visitors (Millions)')
plt.ylabel('Country')

# Set y-axis limits
plt.xlim(25, 95)

# Customize the grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show plot
plt.show()