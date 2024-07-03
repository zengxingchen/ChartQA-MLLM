import matplotlib.pyplot as plt
import numpy as np

categories = ['Literature', 'Writing', 'Poetry', 'Fiction', 'Non-fiction', 
              'Biography', 'Essay', 'Drama', 'Philosophy', 'Criticism']
product_a = [25, 20, 35, 40, 30, 20, 25, 30, 35, 45]
product_b = [30, 25, 30, 25, 45, 35, 40, 20, 30, 25]
product_c = [45, 55, 35, 35, 25, 45, 35, 50, 35, 30]

data = np.array([product_a, product_b, product_c])
data_cum = data.cumsum(axis=0)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

fig, ax = plt.subplots(figsize=(12, 8))

for i, col in enumerate(colors):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(categories, heights, bottom=starts, width=0.6, color=col, label=f'Product {chr(65+i)}')

ax.legend(loc='upper left')

ax.set_ylabel('Percentage')
ax.set_title('Distribution of Products in Literature & Writing Categories', pad=20)

plt.tight_layout()
plt.show()