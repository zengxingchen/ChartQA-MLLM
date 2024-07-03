
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Item': ['Shirts', 'Pants', 'Dresses', 'Jackets', 'Shoes', 'Hats', 
             'Scarves', 'Gloves', 'Belts', 'Bags', 'Ties', 'Socks', 
             'Watches', 'Jewelry', 'Sunglasses'],
    'Quantity': [45, 30, 25, 20, 15, 10, 8, 7, 5, 4, 3, 2, 1, 12, 6]
}

df = pd.DataFrame(data)

colors = ['#FF6347', '#4682B4', '#9ACD32', '#FFD700', '#40E0D0', '#FF69B4', 
          '#CD5C5C', '#4B0082', '#BDB76B', '#8FBC8F', '#00CED1', '#FF4500', 
          '#DA70D6', '#F0E68C', '#5F9EA0']

fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, aspect="auto")

squarify.plot(sizes=df['Quantity'], label=df['Item'], color=colors, alpha=0.8)

plt.title('Fashion Item Quantities', fontsize=22, pad=20)

plt.axis('off')

plt.show()