
import matplotlib.pyplot as plt

# Data
categories = ['Breakfast', 'Lunch', 'Dinner']
protein = [20, 30, 25]
carbohydrates = [50, 60, 40]
fats = [10, 20, 15]

# Offsets for stacked bars
left_offset_protein = [0, 0, 0]
left_offset_carbohydrates = [a+b for a, b in zip(left_offset_protein, protein)]
left_offset_fats = [a+b for a, b in zip(left_offset_carbohydrates, carbohydrates)]

# Create vertical bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Changed chart size

# Stacked bars
ax.bar(categories, protein, width=0.5, bottom=left_offset_protein, color='#FFA07A')  # Light Salmon
ax.bar(categories, carbohydrates, width=0.5, bottom=left_offset_carbohydrates, color='#20B2AA')  # Light Sea Green
ax.bar(categories, fats, width=0.5, bottom=left_offset_fats, color='#9370DB')  # Medium Purple

# Add some text for labels, title, and custom y-axis tick labels, etc.
ax.set_ylabel('Grams')
ax.set_title('Daily Nutritional Intake')
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories)

# Display the legend
ax.legend(['Protein', 'Carbohydrates', 'Fats'], loc='upper left')

# Add numerical labels on bars
for i, (p, c, f) in enumerate(zip(protein, carbohydrates, fats)):
    ax.text(i, p / 2, str(p), ha='center', va='center', color='black')
    ax.text(i, p + c / 2, str(c), ha='center', va='center', color='black')
    ax.text(i, p + c + f / 2, str(f), ha='center', va='center', color='black')

# Display the plot
plt.tight_layout()
plt.show()