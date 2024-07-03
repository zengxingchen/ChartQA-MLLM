
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Category': ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G', 'Group H', 'Group I', 'Group J'],
    'Science': [30, 20, 25, 25, 30, 20, 25, 30, 25, 20],
    'Math': [25, 35, 20, 20, 25, 30, 25, 20, 25, 30],
    'History': [20, 25, 30, 25, 20, 30, 25, 25, 25, 25],
    'Art': [25, 20, 25, 30, 25, 20, 25, 25, 25, 25]
}

categories = data['Category']
science = data['Science']
math = data['Math']
history = data['History']
art = data['Art']

ind = np.arange(len(categories))
width = 0.5

fig, ax = plt.subplots(figsize=(10, 7))

p1 = ax.barh(ind, science, width, color='#1f77b4')
p2 = ax.barh(ind, math, width, left=science, color='#ff7f0e')
p3 = ax.barh(ind, history, width, left=np.array(science) + np.array(math), color='#2ca02c')
p4 = ax.barh(ind, art, width, left=np.array(science) + np.array(math) + np.array(history), color='#d62728')

ax.set_xlabel('Percentage')
ax.set_title('Distribution of Subjects Among Different Groups')
ax.set_yticks(ind)
ax.set_yticklabels(categories)
ax.legend((p1[0], p2[0], p3[0], p4[0]), ('Science', 'Math', 'History', 'Art'), loc='upper right')

plt.show()