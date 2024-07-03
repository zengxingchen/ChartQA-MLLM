
import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ['USA', 'Canada', 'Australia', 'Germany', 'France', 'Brazil', 'India', 'China', 'South Africa', 'Japan']
protein = [25, 20, 30, 25, 20, 35, 25, 20, 30, 25]
carbs = [35, 40, 30, 25, 30, 20, 35, 40, 30, 25]
fat = [20, 25, 15, 25, 20, 25, 15, 15, 20, 20]
fiber = [10, 10, 15, 15, 20, 10, 15, 15, 10, 15]
sugar = [10, 5, 10, 10, 10, 10, 10, 10, 10, 15]

# Plot
fig, ax = plt.subplots(figsize=(10, 12))
width = 0.6  # width of the bars

# Colors
colors = ['#FF4500', '#32CD32', '#1E90FF', '#FFD700', '#6A5ACD']

# Stacked bar chart
ax.bar(countries, protein, color=colors[0], edgecolor='white', width=width)
ax.bar(countries, carbs, bottom=np.array(protein), color=colors[1], edgecolor='white', width=width)
ax.bar(countries, fat, bottom=np.array(protein) + np.array(carbs), color=colors[2], edgecolor='white', width=width)
ax.bar(countries, fiber, bottom=np.array(protein) + np.array(carbs) + np.array(fat), color=colors[3], edgecolor='white', width=width)
ax.bar(countries, sugar, bottom=np.array(protein) + np.array(carbs) + np.array(fat) + np.array(fiber), color=colors[4], edgecolor='white', width=width)

# Title and labels
ax.set_title('Nutritional Composition by Country', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Country')

# Legend
ax.legend(['Protein', 'Carbs', 'Fat', 'Fiber', 'Sugar'], loc='upper left', bbox_to_anchor=(1, 1))

# Show plot
plt.tight_layout()
plt.show()