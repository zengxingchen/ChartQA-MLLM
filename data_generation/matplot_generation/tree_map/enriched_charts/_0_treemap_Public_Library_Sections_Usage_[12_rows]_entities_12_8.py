
import matplotlib.pyplot as plt
import squarify

# Data for manufacturers' market share
manufacturers = ['Samsung', 'Apple', 'Xiaomi', 'Vivo', 'Oppo', 'Huawei', 'Realme', 'Lenovo', 'Motorola', 'LG', 'Others']
market_share = [21.1, 16.0, 11.1, 8.6, 8.5, 4.6, 2.7, 2.4, 1.8, 1.2, 22.0]

# Custom color scheme
colors = ['#FFD700', '#FF8C00', '#FF6347', '#4682B4', '#6A5ACD', '#20B2AA', '#8FBC8F', '#D2691E', '#778899', '#FF69B4', '#7FFFD4']

# Treemap
plt.figure(figsize=(12, 8))  # Adjusting the size of the treemap
squarify.plot(sizes=market_share, label=manufacturers, color=colors, alpha=0.7)
plt.title('Smartphone Market Share Q1 2021')
plt.axis('off')  # No axes for a cleaner look

plt.show()