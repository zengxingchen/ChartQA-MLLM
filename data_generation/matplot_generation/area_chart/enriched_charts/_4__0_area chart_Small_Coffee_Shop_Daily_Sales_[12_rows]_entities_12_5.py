
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
visitors = [120, 150, 200, 300, 400, 450, 480, 460, 350, 300, 200, 150]

month_numbers = np.arange(len(months)) + 1

fig, ax = plt.subplots(figsize=(14, 7))

ax.fill_between(month_numbers, visitors, color="#ff5733")

ax.set_xticks(month_numbers)
ax.set_xticklabels(months, rotation=45)
ax.set_yticks(range(0, max(visitors) + 100, 100))
ax.set_yticklabels([f"{num} Visitors" for num in range(0, max(visitors) + 100, 100)])

ax.set_title('Monthly Visitors to the Museum', fontsize=18)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Number of Visitors', fontsize=12)

for i, txt in enumerate(visitors):
    ax.annotate(txt, (month_numbers[i], visitors[i]), textcoords="offset points", xytext=(0,5), ha='center')

ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()