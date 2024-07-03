
import matplotlib.pyplot as plt
import squarify

labels = [
    'Fruits', 'Vegetables', 'Grains', 'Proteins', 
    'Dairy', 'Fats', 'Sugars', 'Beverages', 
    'Snacks', 'Condiments', 'Seafood', 'Nuts', 
    'Spices', 'Legumes'
]
sizes = [18, 16, 14, 13, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2]
colors = [
    '#FFA07A', '#20B2AA', '#778899', '#FF6347', 
    '#4682B4', '#DAA520', '#32CD32', '#8B0000', 
    '#D2691E', '#9932CC', '#FFD700', '#CD5C5C', 
    '#FF4500', '#008080'
]

plt.figure(figsize=(16, 12))

squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

plt.title('Distribution of Food Categories in a Balanced Diet', fontsize=18)

plt.axis('off')

plt.show()