
import matplotlib.pyplot as plt

data = {
    'Category': ['Astronomy', 'Astrobiology', 'Cosmology', 'Exoplanet Research', 'Stellar Physics', 
                 'Galactic Astronomy', 'Planetary Science', 'Radio Astronomy', 'Space Missions', 
                 'Space Telescopes', 'Astronautics', 'Space Technology', 'Dark Matter Research', 
                 'Gravitational Waves', 'Solar Physics', 'Astrophysics', 'Observational Astronomy', 
                 'Theoretical Astronomy', 'Astrochemistry', 'Astroinformatics'],
    'Discoveries (millions)': [100, 85, 150, 120, 70, 60, 130, 90, 110, 95, 105, 115, 80, 125, 70, 140, 75, 85, 90, 95],
    'Avg. Time Spent (mins)': [60, 45, 90, 50, 80, 55, 65, 40, 75, 70, 85, 60, 50, 95, 40, 85, 45, 50, 65, 55],
    'Funding (billions)': [5, 3, 7, 4, 2.5, 2, 6, 3.5, 8, 4.5, 5.5, 6.5, 4, 7.5, 2.8, 7, 3.2, 4.1, 3.8, 4.6]
}

fig, ax = plt.subplots(figsize=(18, 10))

for i in range(len(data['Category'])):
    ax.scatter(data['Discoveries (millions)'][i], data['Avg. Time Spent (mins)'][i], 
               s=data['Funding (billions)'][i]*20, 
               label='{}'.format(data['Category'][i]),
               alpha=0.6, edgecolors='w',
               linewidth=1.5)

colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#33FFF3', 
          '#FF33A1', '#33A1FF', '#A1FF33', '#FF33F3', '#33FF85', 
          '#FF8533', '#FF3385', '#3385FF', '#FF5733', '#33FF57', 
          '#3357FF', '#FF33A1', '#33A1FF', '#A1FF33', '#FF33F3']

for i, dot in enumerate(ax.collections):
    dot.set_facecolor(colors[i % len(colors)])

ax.set_title('Bubble Chart: Astronomy & Space Exploration Discoveries, Time Spent, and Funding', pad=20, fontsize=16)
ax.set_xlabel('Discoveries (millions)', fontsize=12)
ax.set_ylabel('Avg. Time Spent (mins)', fontsize=12)

ax.grid(True)
ax.legend(title='Fields of Study', loc='upper left')

plt.tight_layout()
plt.show()