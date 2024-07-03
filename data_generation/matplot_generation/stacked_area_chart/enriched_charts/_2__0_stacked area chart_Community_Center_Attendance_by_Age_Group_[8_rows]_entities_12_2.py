
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
vegetables = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
fruits = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
dairy = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
meat = [180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290]
grains = [75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130]

fig, ax = plt.subplots(figsize=(14, 8))

# Stacking the data
y = np.vstack([vegetables, fruits, dairy, meat, grains])

# Colors
colors = ['#4CAF50', '#FFC107', '#2196F3', '#FF5722', '#9C27B0']

# Plotting the stacked area chart
ax.stackplot(months, y, labels=['Vegetables', 'Fruits', 'Dairy', 'Meat', 'Grains'], colors=colors)

# Annotating specific points
ax.annotate('Peak Meat Consumption', xy=('December', 290 + sum(y[:-1, -1])), xytext=('November', 300 + sum(y[:-1, -2])),
            arrowprops=dict(facecolor='red', shrink=0.05))
ax.annotate('Highest Vegetables', xy=('December', 310), xytext=('November', 320),
            arrowprops=dict(facecolor='green', shrink=0.05))

# Adding title and labels
ax.set_title('Monthly Food Consumption Breakdown')
ax.set_xlabel('Month')
ax.set_ylabel('Consumption (kg)')

# Adding legend
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()