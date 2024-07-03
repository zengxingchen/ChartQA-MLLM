
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
rainfall = [
    942, 1570, 1200, 384, 990, 1260, 210, 1040, 800, 260, 
    940, 400, 860, 1300, 820, 940, 1120, 380, 1050, 830, 
    1050, 1140, 1200, 1080, 1360, 800, 1150, 115, 1575, 1020
]

# Colors for each city
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

# Plot
fig, ax = plt.subplots(figsize=(14, 10))
bars = ax.bar(cities, rainfall, color=colors, width=0.6)

# Set the title and labels
ax.set_title('Annual Rainfall in Various Cities', fontsize=16)
ax.set_xlabel('City', fontsize=12)
ax.set_ylabel('Annual Rainfall (mm)', fontsize=12)

# Customize the tick labels
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)

# Add the data values on the bars
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 20
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height} mm', ha='center')

# Show the plot
plt.tight_layout()
plt.show()