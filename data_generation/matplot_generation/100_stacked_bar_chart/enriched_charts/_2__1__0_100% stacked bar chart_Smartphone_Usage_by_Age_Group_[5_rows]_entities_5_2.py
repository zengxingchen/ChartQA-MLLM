
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
calories = np.array([2500, 2300, 2600, 2400, 2550, 2450, 2700, 2500, 2400, 2600, 2550, 2450])
protein = np.array([150, 140, 160, 145, 155, 148, 165, 150, 145, 160, 155, 148])
fat = np.array([70, 65, 75, 68, 72, 70, 80, 72, 68, 75, 72, 70])
carbs = np.array([320, 310, 340, 315, 330, 320, 350, 330, 315, 340, 330, 320])

# Convert to percentages
total = calories + protein + fat + carbs
calories_percentage = calories / total
protein_percentage = protein / total
fat_percentage = fat / total
carbs_percentage = carbs / total

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

width = 0.6
ax.barh(months, calories_percentage, color='#FF9999', edgecolor='white', height=width, label='Calories')
ax.barh(months, protein_percentage, color='#66B3FF', edgecolor='white', height=width, left=calories_percentage, label='Protein')
ax.barh(months, fat_percentage, color='#99FF99', edgecolor='white', height=width, left=calories_percentage + protein_percentage, label='Fat')
ax.barh(months, carbs_percentage, color='#FFCC99', edgecolor='white', height=width, left=calories_percentage + protein_percentage + fat_percentage, label='Carbs')

ax.set_xlabel('Percentage')
ax.set_title('Monthly Nutrient Intake Distribution', pad=20)
ax.legend(loc='lower right', bbox_to_anchor=(1, 0.5))

plt.show()