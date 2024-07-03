import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Primary Education', 'Secondary Education', 'Higher Education', 'Vocational Training', 'Online Courses'],
    'Q1': [25, 35, 20, 15, 5],
    'Q2': [30, 30, 25, 10, 5],
    'Q3': [20, 25, 30, 15, 10],
    'Q4': [25, 10, 25, 20, 20]
}

categories = data['Category']
q1 = data['Q1']
q2 = data['Q2']
q3 = data['Q3']
q4 = data['Q4']

ind = np.arange(len(categories))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 6))

p1 = ax.barh(ind, q1, width, color='#FF9999')
p2 = ax.barh(ind, q2, width, left=q1, color='#66B2FF')
p3 = ax.barh(ind, q3, width, left=np.add(q1, q2), color='#99FF99')
p4 = ax.barh(ind, q4, width, left=np.add(np.add(q1, q2), q3), color='#FFCC99')

ax.set_title('Quarterly Distribution of Education Types', pad=20)
ax.set_yticks(ind)
ax.set_yticklabels(categories)
ax.legend((p1[0], p2[0], p3[0], p4[0]), ('Q1', 'Q2', 'Q3', 'Q4'))

plt.show()