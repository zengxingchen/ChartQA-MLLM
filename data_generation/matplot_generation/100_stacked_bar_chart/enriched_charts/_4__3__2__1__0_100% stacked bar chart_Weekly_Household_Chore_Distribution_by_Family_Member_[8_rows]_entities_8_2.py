
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Apple', 'Banana', 'Carrot', 'Dates', 'Eggplant', 'Fig', 'Grapes', 'Honeydew']
nutrients = ['Nutrient A', 'Nutrient B', 'Nutrient C', 'Nutrient D', 'Nutrient E']
data = np.array([
    [22, 18, 28, 25, 7],
    [24, 21, 17, 28, 10],
    [11, 21, 23, 30, 15],
    [33, 12, 20, 25, 10],
    [16, 24, 20, 24, 16],
    [20, 17, 23, 30, 10],
    [25, 19, 16, 28, 12],
    [18, 22, 20, 30, 10]
])

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF']

# Normalize data to 100%
data_normalized = data / data.sum(axis=1)[:, np.newaxis] * 100

# Plot
fig, ax = plt.subplots(figsize=(7, 10))

# Stack bars vertically
bottom = np.zeros(len(categories))
for i in range(data.shape[1]):
    ax.bar(categories, data_normalized[:, i], bottom=bottom, color=colors[i], label=nutrients[i])
    bottom += data_normalized[:, i]

# Add title and labels
ax.set_title('Percentage Composition of Nutrients in Various Food Items', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Food Items')
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1))

plt.tight_layout()
plt.show()