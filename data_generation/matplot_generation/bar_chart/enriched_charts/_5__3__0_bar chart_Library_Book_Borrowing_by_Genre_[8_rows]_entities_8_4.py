
import matplotlib.pyplot as plt

# Data
cities = [
    "New York", "Los Angeles", "London", "Tokyo", "Sydney",
    "Moscow", "Dubai", "Paris", "Beijing", "Mumbai",
    "Johannesburg", "Rio de Janeiro", "Toronto", "Delhi", 
    "Singapore", "Cape Town", "Hong Kong", "San Francisco", 
    "Buenos Aires", "Cairo"
]
consumption = [
    120, 95, 85, 150, 105, 90, 70, 100, 140, 130,
    80, 110, 115, 125, 135, 75, 145, 130, 95, 65
]

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(10, 14))

# Horizontal bar chart
bars = ax.barh(cities, consumption, color=[
    '#4B0082', '#8A2BE2', '#FF4500', '#FF6347', '#00FA9A', 
    '#4682B4', '#D2691E', '#6495ED', '#DC143C', '#FF7F50', 
    '#2E8B57', '#DAA520', '#7FFF00', '#ADFF2F', '#7B68EE',
    '#00CED1', '#FF69B4', '#FFD700', '#FF4500', '#5F9EA0'
], height=0.5)

# Set the title and labels
ax.set_title('Average Annual Vegetable Consumption per Capita (kg)', fontsize=18)
ax.set_xlabel('Average Annual Vegetable Consumption (kg)', fontsize=14)
ax.set_ylabel('City', fontsize=14)

# Remove the spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Set grid to be behind the bars
ax.set_axisbelow(True)
ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

# Show Values on Bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 3
    ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width}', ha='center', va='bottom')

# Set the layout to be tight
plt.tight_layout()

# Set y-axis limits
ax.set_xlim(50, 160)

# Show the plot
plt.show()