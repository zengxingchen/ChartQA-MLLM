
import matplotlib.pyplot as plt

# Data
countries = [
    "China", "USA", "Germany", "India", "Japan", 
    "Brazil", "UK", "France", "Canada", "Italy", 
    "Spain", "Australia", "South Korea", "Mexico", "Russia",
    "Norway", "Sweden", "Finland", "Denmark", "Netherlands",
    "Belgium", "Switzerland", "Austria", "Portugal"
]
renewable_capacity = [800, 300, 150, 100, 80, 75, 60, 55, 50, 45, 40, 35, 30, 25, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

# Colors for each country
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8F33',
    '#8D33FF', '#33FFBD', '#FF3387', '#33FFF3', '#FF8F33',
    '#5733FF', '#33A6FF', '#8F33FF', '#57FF33', '#FF3357',
    '#FFB533', '#33FFB5', '#B533FF', '#33B5FF', '#FF5733',
    '#33FF57', '#3357FF', '#FF33A6', '#FF8F33'
]

# Plot
fig, ax = plt.subplots(figsize=(12, 16))
bars = ax.barh(countries, renewable_capacity, color=colors, height=0.6)

# Set the title and labels
ax.set_title('Top Countries by Renewable Energy Capacity', fontsize=16)
ax.set_xlabel('Renewable Energy Capacity (GW)', fontsize=13)
ax.set_ylabel('Country', fontsize=13)

# Customize the tick labels
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Add the data values on the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 10
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width} GW', va='center')

# Show the plot
plt.tight_layout()
plt.show()