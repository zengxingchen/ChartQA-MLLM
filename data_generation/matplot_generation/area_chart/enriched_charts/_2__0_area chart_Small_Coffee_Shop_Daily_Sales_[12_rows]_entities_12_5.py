
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [100, 120, 130, 150, 160, 180, 190, 210, 200, 220, 230, 240]

month_numbers = np.arange(len(months)) + 1

fig, ax = plt.subplots(figsize=(14, 7))

ax.fill_between(month_numbers, revenue, color="#2ecc71")

ax.set_xticks(month_numbers)
ax.set_xticklabels(months, rotation=45)
ax.set_yticks(range(0, max(revenue) + 50, 50))
ax.set_yticklabels([f"${rev}K" for rev in range(0, max(revenue) + 50, 50)])

ax.set_title('Monthly Revenue in 2023', fontsize=18, pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Revenue (in thousands $)', fontsize=14)

ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

for i, rev in enumerate(revenue):
    ax.text(month_numbers[i], rev + 5, f"${rev}K", ha='center', fontsize=10)

plt.tight_layout()
plt.show()