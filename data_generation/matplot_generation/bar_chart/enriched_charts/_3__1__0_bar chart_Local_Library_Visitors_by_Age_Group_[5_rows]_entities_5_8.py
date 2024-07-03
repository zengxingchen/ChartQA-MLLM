import matplotlib.pyplot as plt

# Data
countries = [
    "Argentina", "Brazil", "Germany", "France", "Italy", 
    "Spain", "Netherlands", "Portugal", "England", "Uruguay", 
    "Belgium", "Croatia", "Mexico", "Colombia", "Chile"
]
total_goals = [45, 40, 38, 35, 33, 32, 30, 28, 27, 25, 23, 22, 20, 18, 15]

# Colors for each country
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8F33',
    '#8D33FF', '#33FFBD', '#FF3387', '#33FFF3', '#FF8F33',
    '#5733FF', '#33A6FF', '#8F33FF', '#57FF33', '#FF3357'
]

# Plot
fig, ax = plt.subplots(figsize=(12, 16))
bars = ax.barh(countries, total_goals, color=colors, height=0.6)

# Set the title and labels
ax.set_title('Top Football Nations by Total Goals Scored in World Cup', fontsize=16, pad=20)
ax.set_xlabel('Total Goals Scored', fontsize=13)
ax.set_ylabel('Country', fontsize=13)

# Customize the tick labels
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Add the data values on the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 1
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}', va='center')

# Show the plot
plt.tight_layout()
plt.show()