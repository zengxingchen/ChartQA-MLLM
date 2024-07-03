
import matplotlib.pyplot as plt
import numpy as np

categories = ['Strength', 'Cardio', 'Flexibility', 'Balance', 'Endurance', 'Coordination', 'Power', 'Speed', 'Agility']
values = np.array([
    [25, 30, 20, 25],
    [30, 25, 30, 15],
    [20, 20, 25, 35],
    [25, 25, 25, 25],
    [20, 30, 35, 15],
    [30, 20, 15, 35],
    [35, 25, 25, 15],
    [15, 35, 25, 25],
    [25, 25, 20, 30]
])

values_percentage = values / values.sum(axis=1)[:, None] * 100

fig, ax = plt.subplots(figsize=(14, 8))

width = 0.6  # bar width
indices = np.arange(len(categories))

bottoms = np.zeros(len(categories))
for i in range(values_percentage.shape[1]):
    ax.barh(indices, values_percentage[:, i], left=bottoms, height=width, label=f'Value {i+1}',
            color=['#FF6347', '#4682B4', '#8A2BE2', '#3CB371'][i])
    bottoms += values_percentage[:, i]

ax.set_yticks(indices)
ax.set_yticklabels(categories)
ax.set_xlabel('Percentage')
ax.set_title('Distribution of Fitness Components by Percentage')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)

plt.tight_layout()
plt.show()