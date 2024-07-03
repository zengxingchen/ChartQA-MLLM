
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
population = [1500, 1600, 1700, 1800, 2000, 2200, 2500, 2400, 2300, 2100, 1900, 1700]

month_numbers = np.arange(len(months)) + 1

fig, ax = plt.subplots(figsize=(14, 7))

ax.fill_between(month_numbers, population, color="#FF5733")

ax.set_xticks(month_numbers)
ax.set_xticklabels(months, rotation=45)
ax.set_yticks(range(0, max(population) + 500, 500))
ax.set_yticklabels([f"{pop} people" for pop in range(0, max(population) + 500, 500)])

ax.set_title('Monthly Population Growth in 2024', fontsize=18, y=1.05)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Population', fontsize=14)

for i, pop in enumerate(population):
    ax.text(i + 1, pop + 50, str(pop), ha='center')

ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()