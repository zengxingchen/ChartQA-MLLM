
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [25, 40, 35],
    [30, 45, 25],
    [35, 30, 35],
    [40, 35, 25],
    [20, 50, 30],
    [35, 30, 35],
    [30, 35, 35],
    [40, 30, 30],
    [25, 40, 35],
    [30, 45, 25],
    [35, 30, 35],
    [40, 35, 25],
    [20, 50, 30],
    [35, 30, 35],
    [30, 35, 35],
    [40, 30, 30],
    [25, 40, 35],
    [30, 45, 25],
    [35, 30, 35],
    [40, 35, 25]
])

categories = ['2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', 
              '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040']

fig, ax = plt.subplots(figsize=(12, 10))

bars1 = data[:, 0]
bars2 = data[:, 1]
bars3 = data[:, 2]

bar_width = 0.6
x = np.arange(len(categories))

ax.bar(x, bars1, color='#FF5733', edgecolor='grey', width=bar_width, label='Value1')
ax.bar(x, bars2, bottom=bars1, color='#33FFBD', edgecolor='grey', width=bar_width, label='Value2')
ax.bar(x, bars3, bottom=bars1+bars2, color='#3375FF', edgecolor='grey', width=bar_width, label='Value3')

ax.set_ylabel('Percentage')
ax.set_title('Projected Climate Impact by Year (2021-2040)')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()