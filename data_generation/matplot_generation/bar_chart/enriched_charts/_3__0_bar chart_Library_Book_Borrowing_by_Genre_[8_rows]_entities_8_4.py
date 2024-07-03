
import matplotlib.pyplot as plt

# Data
cities = [
    "New York", "Los Angeles", "London", "Tokyo", "Sydney",
    "Moscow", "Dubai", "Paris", "Beijing", "Mumbai",
    "Johannesburg", "Rio de Janeiro", "Toronto", "Delhi", 
    "Singapore", "Cape Town", "Hong Kong", "San Francisco", 
    "Buenos Aires", "Cairo"
]
rainfall = [
    1200, 380, 610, 1520, 1210, 690, 100, 650, 570, 2420,
    750, 1170, 830, 780, 2160, 515, 2380, 520, 1160, 25
]

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(14, 10))

# Vertical bar chart
bars = ax.bar(cities, rainfall, color=[
    '#FF6347', '#4682B4', '#8A2BE2', '#5F9EA0', '#7FFF00', 
    '#D2691E', '#FF7F50', '#6495ED', '#DC143C', '#00FA9A', 
    '#FF4500', '#2E8B57', '#DAA520', '#4B0082', '#ADFF2F',
    '#7B68EE', '#00CED1', '#FF69B4', '#FFD700', '#FF4500'
], width=0.6)

# Set the title and labels
ax.set_title('Average Annual Rainfall in Various Cities (mm)', fontsize=18)
ax.set_xlabel('City', fontsize=14)
ax.set_ylabel('Average Annual Rainfall (mm)', fontsize=14)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Remove the spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Set grid to be behind the bars
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

# Show Values on Bars
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 20
    ax.text(bar.get_x() + bar.get_width() / 2, label_y_pos, f'{height}', ha='center', va='bottom')

# Set the layout to be tight
plt.tight_layout()

# Show the plot
plt.show()