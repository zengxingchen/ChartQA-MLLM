
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    'A': [25, 30, 20, 35, 25, 30, 20, 25, 30, 20],
    'B': [35, 25, 30, 25, 30, 35, 25, 40, 30, 35],
    'C': [40, 45, 50, 40, 45, 35, 55, 35, 40, 45]
}

categories = data['Category']
a_values = data['A']
b_values = data['B']
c_values = data['C']

ind = np.arange(len(categories))  # the x locations for the groups
width = 0.5  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 7))

p1 = ax.barh(ind, a_values, width, color='#1f77b4')
p2 = ax.barh(ind, b_values, width, left=a_values, color='#ff7f0e')
p3 = ax.barh(ind, c_values, width, left=np.array(a_values)+np.array(b_values), color='#2ca02c')

ax.set_xlabel('Percentage')
ax.set_title('Yearly Distribution of Product Categories')
ax.set_yticks(ind)
ax.set_yticklabels(categories)
ax.legend((p1[0], p2[0], p3[0]), ('Category A', 'Category B', 'Category C'))

plt.show()