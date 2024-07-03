
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Research & Development', 'Marketing', 'Sales', 'Customer Service', 'IT & Support', 'Human Resources']
years = ['1990', '2000', '2010', '2020']
data = np.array([
    [20, 25, 30, 35],
    [15, 20, 25, 30],
    [25, 30, 35, 40],
    [10, 15, 20, 25],
    [30, 10, 15, 10],
    [10, 10, 5, 5]
])

# Colors
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF4500']

# Bar Width
bar_width = 0.6

# Plot
fig, ax = plt.subplots(figsize=(10, 12))
bottom = np.zeros(len(years))

for i in range(len(categories)):
    ax.bar(years, data[i], bar_width, label=categories[i], color=colors[i], bottom=bottom)
    bottom += data[i]

# Customize chart
ax.set_title('Distribution of Company Resources Over Decades', fontsize=16)
ax.set_xlabel('Years', fontsize=12)
ax.set_ylabel('Percentage', fontsize=12)
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1))

# Display the plot
plt.show()