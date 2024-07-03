
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Primary', 'Secondary', 'Tertiary', 'Vocational', 'Adult', 'Postgraduate', 'Professional', 'Doctorate'],
    'Group1': [15, 30, 25, 40, 20, 35, 50, 45],
    'Group2': [20, 25, 35, 30, 25, 40, 35, 30],
    'Group3': [65, 45, 40, 30, 55, 25, 15, 25]
}

categories = data['Category']
group1 = data['Group1']
group2 = data['Group2']
group3 = data['Group3']

bar_width = 0.35

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(categories))

p1 = ax.bar(categories, group1, bar_width, label='Group1', color='#1a5276', bottom=bottom)
bottom += group1

p2 = ax.bar(categories, group2, bar_width, label='Group2', color='#d35400', bottom=bottom)
bottom += group2

p3 = ax.bar(categories, group3, bar_width, label='Group3', color='#27ae60', bottom=bottom)

ax.set_ylabel('Percentage')
ax.set_title('Distribution of Educational Attainment Levels by Group')
ax.legend()

plt.show()