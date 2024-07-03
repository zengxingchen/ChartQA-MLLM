
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
fruits = [15, 18, 20, 22, 25, 28, 30, 28, 26, 24, 22, 20]
vegetables = [20, 22, 24, 26, 28, 30, 32, 31, 29, 27, 25, 23]
dairy = [18, 20, 22, 24, 26, 28, 30, 29, 27, 25, 23, 21]
meat = [12, 14, 16, 18, 20, 22, 24, 23, 21, 19, 17, 15]
grains = [10, 12, 14, 16, 18, 20, 22, 21, 19, 17, 15, 13]

fig, ax = plt.subplots(figsize=(16, 8))

# Stacking the data
y = np.vstack([fruits, vegetables, dairy, meat, grains])

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFA533']

# Plotting the stacked area chart
ax.stackplot(months, y, labels=['Fruits', 'Vegetables', 'Dairy', 'Meat', 'Grains'], colors=colors)

# Annotating specific points
ax.annotate('Peak fruit consumption', xy=('July', 30), xytext=('June', 35),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('High vegetable consumption', xy=('July', 122), xytext=('August', 130),
            arrowprops=dict(facecolor='blue', shrink=0.05))

# Adding title and labels
ax.set_title('Monthly Food Consumption Breakdown', pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Number of Servings')

# Adding legend
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()