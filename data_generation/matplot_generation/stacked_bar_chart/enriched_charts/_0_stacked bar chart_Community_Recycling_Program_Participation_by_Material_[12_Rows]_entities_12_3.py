
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
apples = [5, 8, 2, 10, 11, 3, 1, 4, 12, 6, 9, 2]
oranges = [7, 6, 9, 3, 4, 4, 5, 8, 10, 4, 11, 7]
berries = [3, 2, 3, 1, 7, 6, 2, 1, 8, 5, 3, 4]
grapes = [1, 4, 5, 4, 8, 7, 9, 3, 2, 3, 6, 8]

# Stacked bar chart data accumulation
bars_oranges = np.add(apples, berries).tolist()

# Modify the color scheme using hexadecimal color codes
colors = ['#FF9999', '#FFCC99', '#66B2FF', '#99FF99']

fig, ax = plt.subplots(figsize=(10, 8)) # Change size of the chart

# Creating the horizontal bar chart
ax.barh(months, apples, color=colors[0], edgecolor='white', height=0.8, label='Apples')
ax.barh(months, oranges, left=apples, color=colors[1], edgecolor='white', height=0.8, label='Oranges')
ax.barh(months, berries, left=bars_oranges, color=colors[2], edgecolor='white', height=0.8, label='Berries')
ax.barh(months, grapes, left=np.add(bars_oranges, oranges).tolist(), color=colors[3], edgecolor='white', height=0.8, label='Grapes')

# Customizing the horizontal stacked bar chart with the new topic: 'Fruit Consumption per Month'
plt.title('Fruit Consumption per Month')
plt.xlabel('Quantity')
plt.ylabel('Month')
plt.xticks(np.arange(0, 51, 5))
plt.yticks(months)
plt.legend(loc='upper right')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the final plot
plt.show()