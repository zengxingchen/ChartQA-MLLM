
import matplotlib.pyplot as plt

salaries = [
    45000, 47000, 48000, 50000, 51000, 52000, 53000, 54000, 55000, 56000, 57000, 58000, 59000, 60000, 
    61000, 62000, 63000, 64000, 65000, 66000, 67000, 68000, 69000, 70000, 71000, 72000, 73000, 74000, 
    75000, 76000, 77000, 78000, 79000, 80000, 81000, 82000, 83000, 84000, 85000, 86000, 87000, 88000, 
    89000, 90000, 91000, 92000, 93000, 94000, 95000, 96000, 97000, 98000, 99000, 100000
]

fig, ax = plt.subplots(figsize=(12, 8))
n, bins, patches = ax.hist(salaries, bins=10, orientation='vertical', color='#336699', edgecolor='#000000', linewidth=1.2)

ax.set_title('Salary Distribution of Employees', pad=20)
ax.set_xlabel('Salary ($)', labelpad=15)
ax.set_ylabel('Number of Employees', labelpad=15)
ax.set_ylim(0, 12)

for i, patch in enumerate(patches):
    patch.set_facecolor(plt.cm.plasma(i / len(patches)))

plt.tight_layout()
plt.show()