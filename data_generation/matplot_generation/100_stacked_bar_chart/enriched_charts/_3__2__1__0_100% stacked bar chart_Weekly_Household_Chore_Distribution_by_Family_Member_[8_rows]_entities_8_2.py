
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Apple', 'Banana', 'Carrot', 'Dates', 'Eggplant']
nutrients = ['Nutrient A', 'Nutrient B', 'Nutrient C', 'Nutrient D', 'Nutrient E']
data = np.array([
    [20, 15, 30, 25, 10],
    [25, 20, 15, 30, 10],
    [10, 20, 25, 30, 15],
    [35, 10, 15, 25, 15],
    [15, 25, 20, 25, 15]
])

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF']

# Normalize data to 100%
data_normalized = data / data.sum(axis=1)[:, np.newaxis] * 100

# Plot
fig, ax = plt.subplots(figsize=(10, 7))

# Stack bars horizontally
bottom = np.zeros(len(categories))
for i in range(data.shape[1]):
    ax.barh(categories, data_normalized[:, i], left=bottom, color=colors[i], label=nutrients[i])
    bottom += data_normalized[:, i]

# Add title and labels
ax.set_title('Percentage Composition of Nutrients in Various Food Items', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Food Items')
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1))

plt.tight_layout()
plt.show()