
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
type_a = [20, 22, 25, 30, 28, 30, 25, 20, 22, 25, 27, 30]
type_b = [25, 20, 23, 25, 27, 30, 30, 25, 28, 25, 23, 20]
type_c = [30, 28, 27, 20, 25, 20, 25, 30, 25, 25, 25, 25]
type_d = [25, 30, 25, 25, 20, 20, 20, 25, 25, 25, 25, 25]

# Stack data
data = np.array([type_a, type_b, type_c, type_d])
data_cum = data.cumsum(axis=0)

# Colors
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9']

# Plot
fig, ax = plt.subplots(figsize=(12, 10))

for i, col in enumerate(colors):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(months, heights, bottom=starts, width=0.5, label=f'Type {chr(65+i)}', color=col)

# Customize
ax.set_ylabel('Percentage')
ax.set_xlabel('Months')
ax.set_title('Monthly Distribution of Food Consumption for 2024', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()