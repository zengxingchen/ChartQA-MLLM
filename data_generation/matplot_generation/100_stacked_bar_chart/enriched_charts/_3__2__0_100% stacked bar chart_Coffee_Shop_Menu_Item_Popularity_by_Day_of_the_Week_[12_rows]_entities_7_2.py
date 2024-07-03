import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031"]
value1 = [15, 20, 25, 30, 35, 40, 50, 45, 50, 55, 60]
value2 = [25, 30, 35, 40, 45, 30, 20, 25, 20, 25, 30]
value3 = [60, 50, 40, 30, 20, 30, 30, 30, 30, 20, 10]

# Create stacked bar chart
barWidth = 0.5
fig, ax = plt.subplots(figsize=(10, 6))

# Set position of bar on X axis
r = np.arange(len(categories))

# Make the plot
ax.barh(r, value1, color='#1f77b4', edgecolor='grey', height=barWidth, label='Value 1')
ax.barh(r, value2, left=value1, color='#ff7f0e', edgecolor='grey', height=barWidth, label='Value 2')
ax.barh(r, value3, left=np.add(value1, value2), color='#2ca02c', edgecolor='grey', height=barWidth, label='Value 3')

# Add labels
ax.set_xlabel('Percentage')
ax.set_ylabel('Years')
ax.set_title('Distribution of Values over Years', pad=20)
ax.set_yticks(r)
ax.set_yticklabels(categories)
ax.legend(loc='upper right')

plt.show()