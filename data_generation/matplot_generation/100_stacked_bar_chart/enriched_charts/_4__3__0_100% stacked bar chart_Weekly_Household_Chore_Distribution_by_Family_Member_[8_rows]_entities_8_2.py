import matplotlib.pyplot as plt
import numpy as np

categories = ['Ancient Egypt', 'Ancient Greece', 'Roman Empire', 'Medieval Europe', 'Renaissance', 
              'Industrial Revolution', 'World War I', 'World War II', 'Cold War', 'Modern Era']
expenditure_a = [30, 25, 28, 22, 30, 24, 26, 27, 29, 25]
expenditure_b = [35, 30, 32, 28, 27, 29, 33, 31, 34, 28]
expenditure_c = [35, 45, 40, 50, 43, 47, 41, 42, 37, 47]

barWidth = 0.6

r = np.arange(len(categories))

bars1 = np.array(expenditure_a)
bars2 = np.array(expenditure_b)
bars3 = np.array(expenditure_c)

bars = np.add(bars1, bars2).tolist()

fig, ax = plt.subplots(figsize=(10, 14))

ax.bar(r, bars1, color='#8B0000', edgecolor='white', width=barWidth)
ax.bar(r, bars2, bottom=bars1, color='#FFD700', edgecolor='white', width=barWidth)
ax.bar(r, bars3, bottom=bars, color='#1E90FF', edgecolor='white', width=barWidth)

ax.set_ylabel('Percentage')
ax.set_xlabel('Historical Periods')
ax.set_xticks(r)
ax.set_xticklabels(categories, rotation=45, ha="right")
ax.legend(['Expenditure A', 'Expenditure B', 'Expenditure C'], loc='upper left')
ax.set_title('Distribution of Historical Studies Focus', pad=20)

plt.tight_layout()
plt.show()