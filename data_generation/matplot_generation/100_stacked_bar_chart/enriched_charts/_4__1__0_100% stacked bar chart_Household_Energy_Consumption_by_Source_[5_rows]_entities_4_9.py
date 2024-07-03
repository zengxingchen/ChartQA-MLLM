
import matplotlib.pyplot as plt
import numpy as np

# Data
foods = ['Chicken', 'Beef', 'Tofu', 'Salmon', 'Lentils', 'Rice', 'Broccoli', 'Almonds', 'Eggs', 'Yogurt', 
         'Quinoa', 'Pasta', 'Bread', 'Beans', 'Cheese', 'Milk', 'Nuts', 'Peas', 'Oats', 'Bananas', 'Spinach']
philosophy = np.array([35, 40, 30, 50, 20, 5, 30, 15, 25, 15, 25, 10, 15, 25, 35, 30, 20, 20, 25, 5, 30])
ethics = np.array([30, 25, 45, 20, 50, 60, 45, 30, 30, 40, 55, 50, 60, 45, 25, 35, 25, 45, 50, 60, 50])
morality = np.array([35, 35, 25, 30, 30, 35, 25, 55, 45, 45, 20, 40, 25, 30, 40, 35, 55, 35, 25, 35, 20])

# Stacking the data
bottom1 = philosophy
bottom2 = philosophy + ethics

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF']

# Create vertical bar chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(foods, philosophy, color=colors[0], edgecolor='white', width=0.6, label='Philosophy')
ax.bar(foods, ethics, bottom=bottom1, color=colors[1], edgecolor='white', width=0.6, label='Ethics')
ax.bar(foods, morality, bottom=bottom2, color=colors[2], edgecolor='white', width=0.6, label='Morality')

# Add legend
ax.legend(loc='upper right')

# Title and labels
ax.set_title('Philosophical Perspectives in Different Foods', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Food')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Display the chart
plt.tight_layout()
plt.show()