
import matplotlib.pyplot as plt
import numpy as np

categories = ['Shirts', 'Pants', 'Shoes', 'Accessories', 'Outerwear', 'Bags', 'Hats']
brand_a = [20, 35, 40, 15, 25, 30, 10]
brand_b = [50, 25, 35, 40, 35, 30, 50]
brand_c = [30, 40, 25, 45, 40, 40, 40]

barWidth = 0.6

r = np.arange(len(categories))

plt.figure(figsize=(12, 8))

plt.barh(r, brand_a, color='#FF5733', edgecolor='grey', height=barWidth, label='Brand A')
plt.barh(r, brand_b, left=brand_a, color='#33FF57', edgecolor='grey', height=barWidth, label='Brand B')
plt.barh(r, brand_c, left=np.add(brand_a, brand_b), color='#3357FF', edgecolor='grey', height=barWidth, label='Brand C')

plt.xlabel('Percentage')
plt.ylabel('Categories')
plt.title('Distribution of Product Sales by Brand')
plt.yticks(r, categories)
plt.legend(loc='upper right', bbox_to_anchor=(1, 1))

plt.show()