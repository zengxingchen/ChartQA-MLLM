
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
basketball = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]
soccer = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115]
tennis = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
swimming = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.2
bar_locations_basketball = range(len(basketball))
bar_locations_soccer = [x + bar_height for x in bar_locations_basketball]
bar_locations_tennis = [x + bar_height for x in bar_locations_soccer]
bar_locations_swimming = [x + bar_height for x in bar_locations_tennis]

bars1 = ax.barh(bar_locations_basketball, basketball, bar_height, label='Basketball', color='#1f77b4')
bars2 = ax.barh(bar_locations_soccer, soccer, bar_height, label='Soccer', color='#ff7f0e')
bars3 = ax.barh(bar_locations_tennis, tennis, bar_height, label='Tennis', color='#2ca02c')
bars4 = ax.barh(bar_locations_swimming, swimming, bar_height, label='Swimming', color='#d62728')

ax.set_yticks([r + bar_height for r in range(len(basketball))])
ax.set_yticklabels(months)

plt.xlabel('Participation Levels')
plt.title('Monthly Sports Participation')
ax.legend(loc='lower right')

plt.tight_layout()
plt.show()