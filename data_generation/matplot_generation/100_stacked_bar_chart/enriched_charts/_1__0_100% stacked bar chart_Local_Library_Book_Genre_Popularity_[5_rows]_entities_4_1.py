
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
carbohydrates = np.array([50, 45, 55, 60, 50])
proteins = np.array([30, 35, 25, 20, 30])
fats = np.array([20, 20, 20, 20, 20])
vitamins = np.array([10, 15, 15, 10, 10])
minerals = np.array([10, 5, 10, 10, 10])

# Stacked data
data = np.vstack([carbohydrates, proteins, fats, vitamins, minerals])
data_cum = data.cumsum(axis=0)

# Colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']

# Plot
fig, ax = plt.subplots(figsize=(10, 7))

# Horizontal bar
bar_width = 0.8
for i, (colname, color) in enumerate(zip(['Carbohydrates', 'Proteins', 'Fats', 'Vitamins', 'Minerals'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(labels, widths, left=starts, height=bar_width, label=colname, color=color)

# Customize the plot
ax.set_xlabel('Percentage of Daily Intake')
ax.set_title('Daily Nutrient Intake by Day', pad=20)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=5)

plt.tight_layout()
plt.show()