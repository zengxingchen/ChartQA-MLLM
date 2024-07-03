
import matplotlib.pyplot as plt

# Data
categories = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']
fruits = [1.5, 1.2, 1.1, 0.7]
vegetables = [0.5, 1.7, 1.9, 0.6]
proteins = [1.0, 1.5, 2.2, 0.8]
grains = [1.0, 2.3, 2.7, 0.5]

# Offsets for stacked bars
bottom_offset_fruits = [0, 0, 0, 0]
bottom_offset_vegetables = [a+b for a, b in zip(bottom_offset_fruits, fruits)]
bottom_offset_proteins = [a+b for a, b in zip(bottom_offset_vegetables, vegetables)]
bottom_offset_grains = [a+b for a, b in zip(bottom_offset_proteins, proteins)]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))  # Changed chart size

# Stacked bars
ax.barh(categories, fruits, height=0.5, left=bottom_offset_fruits, color='#FFA07A')  # LightSalmon
ax.barh(categories, vegetables, height=0.5, left=bottom_offset_vegetables, color='#98FB98')  # PaleGreen
ax.barh(categories, proteins, height=0.5, left=bottom_offset_proteins, color='#4682B4')  # SteelBlue
ax.barh(categories, grains, height=0.5, left=bottom_offset_grains, color='#DAA520')  # GoldenRod

# Add some text for labels, title, and custom y-axis tick labels, etc.
ax.set_xlabel('Servings')
ax.set_title('Average Daily Nutrient Intake by Meal', pad=20)
ax.set_yticks(range(len(categories)))
ax.set_yticklabels(categories)
ax.set_ylabel('Meals')

# Display the legend
ax.legend(['Fruits', 'Vegetables', 'Proteins', 'Grains'], loc='lower right')

# Add numerical labels to each bar
for i in range(len(categories)):
    ax.text(fruits[i] / 2, i, str(fruits[i]), va='center', ha='center', color='black')
    ax.text(fruits[i] + vegetables[i] / 2, i, str(vegetables[i]), va='center', ha='center', color='black')
    ax.text(fruits[i] + vegetables[i] + proteins[i] / 2, i, str(proteins[i]), va='center', ha='center', color='black')
    ax.text(fruits[i] + vegetables[i] + proteins[i] + grains[i] / 2, i, str(grains[i]), va='center', ha='center', color='black')

# Display the plot
plt.tight_layout()
plt.show()