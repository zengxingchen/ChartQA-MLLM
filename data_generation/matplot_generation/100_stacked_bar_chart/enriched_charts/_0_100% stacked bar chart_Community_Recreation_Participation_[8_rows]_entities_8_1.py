
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Product A': [25, 30, 35, 40],
    'Product B': [35, 40, 25, 20],
    'Product C': [40, 30, 40, 40]
}
df = pd.DataFrame(data)

# Create a figure with specified figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Colors for each product
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot stacked bar chart horizontally
bottoms = np.zeros(len(df['Quarter']))
for i, col in enumerate(df.columns[1:]):
    values = df[col] / 100 * df.sum(axis=1)
    ax.barh(df['Quarter'], values, left=bottoms, label=col, color=colors[i], height=0.4)
    bottoms += values

# Adding labels and title
ax.set_xlabel('Sales Percentage')
ax.set_title('Sales Distribution for Products A, B, and C per Quarter')

# Add legend
ax.legend()

plt.show()