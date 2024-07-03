
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Science', 'Nature', 'Technology', 'Innovation', 'Discovery'],
    'Subcategory1': [15, 20, 25, 30, 10],
    'Subcategory2': [25, 30, 20, 25, 35],
    'Subcategory3': [35, 25, 30, 20, 25],
    'Subcategory4': [25, 25, 25, 25, 30]
}

categories = data['Category']
subcategory1 = data['Subcategory1']
subcategory2 = data['Subcategory2']
subcategory3 = data['Subcategory3']
subcategory4 = data['Subcategory4']

barWidth = 0.5
bars1 = np.array(subcategory1)
bars2 = np.array(subcategory2)
bars3 = np.array(subcategory3)
bars4 = np.array(subcategory4)

r = np.arange(len(categories))

plt.figure(figsize=(10, 8))

plt.barh(r, bars1, color='#FF5733', edgecolor='grey', height=barWidth)
plt.barh(r, bars2, left=bars1, color='#33FF57', edgecolor='grey', height=barWidth)
plt.barh(r, bars3, left=bars1+bars2, color='#3357FF', edgecolor='grey', height=barWidth)
plt.barh(r, bars4, left=bars1+bars2+bars3, color='#FF33A1', edgecolor='grey', height=barWidth)

plt.xlabel('Percentage')
plt.ylabel('Categories')
plt.title('Distribution of Categories in Science & Nature')

plt.yticks(r, categories)

plt.legend(['Subcategory1', 'Subcategory2', 'Subcategory3', 'Subcategory4'], loc='lower right')

plt.show()