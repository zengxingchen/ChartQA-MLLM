
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Primary', 'Secondary', 'Tertiary', 'Vocational', 'Adult'],
    'Group1': [30, 25, 20, 35, 40],
    'Group2': [40, 35, 50, 25, 30],
    'Group3': [30, 40, 30, 40, 30]
}

categories = data['Category']
group1 = data['Group1']
group2 = data['Group2']
group3 = data['Group3']

bar_width = 0.5

fig, ax = plt.subplots(figsize=(10, 6))
bottom = np.zeros(len(categories))

p1 = ax.barh(categories, group1, bar_width, label='Group1', color='#1f77b4', left=bottom)
bottom += group1

p2 = ax.barh(categories, group2, bar_width, label='Group2', color='#ff7f0e', left=bottom)
bottom += group2

p3 = ax.barh(categories, group3, bar_width, label='Group3', color='#2ca02c', left=bottom)

ax.set_xlabel('Percentage')
ax.set_title('Distribution of Educational Attainment Levels')
ax.legend()

plt.show()