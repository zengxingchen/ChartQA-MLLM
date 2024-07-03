
import matplotlib.pyplot as plt
import numpy as np

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
shirts = np.array([20, 25, 30, 15, 10, 20, 25, 20, 30, 15])
pants = np.array([15, 20, 15, 25, 20, 15, 30, 15, 20, 25])
shoes = np.array([30, 25, 20, 15, 20, 25, 20, 25, 15, 20])
hats = np.array([25, 20, 15, 25, 30, 20, 15, 15, 20, 20])
accessories = np.array([10, 10, 20, 20, 20, 20, 10, 25, 15, 20])

data = np.vstack([shirts, pants, shoes, hats, accessories])
data_cumsum = np.cumsum(data, axis=0)

colors = ['#8B0000', '#FF4500', '#FFD700', '#32CD32', '#1E90FF']

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.35

for i, (color, label) in enumerate(zip(colors, ['Shirts', 'Pants', 'Shoes', 'Hats', 'Accessories'])):
    if i == 0:
        ax.bar(cities, data[i], color=color, edgecolor='white', width=bar_width, label=label)
    else:
        ax.bar(cities, data[i], bottom=data_cumsum[i-1], color=color, edgecolor='white', width=bar_width, label=label)

ax.set_title('Fashion Item Sales Distribution Across Major US Cities', fontsize=18, pad=20)
ax.set_ylabel('Percentage of Total Sales', fontsize=14)
ax.set_xlabel('City', fontsize=14)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()