
import matplotlib.pyplot as plt

# Data
countries = [
    "USA", "China", "Japan", "Germany", "South Korea", 
    "India", "France", "UK", "Brazil", "Italy", 
    "Canada", "Russia", "Australia", "Spain", "Mexico"
]
rd_spending = [580, 490, 170, 120, 90, 60, 55, 50, 40, 35, 30, 25, 20, 15, 10]

# Colors for each country
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8F33',
    '#8D33FF', '#33FFBD', '#FF3387', '#33FFF3', '#FF8F33',
    '#5733FF', '#33A6FF', '#8F33FF', '#57FF33', '#FF3357'
]

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(countries, rd_spending, color=colors, height=0.6)

# Set the title and labels
ax.set_title('Top Countries by R&D Spending', fontsize=16, pad=20)
ax.set_xlabel('R&D Spending (Billion USD)', fontsize=13)
ax.set_ylabel('Country', fontsize=13)

# Customize the tick labels
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Set y-axis limit
ax.set_xlim(0, 600)

# Add the data values on the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 10
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width} B', ha='center', va='center')

# Show the plot
plt.tight_layout()
plt.show()