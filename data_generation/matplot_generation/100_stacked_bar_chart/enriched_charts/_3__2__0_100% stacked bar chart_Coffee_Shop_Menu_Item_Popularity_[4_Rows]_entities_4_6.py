
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy']
meals = ['Breakfast', 'Lunch', 'Dinner', 'Snack']
data = np.array([
    [15, 25, 30, 20, 10],  # Breakfast
    [10, 30, 25, 25, 10],  # Lunch
    [20, 25, 20, 25, 10],  # Dinner
    [30, 10, 20, 20, 20]   # Snack
])

# Calculate the cumulative sum for each bar
cumulative_data = np.cumsum(data, axis=1)

# Colors for each category
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF6666']

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

for i in range(len(categories)):
    if i == 0:
        ax.barh(meals, data[:, i], color=colors[i], edgecolor='white', height=0.5)
    else:
        ax.barh(meals, data[:, i], left=cumulative_data[:, i-1], color=colors[i], edgecolor='white', height=0.5)

# Title and labels
ax.set_title('Percentage of Different Food Groups Consumed in Various Meals', fontsize=14, pad=20)
ax.set_xlabel('Percentage', fontsize=12)
ax.set_ylabel('Meals', fontsize=12)

# Legend
ax.legend(categories, loc='upper left', bbox_to_anchor=(1, 1))

# Display the chart
plt.tight_layout()
plt.show()