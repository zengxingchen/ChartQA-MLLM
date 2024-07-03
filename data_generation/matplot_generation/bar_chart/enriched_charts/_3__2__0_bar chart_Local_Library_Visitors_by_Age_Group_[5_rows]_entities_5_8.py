
import matplotlib.pyplot as plt

# Data
countries = [
    "United States", "China", "Japan", "Great Britain", "ROC", "Australia", 
    "Netherlands", "France", "Germany", "Italy", "Canada", "Brazil", 
    "New Zealand", "Cuba", "Hungary", "South Korea", "Poland", 
    "Czech Republic", "Kenya", "Norway"
]
gold_medals = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6, 6, 4, 4, 4, 4]
silver_medals = [41, 32, 14, 21, 28, 7, 12, 12, 11, 10, 6, 6, 6, 3, 7, 4, 5, 4, 4, 2]
bronze_medals = [33, 18, 17, 22, 23, 22, 14, 11, 16, 20, 11, 8, 7, 5, 7, 10, 5, 3, 2, 2]

# Colors for each country
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#c4e17f', '#76d7c4', '#f7b7a3', '#b2ad7f',
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#c4e17f', '#76d7c4', '#f7b7a3', '#b2ad7f'
]

# Plot
fig, ax = plt.subplots(figsize=(15, 10))  # Adjusted size for horizontal layout
bars = ax.barh(countries, gold_medals, color=colors, height=0.6)  # Adjusted bar height to 0.6

# Set the title and labels
ax.set_title('Olympic Gold Medals by Country', fontsize=18, pad=15)
ax.set_xlabel('Number of Gold Medals', fontsize=12)
ax.set_ylabel('Country', fontsize=12)

# Customize the tick labels
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Add the data values on the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 1
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}', va='center')

# Show the plot
plt.tight_layout()
plt.show()