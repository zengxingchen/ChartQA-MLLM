
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
apples = [10, 15, 20, 30, 25, 35, 25, 30, 20, 15, 20, 25, 30, 35, 40, 30, 20, 25, 30, 25]
oranges = [20, 25, 30, 25, 30, 25, 35, 25, 30, 35, 25, 20, 30, 25, 20, 25, 30, 25, 20, 30]
bananas = [30, 35, 25, 20, 30, 20, 20, 25, 25, 25, 30, 30, 20, 25, 25, 25, 20, 30, 25, 25]
grapes = [40, 25, 25, 25, 15, 20, 20, 20, 25, 25, 25, 25, 20, 15, 15, 20, 30, 20, 25, 20]

# Normalize data to percentages
total = np.array(apples) + np.array(oranges) + np.array(bananas) + np.array(grapes)
apples = np.array(apples) / total * 100
oranges = np.array(oranges) / total * 100
bananas = np.array(bananas) / total * 100
grapes = np.array(grapes) / total * 100

# Plot
fig, ax = plt.subplots(figsize=(14, 8))
width = 0.6

ax.barh(categories, apples, color='#FF9999', edgecolor='white', height=width, label='Apples')
ax.barh(categories, oranges, left=apples, color='#66B2FF', edgecolor='white', height=width, label='Oranges')
ax.barh(categories, bananas, left=apples + oranges, color='#99FF99', edgecolor='white', height=width, label='Bananas')
ax.barh(categories, grapes, left=apples + oranges + bananas, color='#FFCC99', edgecolor='white', height=width, label='Grapes')

# Add title and labels
ax.set_title('Fruit Consumption by Category', fontsize=20, pad=20)
ax.set_xlabel('Percentage', fontsize=14)
ax.set_ylabel('Category', fontsize=14)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()