
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Philosophy', 'Ethics', 'Logic', 'Metaphysics', 'Epistemology', 'Aesthetics'],
    'Subcategory1': [20, 15, 25, 30, 35, 25],
    'Subcategory2': [30, 35, 25, 20, 25, 20],
    'Subcategory3': [25, 30, 20, 25, 20, 30],
    'Subcategory4': [25, 20, 30, 25, 20, 25]
}

categories = data['Category']
subcategory1 = data['Subcategory1']
subcategory2 = data['Subcategory2']
subcategory3 = data['Subcategory3']
subcategory4 = data['Subcategory4']

barWidth = 0.75
bars1 = np.array(subcategory1)
bars2 = np.array(subcategory2)
bars3 = np.array(subcategory3)
bars4 = np.array(subcategory4)

r = np.arange(len(categories))

plt.figure(figsize=(12, 10))

plt.bar(r, bars1, color='#4B0082', edgecolor='grey', width=barWidth)
plt.bar(r, bars2, bottom=bars1, color='#8A2BE2', edgecolor='grey', width=barWidth)
plt.bar(r, bars3, bottom=bars1+bars2, color='#9370DB', edgecolor='grey', width=barWidth)
plt.bar(r, bars4, bottom=bars1+bars2+bars3, color='#BA55D3', edgecolor='grey', width=barWidth)

plt.ylabel('Percentage')
plt.xlabel('Categories')
plt.title('Distribution of Categories in Philosophy & Ethics')

plt.xticks(r, categories, rotation=45)

plt.legend(['Subcategory1', 'Subcategory2', 'Subcategory3', 'Subcategory4'], loc='upper right')

plt.show()