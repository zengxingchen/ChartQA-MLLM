
import matplotlib.pyplot as plt

# Data
categories = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']
fruits = [1.5, 1.0, 1.0, 0.5]
vegetables = [0.5, 1.5, 2.0, 0.5]
proteins = [1.0, 1.5, 2.0, 0.5]
grains = [1.0, 2.0, 2.5, 0.5]

# Offsets for stacked bars
bottom_offset_fruits = [0, 0, 0, 0]
bottom_offset_vegetables = [a+b for a, b in zip(bottom_offset_fruits, fruits)]
bottom_offset_proteins = [a+b for a, b in zip(bottom_offset_vegetables, vegetables)]
bottom_offset_grains = [a+b for a, b in zip(bottom_offset_proteins, proteins)]

# Create vertical bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Changed chart size

# Stacked bars
ax.bar(categories, fruits, width=0.5, bottom=bottom_offset_fruits, color='#FF6347')  # Tomato
ax.bar(categories, vegetables, width=0.5, bottom=bottom_offset_vegetables, color='#3CB371')  # MediumSeaGreen
ax.bar(categories, proteins, width=0.5, bottom=bottom_offset_proteins, color='#1E90FF')  # DodgerBlue
ax.bar(categories, grains, width=0.5, bottom=bottom_offset_grains, color='#FFD700')  # Gold

# Add some text for labels, title, and custom y-axis tick labels, etc.
ax.set_ylabel('Servings')
ax.set_title('Average Daily Food Consumption by Meal')
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories)
ax.set_xlabel('Meals')

# Display the legend
ax.legend(['Fruits', 'Vegetables', 'Proteins', 'Grains'], loc='upper left')

# Display the plot
plt.tight_layout()

plt.show()