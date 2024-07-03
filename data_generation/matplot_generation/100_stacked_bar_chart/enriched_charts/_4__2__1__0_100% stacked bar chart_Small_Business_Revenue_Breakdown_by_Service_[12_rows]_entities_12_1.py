
import matplotlib.pyplot as plt
import numpy as np

categories = ['Technology', 'Finance', 'Healthcare', 'Education', 'Entertainment', 'Retail', 'Real Estate', 'Transportation', 'Energy', 'Utilities']
Q1 = [15, 20, 30, 25, 10, 18, 22, 17, 25, 21]
Q2 = [25, 30, 20, 35, 20, 22, 28, 19, 30, 25]
Q3 = [35, 25, 30, 20, 40, 25, 30, 26, 22, 27]
Q4 = [25, 25, 20, 20, 30, 35, 20, 38, 23, 27]

barWidth = 0.8

r = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(10, 14))
ax.bar(r, Q1, color='#FF5733', edgecolor='white', width=barWidth)
ax.bar(r, Q2, bottom=Q1, color='#33FF57', edgecolor='white', width=barWidth)
ax.bar(r, Q3, bottom=np.array(Q1)+np.array(Q2), color='#3357FF', edgecolor='white', width=barWidth)
ax.bar(r, Q4, bottom=np.array(Q1)+np.array(Q2)+np.array(Q3), color='#FF33A1', edgecolor='white', width=barWidth)

ax.set_ylabel('Percentage')
ax.set_title('Annual Distribution of Sector Performance')
ax.set_xticks(r)
ax.set_xticklabels(categories, rotation=45, ha="right")
ax.legend(['Q1', 'Q2', 'Q3', 'Q4'], loc='upper left')

plt.tight_layout()
plt.show()