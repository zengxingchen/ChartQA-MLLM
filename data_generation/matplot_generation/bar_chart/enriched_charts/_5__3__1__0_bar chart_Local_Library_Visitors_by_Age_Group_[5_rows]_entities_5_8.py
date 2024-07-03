
import matplotlib.pyplot as plt

# Data
countries = [
    "USA", "Russia", "China", "Japan", "India", 
    "Europe", "Israel", "North Korea", "South Korea", "Iran", 
    "Brazil", "Australia", "UK", "Canada", "New Zealand"
]
total_space_missions = [339, 172, 134, 54, 46, 32, 16, 10, 8, 7, 6, 5, 4, 3, 2]

# Colors for each country
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8F33',
    '#8D33FF', '#33FFBD', '#FF3387', '#33FFF3', '#FF8F33',
    '#5733FF', '#33A6FF', '#8F33FF', '#57FF33', '#FF3357'
]

# Plot
fig, ax = plt.subplots(figsize=(16, 10))
bars = ax.bar(countries, total_space_missions, color=colors, width=0.6)

# Set the title and labels
ax.set_title('Top Countries by Total Space Missions', fontsize=18, pad=20)
ax.set_ylabel('Total Space Missions', fontsize=14)
ax.set_xlabel('Country', fontsize=14)

# Customize the tick labels
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)

# Set y-axis limits
ax.set_ylim(0, 350)

# Add the data values on the bars
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 5
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height}', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()