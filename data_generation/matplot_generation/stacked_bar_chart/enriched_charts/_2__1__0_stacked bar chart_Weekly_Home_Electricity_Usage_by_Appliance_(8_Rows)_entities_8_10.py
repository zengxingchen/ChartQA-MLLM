
import matplotlib.pyplot as plt

# Data
countries = ['USA', 'Canada', 'Germany', 'France', 'Japan', 'China', 'India', 'Brazil', 'Australia', 'South Africa', 'UK', 'Italy', 'Spain', 'Russia', 'Mexico']
proteins = [90, 85, 80, 75, 70, 65, 60, 78, 82, 76, 88, 77, 74, 81, 79]
carbohydrates = [160, 140, 145, 135, 130, 120, 115, 125, 130, 120, 150, 140, 138, 135, 130]
fats = [70, 65, 60, 55, 50, 45, 40, 48, 52, 50, 68, 55, 53, 59, 58]
fibers = [35, 32, 30, 28, 25, 22, 20, 23, 27, 26, 34, 29, 28, 30, 31]

# Colors for each nutrient
colors = ['#FF5733','#33FF57','#3357FF','#FF33A6']

# Figure size
plt.figure(figsize=(14, 8))

# Bar widths
bar_width = 0.4

# Plotting
plt.bar(countries, proteins, color=colors[0], edgecolor='white', width=bar_width, label='Proteins')
plt.bar(countries, carbohydrates, bottom=proteins, color=colors[1], edgecolor='white', width=bar_width, label='Carbohydrates')
plt.bar(countries, fats, bottom=[proteins[i] + carbohydrates[i] for i in range(len(fats))], color=colors[2], edgecolor='white', width=bar_width, label='Fats')
plt.bar(countries, fibers, bottom=[proteins[i] + carbohydrates[i] + fats[i] for i in range(len(fibers))], color=colors[3], edgecolor='white', width=bar_width, label='Fibers')

# Adding numerical labels
for i in range(len(countries)):
    plt.text(i, proteins[i] / 2, str(proteins[i]), ha='center', va='center', color='white', fontsize=9)
    plt.text(i, proteins[i] + carbohydrates[i] / 2, str(carbohydrates[i]), ha='center', va='center', color='white', fontsize=9)
    plt.text(i, proteins[i] + carbohydrates[i] + fats[i] / 2, str(fats[i]), ha='center', va='center', color='white', fontsize=9)
    plt.text(i, proteins[i] + carbohydrates[i] + fats[i] + fibers[i] / 2, str(fibers[i]), ha='center', va='center', color='white', fontsize=9)

# Labels and Title
plt.ylabel('Calorie Intake (grams)')
plt.title('Average Daily Calorie Intake by Country for Athletes')
plt.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()