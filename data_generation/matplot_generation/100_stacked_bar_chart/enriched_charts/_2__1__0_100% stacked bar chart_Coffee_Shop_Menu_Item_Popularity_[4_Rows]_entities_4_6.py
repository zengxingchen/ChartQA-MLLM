
import matplotlib.pyplot as plt
import numpy as np

# Data
food_groups = ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meats']
carbohydrates = np.array([40, 30, 50, 30, 10])
proteins = np.array([5, 10, 15, 20, 30])
fats = np.array([2, 5, 3, 15, 25])
vitamins = np.array([30, 25, 15, 10, 5])
minerals = np.array([23, 30, 17, 25, 30])

# Normalize data to 100%
total = carbohydrates + proteins + fats + vitamins + minerals
carbohydrates = carbohydrates / total * 100
proteins = proteins / total * 100
fats = fats / total * 100
vitamins = vitamins / total * 100
minerals = minerals / total * 100

# Stack data
ind = np.arange(len(food_groups))
width = 0.6  # Width of the bars

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

p1 = ax.barh(ind, carbohydrates, width, color='#ff9999')
p2 = ax.barh(ind, proteins, width, left=carbohydrates, color='#66b3ff')
p3 = ax.barh(ind, fats, width, left=carbohydrates+proteins, color='#99ff99')
p4 = ax.barh(ind, vitamins, width, left=carbohydrates+proteins+fats, color='#ffcc99')
p5 = ax.barh(ind, minerals, width, left=carbohydrates+proteins+fats+vitamins, color='#c2c2f0')

ax.set_xlabel('Percentage')
ax.set_title('Daily Nutritional Intake by Food Group', pad=20)
ax.set_yticks(ind)
ax.set_yticklabels(food_groups)
ax.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('Carbohydrates', 'Proteins', 'Fats', 'Vitamins', 'Minerals'), bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()