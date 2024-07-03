
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
calories = [1800, 1750, 1850, 1900, 2000, 2100, 2200, 2150, 2050, 1950, 1850, 1750]
fat = [70, 68, 72, 74, 78, 80, 85, 83, 79, 76, 73, 70]
protein = [90, 88, 92, 95, 100, 105, 110, 108, 102, 98, 94, 90]

# Plot setup
fig, ax = plt.subplots(figsize=(14,8))

# Create bar chart
bar_width = 0.25
bar_locations_cal = range(len(calories))
bar_locations_fat = [x + bar_width for x in bar_locations_cal]
bar_locations_prot = [x + bar_width for x in bar_locations_fat]

bars1 = ax.barh(bar_locations_cal, calories, bar_width, label='Calories (kcal)', color='#4CAF50')
bars2 = ax.barh(bar_locations_fat, fat, bar_width, label='Fat (g)', color='#FF9800')
bars3 = ax.barh(bar_locations_prot, protein, bar_width, label='Protein (g)', color='#2196F3')

# Set the position of the y ticks
ax.set_yticks([r + bar_width for r in range(len(calories))])
ax.set_yticklabels(months)

# Adding labels and title
plt.xlabel('Measurements')
plt.title('Monthly Nutritional Intake')
ax.legend(loc='lower right')

# Display the plot
plt.tight_layout()
plt.show()