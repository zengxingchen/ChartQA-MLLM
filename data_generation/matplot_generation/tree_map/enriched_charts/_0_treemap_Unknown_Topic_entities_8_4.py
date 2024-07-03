
import matplotlib.pyplot as plt
import squarify

# Data
brands = ['Samsung', 'Apple', 'Xiaomi', 'Oppo', 'Vivo', 'Huawei', 'Realme', 'Motorola', 'OnePlus', 'Google', 'Others']
market_share = [21.4, 18.3, 12.2, 10.5, 8.7, 7.6, 6.8, 3.9, 2.3, 2.0, 6.3]
colors = ['#FFD700', '#AFEEEE', '#DE3163', '#FF8C00', '#98FB98', '#D2691E', '#6495ED', '#DC143C', '#F0E68C', '#FF69B4', '#A9A9A9']

# Create a figure with specified size
plt.figure(figsize=(14, 8))

# Create a treemap with the above data
squarify.plot(sizes=market_share, label=brands, color=colors, alpha=0.7)

# Title of the treemap
plt.title('Global Smartphone Market Share in 2023', fontsize=18)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()