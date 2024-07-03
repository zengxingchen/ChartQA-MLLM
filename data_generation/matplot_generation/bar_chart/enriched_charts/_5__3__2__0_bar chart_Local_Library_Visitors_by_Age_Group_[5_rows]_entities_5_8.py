
import matplotlib.pyplot as plt

# Data
countries = [
    "China", "United States", "Brazil", "India", "Germany", 
    "Canada", "Russia", "Japan", "Norway", "Italy", 
    "France", "Spain", "United Kingdom", "Sweden", "Australia", 
    "South Korea", "Mexico", "Indonesia", "Turkey", "Netherlands"
]
renewable_energy_production = [
    2950, 1220, 850, 820, 500, 
    480, 430, 370, 340, 320, 
    310, 300, 290, 270, 260, 
    250, 240, 230, 220, 210
]

# Colors for each country
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF',
    '#33FFF7', '#FF8F33', '#8FFF33', '#3375FF', '#F733FF',
    '#75FF33', '#FF3333', '#33FFD4', '#D433FF', '#33A8FF',
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF'
]

# Plot
fig, ax = plt.subplots(figsize=(12, 8))  # Adjusted size for vertical layout
bars = ax.bar(countries, renewable_energy_production, color=colors, width=0.6)  # Adjusted bar width to 0.6

# Set the title and labels
ax.set_title('Top Countries by Renewable Energy Production (TWh)', fontsize=18, pad=20)
ax.set_xlabel('Country', fontsize=12)
ax.set_ylabel('Renewable Energy Production (TWh)', fontsize=12)

# Customize the tick labels
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)

# Set y-axis limits
ax.set_ylim(200, 3100)

# Add the data values on the bars
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 20
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height}', ha='center')

# Show the plot
plt.tight_layout()
plt.show()