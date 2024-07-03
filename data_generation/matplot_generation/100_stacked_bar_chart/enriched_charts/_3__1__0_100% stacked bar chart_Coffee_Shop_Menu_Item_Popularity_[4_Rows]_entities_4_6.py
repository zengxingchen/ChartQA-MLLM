import matplotlib.pyplot as plt
import numpy as np

categories = ['AI Research', 'Quantum Computing', 'Renewable Energy', 'Space Exploration', 'Healthcare Innovations', 'Cybersecurity', 'Nanotechnology', 'Autonomous Vehicles', 'Blockchain', '3D Printing', 'Robotics']
years = ['1990', '2000', '2010', '2020']
data = np.array([
    [15, 25, 35, 45],
    [5, 10, 20, 30],
    [10, 20, 25, 35],
    [8, 12, 18, 22],
    [12, 18, 22, 28],
    [6, 12, 18, 24],
    [4, 6, 10, 16],
    [7, 15, 22, 30],
    [3, 8, 15, 22],
    [10, 14, 20, 25],
    [15, 22, 30, 38]
])

data_percentage = data / data.sum(axis=0) * 100

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.75
bar_positions = np.arange(len(years))

bottoms = np.zeros(len(years))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#9edae5']

for i, category in enumerate(categories):
    ax.bar(bar_positions, data_percentage[i], bar_width, bottom=bottoms, label=category, color=colors[i])
    bottoms += data_percentage[i]

ax.set_xticks(bar_positions)
ax.set_xticklabels(years)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Trends in Future Technologies Over Decades')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()

plt.show()