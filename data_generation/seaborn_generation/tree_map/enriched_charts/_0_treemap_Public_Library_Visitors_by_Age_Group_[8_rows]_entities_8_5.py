
import matplotlib.pyplot as plt
import squarify

# Data points for the treemap
categories = ['Oak', 'Maple', 'Pine', 'Willow', 'Birch', 'Redbud', 'Cherry', 'Aspen', 'Magnolia', 'Elm', 'Spruce', 'Cedar', 'Walnut', 'Hemlock']
count = [1200, 950, 800, 640, 500, 320, 300, 250, 200, 180, 160, 140, 120, 100]

# TreeMap customization
color_palette = ['#457b9d', '#1d3557', '#a8dadc', '#f1faee', '#e63946', '#f4a261', '#ddbea9', '#2a9d8f', '#e76f51', '#264653', '#2b2d42', '#8d99ae', '#edf2f4', '#06d6a0']
plt.figure(figsize=(16, 9))

# Creating the treemap
squarify.plot(sizes=count, label=categories, color=color_palette, alpha=0.7)

# Title and labels
plt.title('Distribution of Tree Types in the Urban Forest', fontsize=18, fontweight='bold')
plt.axis('off')

plt.show()