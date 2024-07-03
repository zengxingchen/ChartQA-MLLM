
import matplotlib.pyplot as plt
import squarify

categories = ['Oak', 'Maple', 'Pine', 'Willow', 'Birch', 'Redbud', 'Cherry', 'Aspen', 'Magnolia', 'Elm', 'Spruce', 'Cedar', 'Walnut', 'Hemlock', 'Fir', 'Hickory', 'Sycamore', 'Ash', 'Poplar', 'Beech']
count = [1200, 950, 800, 640, 500, 320, 300, 250, 200, 180, 160, 140, 120, 100, 90, 80, 70, 60, 50, 40]

color_palette = ['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a', '#b15928', '#a6cee3', '#b2df8a', '#fb9a99', '#fdbf6f', '#cab2d6', '#ffff99', '#ff33cc', '#cc33ff', '#66ff66', '#66ccff', '#ff6666', '#ffcc66', '#cccccc', '#99ff99']
plt.figure(figsize=(18, 10))

squarify.plot(sizes=count, label=categories, color=color_palette, alpha=0.8)

plt.title('Distribution of Tree Species in the Urban Forest', fontsize=22, fontweight='bold', pad=20)
plt.axis('off')

plt.show()