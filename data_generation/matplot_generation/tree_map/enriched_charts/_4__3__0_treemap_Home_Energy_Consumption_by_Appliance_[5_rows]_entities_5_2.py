
import matplotlib.pyplot as plt
import squarify

# Dataset
topics = [
    'Ancient Rome', 'Ancient Egypt', 'Medieval Europe', 'Ancient Greece', 'Mesoamerica', 
    'Ancient China', 'Indus Valley', 'Mesopotamia', 'Ancient Persia', 'Phoenicians', 
    'Carthage', 'Hittites', 'Byzantine Empire', 'Ottoman Empire', 'Minoans', 
    'Macedonian Empire', 'Celtic Europe', 'Viking Age', 'Mughal Empire', 'Achaemenid Empire'
]
values = [
    1200, 1500, 1300, 1100, 900, 
    1400, 950, 1200, 1250, 800, 
    850, 750, 1350, 1600, 700, 
    1450, 1000, 1100, 1300, 1250
]

# Color Scheme
colors = [
    '#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', 
    '#e6ab02', '#a6761d', '#666666', '#1b9e77', '#d95f02', 
    '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', 
    '#666666', '#1b9e77', '#d95f02', '#7570b3', '#e7298a'
]

plt.figure(figsize=(16, 12))

# Creating the treemap
squarify.plot(sizes=values, label=topics, color=colors, alpha=0.8)

# Adding a title
plt.title('Significant Historical Civilizations (Influence Score)', fontsize=18, weight='bold')

# Removing the axes
plt.axis('off')

# Display the plot
plt.show()