
import matplotlib.pyplot as plt
import numpy as np

categories = ['Soccer', 'Basketball', 'Tennis', 'Running', 'Swimming', 'Cycling']
values = np.array([[20, 25, 30, 25],
                   [25, 30, 20, 25],
                   [15, 20, 35, 30],
                   [30, 20, 25, 25],
                   [10, 25, 20, 45],
                   [20, 15, 30, 35]])

values_percentage = values / values.sum(axis=1)[:, None] * 100

bar_width = 0.5
fig, ax = plt.subplots(figsize=(10, 7))

bottoms = np.zeros(len(categories))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

for i in range(values.shape[1]):
    ax.barh(categories, values_percentage[:, i], left=bottoms, height=bar_width, color=colors[i])
    bottoms += values_percentage[:, i]

ax.set_xlabel('Percentage')
ax.set_title('Percentage Distribution of Sports Activities')
ax.legend(['Value1', 'Value2', 'Value3', 'Value4'], loc='upper right')

plt.show()