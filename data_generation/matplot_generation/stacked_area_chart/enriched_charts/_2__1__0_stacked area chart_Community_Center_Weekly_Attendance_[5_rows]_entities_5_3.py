
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
star_discoveries = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
planet_discoveries = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
galaxy_discoveries = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

fig, ax = plt.subplots(figsize=(14, 10))
ax.stackplot(months, star_discoveries, planet_discoveries, galaxy_discoveries, colors=['#FF5733', '#33FF57', '#3357FF'])

ax.set_title('Monthly Astronomy Discoveries in 2023', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Number of Discoveries', fontsize=14)

for i in range(len(months)):
    total_discoveries = star_discoveries[i] + planet_discoveries[i] + galaxy_discoveries[i]
    ax.text(i, total_discoveries, f"{total_discoveries:,}", ha='center', va='bottom')

plt.tight_layout()
plt.show()