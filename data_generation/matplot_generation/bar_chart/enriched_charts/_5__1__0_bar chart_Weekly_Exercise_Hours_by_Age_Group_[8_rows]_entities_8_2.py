
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
historical_fiction = [145, 150, 148, 152, 155, 160, 162, 165, 160, 158, 155, 150]
science_fiction = [160, 165, 163, 168, 170, 175, 178, 180, 175, 172, 170, 165]
fantasy = [155, 158, 157, 160, 162, 165, 167, 170, 165, 163, 160, 158]

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.25
bar_locations_historical = range(len(historical_fiction))
bar_locations_science = [x + bar_width for x in bar_locations_historical]
bar_locations_fantasy = [x + bar_width for x in bar_locations_science]

bars1 = ax.barh(bar_locations_historical, historical_fiction, bar_width, label='Historical Fiction', color='#FF5733')
bars2 = ax.barh(bar_locations_science, science_fiction, bar_width, label='Science Fiction', color='#33FF57')
bars3 = ax.barh(bar_locations_fantasy, fantasy, bar_width, label='Fantasy', color='#3357FF')

ax.set_yticks([r + bar_width for r in range(len(historical_fiction))])
ax.set_yticklabels(months)

ax.set_xlim(140, 185)
plt.xlabel('Book Sales (in thousands)')
plt.title('Monthly Book Sales by Genre')
ax.legend(loc='lower right')

plt.tight_layout()
plt.show()