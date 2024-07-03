
import matplotlib.pyplot as plt
import numpy as np

# Data
drinks = ['Gatorade', 'Powerade', 'VitaminWater', 'BodyArmor', 'CoconutWater', 'ElectrolyteWater', 'EnergyDrink', 'ProteinShake', 'RecoveryDrink', 'SportsTea']
carbohydrates = np.array([21, 25, 13, 18, 9, 0, 29, 3, 17, 7])
proteins = np.array([0, 0, 0, 0, 1, 0, 1, 20, 8, 0])
fats = np.array([0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
fibers = np.array([0, 0, 0, 0, 0.5, 0, 0, 0, 0.5, 0.5])

# Normalizing data to percentage
totals = carbohydrates + proteins + fats + fibers
carbohydrates = carbohydrates / totals * 100
proteins = proteins / totals * 100
fats = fats / totals * 100
fibers = fibers / totals * 100

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

bar_width = 0.8
x = np.arange(len(drinks))

ax.bar(x, carbohydrates, color='#FF5733', edgecolor='grey', width=bar_width, label='Carbohydrates')
ax.bar(x, proteins, bottom=carbohydrates, color='#33FFBD', edgecolor='grey', width=bar_width, label='Proteins')
ax.bar(x, fats, bottom=carbohydrates + proteins, color='#FF33A6', edgecolor='grey', width=bar_width, label='Fats')
ax.bar(x, fibers, bottom=carbohydrates + proteins + fats, color='#3375FF', edgecolor='grey', width=bar_width, label='Fibers')

# Labels and Title
ax.set_ylabel('Percentage')
ax.set_title('Nutritional Composition of Different Sports Drinks', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(drinks, rotation=45, ha='right')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.15))

plt.tight_layout()
plt.show()