
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
pollution_air = [78, 82, 76, 80, 85, 88, 90, 92, 89, 87, 84, 81]
pollution_water = [67, 72, 69, 74, 70, 75, 73, 78, 76, 74, 72, 70]
pollution_soil = [50, 55, 53, 57, 60, 62, 65, 67, 64, 61, 59, 58]

fig, ax = plt.subplots(figsize=(10, 12))

bar_width = 0.35
bar_locations_air = range(len(pollution_air))
bar_locations_water = [x + bar_width for x in bar_locations_air]
bar_locations_soil = [x + bar_width for x in bar_locations_water]

bars1 = ax.bar(bar_locations_air, pollution_air, bar_width, label='Air Pollution', color='#FF6347')
bars2 = ax.bar(bar_locations_water, pollution_water, bar_width, label='Water Pollution', color='#4682B4')
bars3 = ax.bar(bar_locations_soil, pollution_soil, bar_width, label='Soil Pollution', color='#32CD32')

ax.set_xticks([r + bar_width for r in range(len(pollution_air))])
ax.set_xticklabels(months, rotation=45)

plt.ylabel('Pollution Levels')
plt.title('Monthly Pollution Levels in Air, Water, and Soil')
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()