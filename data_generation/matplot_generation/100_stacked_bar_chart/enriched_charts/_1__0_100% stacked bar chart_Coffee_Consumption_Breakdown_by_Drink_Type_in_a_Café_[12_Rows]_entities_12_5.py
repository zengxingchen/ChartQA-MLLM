
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [30, 50, 20],
    [35, 40, 25],
    [25, 55, 20],
    [45, 35, 20],
    [20, 50, 30],
    [40, 30, 30],
    [30, 45, 25],
    [35, 40, 25],
    [25, 55, 20],
    [45, 35, 20],
    [20, 50, 30],
    [40, 30, 30],
    [30, 45, 25],
    [35, 40, 25],
    [25, 55, 20],
    [45, 35, 20],
    [20, 50, 30],
    [40, 30, 30],
    [30, 45, 25],
    [35, 40, 25]
])

categories = ['2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', 
              '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040']

width = 0.5  # Width of the bars
fig, ax = plt.subplots(figsize=(14, 8))  # Adjusted the size of the figure

bars1 = data[:, 0]
bars2 = data[:, 1]
bars3 = data[:, 2]

bar_width = 0.4  # Bar width
x = np.arange(len(categories))

ax.barh(x, bars1, color='#FF9999', edgecolor='grey', height=bar_width, label='Value1')
ax.barh(x, bars2, left=bars1, color='#66B2FF', edgecolor='grey', height=bar_width, label='Value2')
ax.barh(x, bars3, left=bars1+bars2, color='#99FF99', edgecolor='grey', height=bar_width, label='Value3')

ax.set_xlabel('Percentage')
ax.set_title('Distribution of Future Technology Usage (2021-2040)')
ax.set_yticks(x)
ax.set_yticklabels(categories)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()