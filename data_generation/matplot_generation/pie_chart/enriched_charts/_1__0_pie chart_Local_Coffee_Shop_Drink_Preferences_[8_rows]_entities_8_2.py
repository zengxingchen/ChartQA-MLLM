
import matplotlib.pyplot as plt

# Data to plot
labels = 'Proteins', 'Carbohydrates', 'Fats', 'Vitamins', 'Minerals', 'Fiber', 'Water'
sizes = [25, 45, 20, 5, 3, 2, 30]
colors = ['#ff6347','#4682b4','#ffd700','#32cd32','#ff69b4','#8a2be2','#00ced1']

# Change the size of the figure (width, height)
plt.figure(figsize=(12, 8))

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Nutrient Composition in a Balanced Diet', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()