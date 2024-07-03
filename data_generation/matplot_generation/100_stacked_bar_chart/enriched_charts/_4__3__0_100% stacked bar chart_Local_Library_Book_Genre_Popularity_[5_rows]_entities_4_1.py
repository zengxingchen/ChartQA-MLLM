
import matplotlib.pyplot as plt
import numpy as np

categories = ['Shirts', 'Jeans', 'Dresses', 'Skirts', 'Jackets', 'Shoes', 'Accessories', 'Sportswear', 'Formalwear', 'Loungewear', 'Underwear', 'Swimwear', 'Hats', 'Scarves', 'Gloves', 'Socks', 'Sunglasses', 'Bags', 'Belts', 'Watches']
online = [45, 60, 50, 55, 70, 65, 40, 75, 30, 50, 35, 55, 60, 45, 50, 65, 40, 70, 30, 55]
in_person = [55, 40, 50, 45, 30, 35, 60, 25, 70, 50, 65, 45, 40, 55, 50, 35, 60, 30, 70, 45]

barWidth = 0.8
r = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(14, 10))

ax.bar(r, online, color='#1f77b4', edgecolor='grey', width=barWidth, label='Online')
ax.bar(r, in_person, bottom=online, color='#ff7f0e', edgecolor='grey', width=barWidth, label='In-Person')

ax.set_ylabel('Percentage')
ax.set_title('Fashion Item Sales Distribution', pad=20)
ax.set_xticks(r)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1.05))

plt.tight_layout()
plt.show()