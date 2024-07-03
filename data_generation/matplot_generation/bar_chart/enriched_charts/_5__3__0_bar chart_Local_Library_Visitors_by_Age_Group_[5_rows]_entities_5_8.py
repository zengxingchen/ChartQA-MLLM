
import matplotlib.pyplot as plt

# Data
cities = [
    "Seattle", "Miami", "New York", "Los Angeles", "Chicago", 
    "Houston", "Phoenix", "Philadelphia", "San Antonio", 
    "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", 
    "Fort Worth", "Columbus", "Charlotte", "Denver", "Boston", 
    "Detroit", "Indianapolis", "Washington", "Nashville", 
    "Baltimore", "Memphis", "Milwaukee", "Portland", 
    "Las Vegas", "New Orleans", "Kansas City"
]
population = [
    750000, 467000, 8419600, 3980400, 2716000, 2328000, 1690000, 1584200, 1547200, 
    1426500, 1341000, 1035300, 978000, 911000, 909000, 898000, 872000, 727000, 
    692000, 670000, 872000, 706000, 692000, 586000, 651000, 590000, 654000, 
    651000, 391000, 491000
]

# Colors for each city
colors = [
    '#4B0082', '#FF1493', '#FFD700', '#FF4500', '#7FFF00', 
    '#DC143C', '#00FA9A', '#FF69B4', '#FF6347', '#8A2BE2', 
    '#5F9EA0', '#D2691E', '#FF7F50', '#6495ED', '#FFF8DC', 
    '#DDA0DD', '#8B0000', '#00CED1', '#FFD700', '#ADFF2F', 
    '#FF6347', '#FF4500', '#7FFF00', '#DC143C', '#00FA9A', 
    '#FF69B4', '#FF6347', '#8A2BE2', '#5F9EA0', '#D2691E'
]

# Plot
fig, ax = plt.subplots(figsize=(10, 14))
bars = ax.barh(cities, population, color=colors, height=0.6)

# Set the title and labels
ax.set_title('Population of Various Cities', fontsize=16)
ax.set_ylabel('City', fontsize=12)
ax.set_xlabel('Population', fontsize=12)

# Customize the tick labels
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Set y-axis limit
ax.set_xlim(300000, 9000000)

# Add the data values on the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 50000
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}', va='center')

# Show the plot
plt.tight_layout()
plt.show()