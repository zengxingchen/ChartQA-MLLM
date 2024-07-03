import matplotlib.pyplot as plt
import numpy as np

categories = ['Technology', 'Finance', 'Healthcare', 'Education', 'Entertainment']
Q1 = [15, 20, 30, 25, 10]
Q2 = [25, 30, 20, 35, 20]
Q3 = [35, 25, 30, 20, 40]
Q4 = [25, 25, 20, 20, 30]

barWidth = 0.6

r = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(r, Q1, color='#4A90E2', edgecolor='white', height=barWidth)
ax.barh(r, Q2, left=Q1, color='#50E3C2', edgecolor='white', height=barWidth)
ax.barh(r, Q3, left=np.array(Q1)+np.array(Q2), color='#9013FE', edgecolor='white', height=barWidth)
ax.barh(r, Q4, left=np.array(Q1)+np.array(Q2)+np.array(Q3), color='#F5A623', edgecolor='white', height=barWidth)

ax.set_xlabel('Percentage')
ax.set_title('Quarterly Distribution of Sector Performance')
ax.set_yticks(r)
ax.set_yticklabels(categories)
ax.legend(['Q1', 'Q2', 'Q3', 'Q4'], loc='lower right')

plt.tight_layout()
plt.show()