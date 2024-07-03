
import matplotlib.pyplot as plt
import squarify

categories = ['Apples', 'Bananas', 'Oranges', 'Strawberries', 'Grapes', 'Blueberries', 'Cherries', 'Peaches', 'Pineapples', 'Mangoes', 'Watermelons', 'Kiwis', 'Plums', 'Pomegranates', 'Avocados', 'Figs', 'Pears', 'Lemons', 'Limes', 'Grapefruits']
count = [1500, 1200, 900, 700, 600, 500, 450, 400, 350, 300, 250, 220, 200, 180, 150, 120, 100, 80, 60, 50]

color_palette = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ff9999', '#66b3ff', '#ffcc99', '#ffb3e6', '#c2c2f0', '#99ff99', '#ff9999', '#66b3ff', '#ffcc99', '#ffb3e6', '#c2c2f0', '#99ff99', '#ff9999']
plt.figure(figsize=(20, 12))

squarify.plot(sizes=count, label=categories, color=color_palette, alpha=0.8)

plt.title('Distribution of Various Food Items in Inventory', fontsize=22, fontweight='bold', pad=20)
plt.axis('off')

plt.show()