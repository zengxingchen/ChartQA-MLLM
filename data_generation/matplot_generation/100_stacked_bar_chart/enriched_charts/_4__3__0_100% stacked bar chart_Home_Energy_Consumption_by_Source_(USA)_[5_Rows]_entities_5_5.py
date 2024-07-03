
import matplotlib.pyplot as plt
import numpy as np

categories = ['Virtual Reality', 'Artificial Intelligence', 'Quantum Computing', 'Space Tourism', 
              'Renewable Energy', 'Blockchain', '5G Networks', 'Nanotechnology', 'Biotechnology', 'Drones']
research = [18, 22, 25, 20, 15, 28, 20, 30, 25, 22]
writing = [24, 28, 20, 30, 32, 25, 27, 20, 30, 25]
editing = [32, 30, 35, 25, 28, 22, 33, 25, 20, 28]
publishing = [26, 20, 20, 25, 25, 25, 20, 25, 25, 25]

total = np.array(research) + np.array(writing) + np.array(editing) + np.array(publishing)
research = np.array(research) / total * 100
writing = np.array(writing) / total * 100
editing = np.array(editing) / total * 100
publishing = np.array(publishing) / total * 100

data = np.vstack([research, writing, editing, publishing])
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

fig, ax = plt.subplots(figsize=(10, 14))
bar_width = 0.8

y_pos = np.arange(len(categories))

for i, row in enumerate(data):
    if i == 0:
        ax.bar(y_pos, row, color=colors[i], edgecolor='white', width=bar_width)
    else:
        ax.bar(y_pos, row, bottom=np.sum(data[:i], axis=0), color=colors[i], edgecolor='white', width=bar_width)

ax.set_xticks(y_pos)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.set_ylabel('Percentage')
ax.set_title('Time Allocation in Future Technologies Research & Development')
ax.legend(['Research', 'Writing', 'Editing', 'Publishing'], loc='upper left')

plt.tight_layout()
plt.show()