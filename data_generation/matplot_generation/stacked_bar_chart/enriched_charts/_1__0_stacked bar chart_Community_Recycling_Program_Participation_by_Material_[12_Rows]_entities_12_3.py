
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

fig, ax = plt.subplots(figsize=(12, 6)) # Change size of the chart

# Creating the horizontal bar chart
ax.bar(months, apples, color=colors[0], edgecolor='white', width=0.8, label='Apples')
ax.bar(months, oranges, bottom=apples, color=colors[1], edgecolor='white', width=0.8, label='Oranges')
ax.bar(months, berries, bottom=bars_oranges, color=colors[2], edgecolor='white', width=0.8, label='Berries')
ax.bar(months, grapes, bottom=np.add(bars_oranges, oranges).tolist(), color=colors[3], edgecolor='white', width=0.8, label='Grapes')

# Customizing the vertical stacked bar chart with the new topic: 'Monthly Fruit Sales'
plt.title('Monthly Fruit Sales')
plt.xlabel('Month')
plt.ylabel('Quantity Sold')
plt.yticks(np.arange(0, 51, 5))
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the final plot
plt.show()