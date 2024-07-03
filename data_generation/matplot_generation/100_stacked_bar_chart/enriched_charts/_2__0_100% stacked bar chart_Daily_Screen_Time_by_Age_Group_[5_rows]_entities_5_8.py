
import matplotlib.pyplot as plt
import numpy as np

# Data
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
apple = np.array([15, 20, 30, 25, 20, 10, 20, 25, 30, 15])
banana = np.array([25, 20, 15, 20, 25, 30, 15, 10, 20, 25])
orange = np.array([35, 30, 25, 20, 15, 20, 30, 20, 25, 30])
strawberry = np.array([10, 20, 20, 15, 20, 25, 20, 30, 15, 15])
grape = np.array([15, 10, 10, 20, 20, 15, 15, 15, 10, 15])

# Data for stacking
data = np.vstack([apple, banana, orange, strawberry, grape])
data_cumsum = np.cumsum(data, axis=0)

# Colors
colors = ['#FF5733', '#33FF57', '#5733FF', '#FF33A1', '#33FFF5']

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.5

for i, (color, label) in enumerate(zip(colors, ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grape'])):
    if i == 0:
        ax.barh(cities, data[i], color=color, edgecolor='white', height=bar_width, label=label)
    else:
        ax.barh(cities, data[i], left=data_cumsum[i-1], color=color, edgecolor='white', height=bar_width, label=label)

# Title and labels
ax.set_title('Fruit Consumption Distribution Across Major US Cities', fontsize=16, pad=15)
ax.set_xlabel('Percentage of Total Consumption', fontsize=12)
ax.set_ylabel('City', fontsize=12)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Display
plt.tight_layout()
plt.show()