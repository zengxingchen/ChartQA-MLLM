
import matplotlib.pyplot as plt
import numpy as np

dates = ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', 
         '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12']
page_views = [100, 120, 130, 150, 160, 180, 190, 210, 200, 220, 230, 240]

date_numbers = np.arange(len(dates)) + 1

fig, ax = plt.subplots(figsize=(16, 8))

ax.fill_between(date_numbers, page_views, color="#3498db")

ax.set_xticks(date_numbers)
ax.set_xticklabels(dates, rotation=45)
ax.set_yticks(range(0, max(page_views) + 50, 50))
ax.set_yticklabels([f"{views}K" for views in range(0, max(page_views) + 50, 50)])

ax.set_title('Daily Page Views in January 2023', fontsize=20, pad=20)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Page Views (in thousands)', fontsize=14)

ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

for i, views in enumerate(page_views):
    ax.text(date_numbers[i], views + 5, f"{views}K", ha='center', fontsize=10)

plt.tight_layout()
plt.show()