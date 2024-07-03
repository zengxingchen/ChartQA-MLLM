import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Grains', 'Vegetables', 'Fruits', 'Proteins', 'Dairy', 'Fats']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
data = np.array([
    [40, 25, 15, 10, 5, 5],
    [35, 30, 10, 15, 5, 5],
    [30, 20, 20, 15, 10, 5],
    [45, 15, 10, 15, 10, 5],
    [40, 20, 15, 10, 10, 5]
])

# Colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFB2FF', '#FFDB66']

# Create percentage data
data_percent = data / data.sum(axis=1)[:, None] * 100

# Plot
fig, ax = plt.subplots(figsize=(10, 7))

bar_width = 0.6
bars = np.arange(len(days))

cumulative = np.zeros(len(days))

for i, (category, color) in enumerate(zip(categories, colors)):
    ax.barh(bars, data_percent[:, i], left=cumulative, color=color, label=category, height=bar_width)
    cumulative += data_percent[:, i]

ax.set_yticks(bars)
ax.set_yticklabels(days)
ax.set_xlabel('Percentage')
ax.set_title('Proportion of Different Food Groups in a Sample Diet Over a Week')
ax.legend(loc='lower right')

plt.show()