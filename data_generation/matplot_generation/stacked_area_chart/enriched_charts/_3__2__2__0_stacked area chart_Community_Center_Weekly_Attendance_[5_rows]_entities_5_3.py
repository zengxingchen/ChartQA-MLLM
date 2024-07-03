
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
design = [45, 35, 20, 60, 50, 40, 70, 60, 50, 80, 70, 55]
development = [85, 75, 60, 90, 80, 65, 95, 85, 70, 100, 90, 75]
marketing = [100, 90, 75, 110, 95, 80, 115, 100, 85, 120, 110, 90]

fig, ax = plt.subplots(figsize=(16, 10))
ax.stackplot(months, design, development, marketing, colors=['#FF5733', '#33FF57', '#3357FF'])

ax.set_title('Monthly Team Activity Hours in Project Management', fontsize=20, fontweight='bold', pad=25)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Hours', fontsize=14)

for i in range(len(months)):
    total = design[i] + development[i] + marketing[i]
    ax.text(i, total + 5, f"{total}", ha='center', va='bottom')

plt.legend(['Design', 'Development', 'Marketing'], loc='upper left')
plt.tight_layout()
plt.show()