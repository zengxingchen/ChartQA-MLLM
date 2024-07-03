
import matplotlib.pyplot as plt
import numpy as np

categories = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10']
expenditure_a = [25, 30, 20, 22, 28, 24, 26, 23, 27, 25]
expenditure_b = [35, 25, 30, 33, 27, 26, 28, 30, 29, 32]
expenditure_c = [40, 45, 50, 45, 45, 50, 46, 47, 44, 43]

barWidth = 0.85

r = np.arange(len(categories))

bars1 = np.array(expenditure_a)
bars2 = np.array(expenditure_b)
bars3 = np.array(expenditure_c)

bars = np.add(bars1, bars2).tolist()

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(r, bars1, color='#FF5733', edgecolor='white', height=barWidth)
ax.barh(r, bars2, left=bars1, color='#33FF57', edgecolor='white', height=barWidth)
ax.barh(r, bars3, left=bars, color='#3357FF', edgecolor='white', height=barWidth)

ax.set_xlabel('Percentage')
ax.set_ylabel('Quarters')
ax.set_yticks(r)
ax.set_yticklabels(categories)
ax.legend(['Expenditure A', 'Expenditure B', 'Expenditure C'], loc='upper right')
ax.set_title('Quarterly Expenditure Distribution in Business Sectors')

plt.tight_layout()
plt.show()