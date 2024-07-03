
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
solar = [25, 30, 40, 50, 60, 70, 75, 70, 65, 55, 45, 35]
wind = [30, 35, 45, 55, 65, 75, 80, 75, 70, 60, 50, 40]
hydro = [15, 20, 25, 30, 35, 40, 45, 40, 35, 30, 25, 20]

fig, ax = plt.subplots(figsize=(14, 10))
ax.stackplot(months, solar, wind, hydro, colors=['#FFA07A', '#20B2AA', '#778899'])

ax.set_title('Monthly Renewable Energy Production (in GWh)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Energy Production (GWh)', fontsize=14)

for i in range(len(months)):
    total = solar[i] + wind[i] + hydro[i]
    ax.text(i, total + 2, f"{total}", ha='center', va='bottom')

ax.legend(['Solar', 'Wind', 'Hydro'], loc='upper left')

plt.tight_layout()
plt.show()