import matplotlib.pyplot as plt
import squarify

# Data points
vegetables = ['Tomato', 'Potato', 'Onion', 'Carrot', 'Broccoli', 'Spinach', 
              'Pepper', 'Cucumber', 'Lettuce', 'Cabbage', 'Other']
market_share = [20.7, 18.5, 15.4, 12.3, 8.6, 7.2, 5.9, 3.8, 3.2, 2.4, 2]

# Color scheme
colors = ['#DC143C', '#FF6347', '#FF8C00', '#98FB98', '#32CD32', '#8FBC8F', 
          '#FFD700', '#00CED1', '#6A5ACD', '#4B0082', '#D3D3D3']

plt.figure(figsize=(16, 12))
squarify.plot(sizes=market_share, label=vegetables, color=colors, alpha=0.8)

# Chart details
plt.title('Vegetable Market Share in 2023', fontsize=18, pad=20)
plt.axis('off')

plt.show()