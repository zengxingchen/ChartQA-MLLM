
import matplotlib.pyplot as plt

# Data
countries = [
    "USA", "China", "Japan", "Great Britain", "ROC", "Australia", 
    "Netherlands", "France", "Germany", "Italy", "Canada", "Brazil", 
    "New Zealand", "Cuba", "Hungary"
]
gold = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
silver = [41, 32, 14, 21, 28, 7, 12, 12, 11, 10, 6, 6, 6, 3, 7]
bronze = [33, 18, 17, 22, 23, 22, 14, 11, 16, 20, 11, 8, 7, 5, 7]

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(14, 10))

# Horizontal bar chart
bars_gold = ax.barh(countries, gold, color='#FFD700', height=0.4, label='Gold')
bars_silver = ax.barh(countries, silver, left=gold, color='#C0C0C0', height=0.4, label='Silver')
bars_bronze = ax.barh(countries, bronze, left=[i+j for i,j in zip(gold, silver)], color='#CD7F32', height=0.4, label='Bronze')

# Set the title and labels
ax.set_title('Top 15 Countries by Olympic Medals in 2020 Tokyo Olympics', fontsize=18, pad=20)
ax.set_xlabel('Number of Medals', fontsize=14)
ax.set_ylabel('Country', fontsize=14)

# Remove the spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Set grid to be behind the bars
ax.set_axisbelow(True)
ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

# Show Values on Bars
for bar in bars_gold:
    width = bar.get_width()
    label_x_pos = width - 3
    ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width}', ha='center', va='center', color='black')

for bar in bars_silver:
    width = bar.get_width()
    label_x_pos = bar.get_x() + width - 3
    ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width}', ha='center', va='center', color='black')

for bar in bars_bronze:
    width = bar.get_width()
    label_x_pos = bar.get_x() + width - 3
    ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width}', ha='center', va='center', color='black')

# Add a legend
ax.legend(loc='lower right', fontsize=12)

# Set the layout to be tight
plt.tight_layout()

# Show the plot
plt.show()