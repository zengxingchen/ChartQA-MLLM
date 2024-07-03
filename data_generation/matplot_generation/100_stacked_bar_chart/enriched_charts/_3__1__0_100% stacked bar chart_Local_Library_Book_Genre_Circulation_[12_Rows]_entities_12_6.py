import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [40, 50, 10],
    [30, 60, 10],
    [70, 20, 10],
    [20, 70, 10],
    [60, 30, 10],
    [80, 10, 10],
    [25, 60, 15],
    [65, 20, 15],
    [35, 55, 10],
    [50, 40, 10]
])

countries = ['USA', 'China', 'Germany', 'India', 'France', 'Brazil', 'Japan', 'Canada', 'Australia', 'UK']
categories = ['Renewable Energy', 'Non-Renewable Energy', 'Nuclear Energy']
colors = ['#66c2a5', '#fc8d62', '#8da0cb']

bar_width = 0.6
fig, ax = plt.subplots(figsize=(12, 8))

left = np.zeros(len(data))
for i, category in enumerate(categories):
    ax.barh(countries, data[:, i], left=left, label=category, color=colors[i], height=bar_width)
    left += data[:, i]

ax.set_xlabel('Percentage')
ax.set_title('Energy Consumption by Type in Different Countries', pad=20)
ax.legend(loc='upper right')
plt.show()