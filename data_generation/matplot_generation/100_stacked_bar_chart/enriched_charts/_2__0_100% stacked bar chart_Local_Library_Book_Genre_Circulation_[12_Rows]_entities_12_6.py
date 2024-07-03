import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4']
renewable = np.array([45, 50, 55, 60, 65, 70, 75, 80])
non_renewable = np.array([40, 35, 30, 25, 20, 15, 10, 5])
other_sources = np.array([15, 15, 15, 15, 15, 15, 15, 15])

# Plot
bar_width = 0.5
fig, ax = plt.subplots(figsize=(10, 8))

ax.barh(categories, renewable, color='#1f77b4', edgecolor='white', height=bar_width, label='Renewable Energy')
ax.barh(categories, non_renewable, left=renewable, color='#ff7f0e', edgecolor='white', height=bar_width, label='Non-Renewable Energy')
ax.barh(categories, other_sources, left=renewable+non_renewable, color='#2ca02c', edgecolor='white', height=bar_width, label='Other Sources')

# Title and labels
ax.set_title('Energy Sources Distribution Over Time', fontsize=15)
ax.set_xlabel('Percentage')
ax.set_ylabel('Quarter')

# Legend
ax.legend(loc='upper right')

# Show plot
plt.tight_layout()
plt.show()