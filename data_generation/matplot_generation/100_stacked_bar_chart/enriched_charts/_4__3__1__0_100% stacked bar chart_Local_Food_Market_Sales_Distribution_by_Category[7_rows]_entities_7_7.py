
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Chicken Breast', 'Salmon', 'Almonds', 'Broccoli', 'Apple', 'Milk', 'Cheese', 'Yogurt', 'Bread', 'Egg', 'Avocado', 'Tofu', 'Rice', 'Beans', 'Quinoa', 'Peanut Butter', 'Spinach', 'Oats', 'Banana', 'Lentils', 'Cottage Cheese', 'Walnuts', 'Hummus', 'Kale', 'Chia Seeds', 'Pumpkin Seeds', 'Peas', 'Cashews', 'Pistachios', 'Sunflower Seeds']
protein = [80, 70, 13, 30, 2, 21, 25, 24, 10, 35, 5, 40, 7, 25, 14, 25, 4, 17, 1, 29, 31, 15, 12, 10, 16, 19, 5, 18, 21, 17]
carbohydrates = [0, 0, 15, 60, 95, 49, 3, 50, 85, 2, 10, 8, 90, 65, 68, 20, 80, 66, 93, 59, 6, 13, 58, 85, 46, 34, 74, 30, 28, 22]
fat = [20, 30, 72, 10, 3, 30, 72, 26, 5, 63, 85, 52, 3, 10, 18, 55, 16, 17, 6, 12, 63, 72, 30, 5, 38, 47, 21, 52, 51, 61]

# Parameters
bar_width = 0.4
fig_width = 10
fig_height = 14

# Colors
colors = ['#4CAF50', '#FFC107', '#F44336']

# Stack bar chart
fig, ax = plt.subplots(figsize=(fig_width, fig_height))
bar1 = np.array(protein)
bar2 = np.array(carbohydrates)
bar3 = np.array(fat)

bars = np.vstack([bar1, bar2, bar3])
category_positions = np.arange(len(categories))

# Create the bars
ax.bar(category_positions, bars[0], color=colors[0], edgecolor='white', width=bar_width, label='Protein (%)')
ax.bar(category_positions, bars[1], bottom=bars[0], color=colors[1], edgecolor='white', width=bar_width, label='Carbohydrates (%)')
ax.bar(category_positions, bars[2], bottom=bars[0]+bars[1], color=colors[2], edgecolor='white', width=bar_width, label='Fat (%)')

# X-axis labels
ax.set_xticks(category_positions)
ax.set_xticklabels(categories, rotation=90)

# Chart title and labels
ax.set_title('Macronutrient Composition of Various Foods', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Food Items')

# Legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

# Layout
plt.tight_layout()

# Show the plot
plt.show()