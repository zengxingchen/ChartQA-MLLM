
import matplotlib.pyplot as plt
import squarify

# Data points
fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grapes', 'Mango', 'Blueberry', 
          'Pineapple', 'Peach', 'Watermelon', 'Others']
market_share = [34.6, 22.4, 17.8, 9.1, 5.7, 4.9, 2.6, 1.9, 0.8, 0.6, 0.6]

# Color scheme
colors = ['#FF4500', '#FFD700', '#FFA500', '#FF69B4', '#8A2BE2', '#00FF00', '#1E90FF', 
          '#FF6347', '#FFDAB9', '#00CED1', '#D3D3D3']

plt.figure(figsize=(14, 10))
squarify.plot(sizes=market_share, label=fruits, color=colors, alpha=0.7)

# Chart details
plt.title('Popular Fruit Market Share in 2023')
plt.axis('off')

plt.show()