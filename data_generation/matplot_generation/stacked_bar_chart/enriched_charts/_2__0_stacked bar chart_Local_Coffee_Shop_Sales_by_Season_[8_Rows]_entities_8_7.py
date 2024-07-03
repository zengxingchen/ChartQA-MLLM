
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
protein = [50, 55, 60, 65, 70, 75, 80]
carbohydrates = [200, 210, 220, 230, 240, 250, 260]
fats = [70, 72, 75, 78, 80, 83, 85]

# Plot
fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(years, protein, color='#1f77b4', edgecolor='white', width=0.65, label='Protein (g)')
ax.bar(years, carbohydrates, bottom=protein, color='#ff7f0e', edgecolor='white', width=0.65, label='Carbohydrates (g)')
ax.bar(years, fats, bottom=[i + j for i, j in zip(protein, carbohydrates)], color='#2ca02c', edgecolor='white', width=0.65, label='Fats (g)')

# Labels and Title
ax.set_ylabel('Nutrient Intake (grams)')
ax.set_title('Annual Nutrient Intake from 2015 to 2021', pad=20)
ax.legend(loc='upper left')

# Display the plot
plt.show()