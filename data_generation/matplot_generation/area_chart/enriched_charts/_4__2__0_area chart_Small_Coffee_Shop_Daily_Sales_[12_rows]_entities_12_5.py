
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
books_sold = [50, 65, 70, 80, 85, 90, 120, 130, 125, 140, 150, 160]

month_numbers = np.arange(len(months)) + 1

fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(month_numbers, books_sold, color="#3498db")

ax.set_xticks(month_numbers)
ax.set_xticklabels(months, rotation=45)
ax.set_yticks(range(0, max(books_sold) + 20, 20))
ax.set_yticklabels([f"{sold} Books" for sold in range(0, max(books_sold) + 20, 20)])

ax.set_title('Monthly Book Sales in 2023', fontsize=18, pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Number of Books Sold', fontsize=14)

ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

for i, sold in enumerate(books_sold):
    ax.text(month_numbers[i], sold + 3, f"{sold} Books", ha='center', fontsize=10)

plt.tight_layout()
plt.show()