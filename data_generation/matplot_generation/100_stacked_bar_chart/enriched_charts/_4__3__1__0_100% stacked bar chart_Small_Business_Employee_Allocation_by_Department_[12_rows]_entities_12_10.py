
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Yoga', 'Running', 'Swimming', 'Cycling', 'Gym'],
    'Q1': [30, 15, 25, 20, 10],
    'Q2': [20, 25, 30, 15, 20],
    'Q3': [25, 30, 20, 30, 25],
    'Q4': [25, 30, 25, 35, 45]
}

categories = data['Category']
q1 = data['Q1']
q2 = data['Q2']
q3 = data['Q3']
q4 = data['Q4']

ind = np.arange(len(categories))
width = 0.6

fig, ax = plt.subplots(figsize=(8, 10))

p1 = ax.bar(ind, q1, width, color='#1f77b4')
p2 = ax.bar(ind, q2, width, bottom=q1, color='#ff7f0e')
p3 = ax.bar(ind, q3, width, bottom=np.add(q1, q2), color='#2ca02c')
p4 = ax.bar(ind, q4, width, bottom=np.add(np.add(q1, q2), q3), color='#d62728')

ax.set_title('Quarterly Participation in Sports Activities', pad=20)
ax.set_xticks(ind)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.legend((p1[0], p2[0], p3[0], p4[0]), ('Q1', 'Q2', 'Q3', 'Q4'), loc='upper left', bbox_to_anchor=(1,1))

plt.show()