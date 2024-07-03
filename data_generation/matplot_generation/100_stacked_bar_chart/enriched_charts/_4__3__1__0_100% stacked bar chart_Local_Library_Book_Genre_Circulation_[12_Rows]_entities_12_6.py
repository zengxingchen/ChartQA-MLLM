
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [30, 40, 30],
    [20, 50, 30],
    [40, 30, 30],
    [25, 55, 20],
    [35, 35, 30],
    [45, 30, 25],
    [30, 40, 30],
    [50, 20, 30],
    [40, 30, 30],
    [25, 45, 30],
    [35, 30, 35],
    [30, 35, 35],
    [45, 25, 30],
    [20, 50, 30],
    [25, 40, 35]
])

countries = ['USA', 'China', 'Germany', 'India', 'France', 'Brazil', 'Japan', 'Canada', 'Australia', 'UK', 'Italy', 'Russia', 'Mexico', 'South Korea', 'South Africa']
categories = ['Philosophy', 'Ethics', 'Morality']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

bar_width = 0.8
fig, ax = plt.subplots(figsize=(10, 14))

left = np.zeros(len(data))
for i, category in enumerate(categories):
    ax.bar(countries, data[:, i], bottom=left, label=category, color=colors[i], width=bar_width)
    left += data[:, i]

ax.set_ylabel('Percentage')
ax.set_title('Philosophical Perspectives by Country', pad=20)
ax.legend(loc='upper right')
ax.set_xticklabels(countries, rotation=45, ha='right')
plt.show()