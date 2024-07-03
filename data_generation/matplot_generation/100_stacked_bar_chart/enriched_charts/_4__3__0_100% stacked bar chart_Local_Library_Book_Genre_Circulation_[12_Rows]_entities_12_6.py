
import matplotlib.pyplot as plt
import numpy as np

# Data
foods = ['Pasta', 'Beef', 'Yogurt', 'Spinach', 'Peanut Butter', 'Quinoa', 'Tofu', 'Avocado', 'Cheese', 'Almonds', 'Oatmeal', 'Eggplant', 'Turkey', 'Pumpkin Seeds', 'Lentils', 'Salmon']
carbs = [75, 0, 17, 3.6, 20, 21.3, 1.9, 8.5, 1.3, 21, 67, 6, 0, 15, 20, 0]
proteins = [13, 26, 10, 2.9, 25, 4.4, 8, 2, 25, 21, 17, 1, 29, 19, 25, 20]
fats = [1.5, 20, 3.5, 0.4, 50, 1.9, 4.8, 15, 33, 50, 7, 0.2, 4, 45, 1, 13]

# Colors
colors = ['#ff9999','#66b3ff','#99ff99']

# Stack data
ind = np.arange(len(foods))    # the x locations for the groups
width = 0.6       # the width of the bars: can also be len(x) sequence

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))  # Adjusted figure size for better clarity
p1 = ax.bar(ind, carbs, width, color=colors[0])
p2 = ax.bar(ind, proteins, width, bottom=carbs, color=colors[1])
p3 = ax.bar(ind, fats, width, bottom=np.array(carbs)+np.array(proteins), color=colors[2])

ax.set_title('Nutrient Distribution in Various Foods', pad=20)
ax.set_xlabel('Food Items')
ax.set_ylabel('Percentage')
ax.set_xticks(ind)
ax.set_xticklabels(foods, rotation=90)
ax.legend((p1[0], p2[0], p3[0]), ('Carbohydrates', 'Proteins', 'Fats'), loc='upper left')

# Show the plot
plt.show()