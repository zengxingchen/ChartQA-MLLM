
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', 
              '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4', '2023-Q1', '2023-Q2', '2023-Q3', '2023-Q4']
renewable = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 82, 87, 88, 90, 92, 94, 96])
non_renewable = np.array([40, 35, 30, 25, 20, 15, 10, 5, 8, 9, 6, 5, 4, 3, 2, 2])
other_sources = np.array([15, 15, 15, 15, 15, 15, 15, 15, 7, 9, 7, 7, 6, 5, 4, 2])

# Plot
bar_width = 0.7
fig, ax = plt.subplots(figsize=(12, 10))

ax.bar(categories, renewable, color='#3498db', edgecolor='white', width=bar_width, label='Renewable Energy')
ax.bar(categories, non_renewable, bottom=renewable, color='#e74c3c', edgecolor='white', width=bar_width, label='Non-Renewable Energy')
ax.bar(categories, other_sources, bottom=renewable+non_renewable, color='#2ecc71', edgecolor='white', width=bar_width, label='Other Sources')

# Title and labels
ax.set_title('Energy Sources Distribution Over Time', fontsize=18, pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Quarter')

# Legend
ax.legend(loc='upper left')

# Show plot
plt.tight_layout()
plt.show()