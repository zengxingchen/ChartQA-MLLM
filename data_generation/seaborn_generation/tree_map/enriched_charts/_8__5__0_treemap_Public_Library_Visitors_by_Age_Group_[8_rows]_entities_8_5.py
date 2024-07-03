
import matplotlib.pyplot as plt
import squarify

categories = [
    'Oak', 'Maple', 'Pine', 'Willow', 'Birch', 'Redbud', 'Cherry', 'Aspen', 
    'Magnolia', 'Elm', 'Spruce', 'Cedar', 'Walnut', 'Hemlock', 'Fir', 
    'Hickory', 'Sycamore', 'Ash', 'Poplar', 'Beech'
]
count = [
    1200, 950, 850, 600, 540, 330, 280, 240, 220, 200, 180, 160, 150, 
    140, 130, 120, 110, 100, 90, 80
]
color_palette = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', 
    '#c2f0c2', '#ff6666', '#ffb3b3', '#66c2ff', '#b3b3ff', '#c2f0c2', 
    '#ff9999', '#99ccff', '#b3e6b3', '#ff9999', '#b3ffb3', '#b3b3ff', 
    '#e6b3e6', '#ffcc99'
]

plt.figure(figsize=(16, 9))

squarify.plot(sizes=count, label=categories, color=color_palette, alpha=0.8)

plt.title('Distribution of Tree Species in the Urban Forest', fontsize=22, fontweight='bold', pad=20)
plt.axis('off')

plt.show()