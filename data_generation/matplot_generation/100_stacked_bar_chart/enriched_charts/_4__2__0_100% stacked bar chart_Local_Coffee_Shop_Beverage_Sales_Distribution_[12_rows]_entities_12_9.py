
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Apparel', 'Footwear', 'Accessories', 'Home Decor']
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E', 'Company F', 'Company G', 'Company H', 'Company I', 'Company J']
data = np.array([
    [120, 80, 60, 40],
    [90, 110, 70, 30],
    [60, 100, 80, 60],
    [150, 50, 70, 30],
    [70, 90, 100, 40],
    [130, 60, 90, 50],
    [110, 70, 100, 20],
    [100, 120, 60, 20],
    [90, 70, 120, 20],
    [110, 80, 60, 50]
])

# Calculate percentage data
data_percentage = data / data.sum(axis=1)[:, None] * 100

# Colors
colors = ['#4CAF50', '#FFC107', '#00BCD4', '#E91E63']

# Plotting
fig, ax = plt.subplots(figsize=(12, 10))
width = 0.6  # Width of the bars
x = np.arange(len(companies))

for i in range(len(categories)):
    ax.bar(x, data_percentage[:, i], bottom=np.sum(data_percentage[:, :i], axis=1), color=colors[i], edgecolor='white', width=width)

# Labels and title
ax.set_xticks(x)
ax.set_xticklabels(companies, rotation=45, ha='right')
ax.set_ylabel('Percentage')
ax.set_title('Market Share Distribution in Fashion Industry')

# Legend
ax.legend(categories, loc='upper left', bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()