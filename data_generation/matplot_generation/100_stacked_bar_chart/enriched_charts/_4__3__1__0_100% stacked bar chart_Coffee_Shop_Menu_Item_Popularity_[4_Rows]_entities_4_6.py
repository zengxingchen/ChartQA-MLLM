
import matplotlib.pyplot as plt
import numpy as np

categories = ['AI Research', 'Quantum Computing', 'Renewable Energy', 'Space Exploration', 'Healthcare Innovations', 'Cybersecurity', 'Nanotechnology', 'Autonomous Vehicles', 'Blockchain', '3D Printing', 'Robotics']
years = ['1990', '2000', '2010', '2020']
data = np.array([
    [10, 20, 35, 50],
    [5, 15, 25, 40],
    [8, 18, 28, 38],
    [7, 12, 22, 32],
    [10, 20, 30, 40],
    [6, 16, 26, 36],
    [4, 14, 24, 34],
    [9, 19, 29, 39],
    [3, 13, 23, 33],
    [8, 18, 28, 38],
    [11, 21, 31, 41]
])

data_percentage = data / data.sum(axis=0) * 100

fig, ax = plt.subplots(figsize=(8, 12))

bar_width = 0.55
bar_positions = np.arange(len(years))

bottoms = np.zeros(len(years))

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#f7b7a3', '#6e5773', '#e0bbe4']

for i, category in enumerate(categories):
    ax.bar(bar_positions, data_percentage[i], bar_width, bottom=bottoms, label=category, color=colors[i])
    bottoms += data_percentage[i]

ax.set_xticks(bar_positions)
ax.set_xticklabels(years)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Evolution of Emerging Technologies Over Decades')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()

plt.show()