
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
apples = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
bananas = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
cherries = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155]
dates = [175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285]

fig, ax = plt.subplots(figsize=(10, 12))

bar_width = 0.2
bar_locations_apples = range(len(apples))
bar_locations_bananas = [x + bar_width for x in bar_locations_apples]
bar_locations_cherries = [x + bar_width for x in bar_locations_bananas]
bar_locations_dates = [x + bar_width for x in bar_locations_cherries]

bars1 = ax.bar(bar_locations_apples, apples, bar_width, label='Apples', color='#3498db')
bars2 = ax.bar(bar_locations_bananas, bananas, bar_width, label='Bananas', color='#e74c3c')
bars3 = ax.bar(bar_locations_cherries, cherries, bar_width, label='Cherries', color='#2ecc71')
bars4 = ax.bar(bar_locations_dates, dates, bar_width, label='Dates', color='#f39c12')

ax.set_xticks([r + bar_width for r in range(len(apples))])
ax.set_xticklabels(months, rotation=45, ha='right')

plt.ylabel('Sales Volume')
plt.title('Monthly Food Sales')
ax.legend(loc='upper left')

ax.set_ylim(50, 350)

plt.tight_layout()
plt.show()