
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025']
type_a = [25, 30, 20, 35, 28, 33, 25, 30]
type_b = [35, 30, 40, 25, 32, 27, 35, 30]
type_c = [15, 20, 20, 15, 18, 17, 20, 20]
type_d = [25, 20, 20, 25, 22, 23, 20, 20]

# Stack data
data = np.array([type_a, type_b, type_c, type_d])
data_cum = data.cumsum(axis=0)

# Reversed order to enable horizontal stacking
categories = categories[::-1]
data = data[:, ::-1]
data_cum = data_cum[:, ::-1]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33']

# Plot
fig, ax = plt.subplots(figsize=(10, 8))

for i, col in enumerate(colors):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=0.5, label=f'Type {chr(65+i)}', color=col)

# Customize
ax.set_xlabel('Percentage')
ax.set_ylabel('Quarters')
ax.set_title('Quarterly Distribution of Sales Types for 2024-2025', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()