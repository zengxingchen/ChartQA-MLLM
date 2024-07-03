
import matplotlib.pyplot as plt
import squarify

# Data points for the treemap
categories = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Figs', 'Grapes', 'Honeydew', 'Kiwi', 'Lemon', 'Mango', 'Nectarine', 'Orange', 'Papaya', 'Quince', 'Raspberry', 'Strawberry', 'Tangerine']
count = [1500, 1200, 950, 700, 600, 550, 500, 450, 400, 350, 300, 250, 200, 180, 160, 140, 120, 100]

# TreeMap customization
color_palette = ['#8ecae6', '#219ebc', '#023047', '#ffb703', '#fb8500', '#ff5a5f', '#00a8e8', '#007ea7', '#00afb9', '#e29578', '#6d597a', '#355070', '#b56576', '#6d597a', '#ffc6ff', '#3a86ff', '#8338ec', '#ff006e']
plt.figure(figsize=(18, 10))

# Creating the treemap
squarify.plot(sizes=count, label=categories, color=color_palette, alpha=0.8)

# Title and labels
plt.title('Distribution of Fruit Consumption', fontsize=20, fontweight='bold', pad=20)
plt.axis('off')

plt.show()