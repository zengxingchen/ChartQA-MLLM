
import matplotlib.pyplot as plt

# Data
countries = ['USA', 'Canada', 'Germany', 'France', 'Japan', 'China', 'India', 'Brazil', 'Australia', 'South Africa']
protein = [80, 70, 75, 65, 60, 50, 55, 65, 70, 60]
carbohydrates = [150, 130, 140, 120, 110, 100, 105, 115, 125, 115]
fats = [60, 55, 50, 45, 40, 35, 33, 40, 50, 45]
fibers = [30, 28, 27, 25, 20, 18, 17, 22, 26, 24]

# Colors for each nutrient
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Figure size
plt.figure(figsize=(12, 10))

# Bar widths (change to height for vertical bars)
bar_width = 0.5

# Plotting
plt.bar(countries, protein, color=colors[0], edgecolor='white', width=bar_width, label='Protein')
plt.bar(countries, carbohydrates, bottom=protein, color=colors[1], edgecolor='white', width=bar_width, label='Carbohydrates')
plt.bar(countries, fats, bottom=[protein[i] + carbohydrates[i] for i in range(len(fats))], color=colors[2], edgecolor='white', width=bar_width, label='Fats')
plt.bar(countries, fibers, bottom=[protein[i] + carbohydrates[i] + fats[i] for i in range(len(fibers))], color=colors[3], edgecolor='white', width=bar_width, label='Fibers')

# Labels and Title
plt.ylabel('Nutrient Intake (grams)')
plt.title('Nutrient Intake by Country')
plt.legend(loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()