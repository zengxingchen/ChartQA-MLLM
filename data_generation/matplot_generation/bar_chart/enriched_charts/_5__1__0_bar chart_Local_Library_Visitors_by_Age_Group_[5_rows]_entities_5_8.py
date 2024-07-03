
import matplotlib.pyplot as plt

# Data
countries = [
    "China", "USA", "Germany", "India", "Japan", 
    "Australia", "Italy", "Spain", "France", "UK", 
    "South Korea", "Brazil", "Mexico", "Canada", "Russia"
]
solar_energy_production = [1000, 850, 600, 550, 450, 400, 300, 280, 250, 200, 180, 150, 120, 100, 80]

# Colors for each country
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8F33',
    '#8D33FF', '#33FFBD', '#FF3387', '#33FFF3', '#FF8F33',
    '#5733FF', '#33A6FF', '#8F33FF', '#57FF33', '#FF3357'
]

# Plot
fig, ax = plt.subplots(figsize=(10, 14))
bars = ax.barh(countries, solar_energy_production, color=colors, height=0.7)

# Set the title and labels
ax.set_title('Top Countries by Solar Energy Production', fontsize=16)
ax.set_xlabel('Solar Energy Production (GW)', fontsize=13)
ax.set_ylabel('Country', fontsize=13)

# Customize the tick labels
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Set y-axis limits
ax.set_xlim(70, 1050)

# Add the data values on the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 20
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width} GW', ha='center', va='center')

# Show the plot
plt.tight_layout()
plt.show()