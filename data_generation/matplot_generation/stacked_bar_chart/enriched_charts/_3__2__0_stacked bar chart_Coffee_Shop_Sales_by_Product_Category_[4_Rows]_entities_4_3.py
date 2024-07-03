
import matplotlib.pyplot as plt

# Data
quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022',
            'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023']
pop_music = [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]
classical_music = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
rock_music = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]

# Colors
colors_pop = '#FF5733'
colors_classical = '#33FF57'
colors_rock = '#3357FF'

# Plotting
fig, ax = plt.subplots(figsize=(14, 10))  # Change the figure size

bar_width = 0.35  # Change the width of the bars

y_positions = range(len(quarters))

ax.bar(y_positions, pop_music, bar_width, label='Pop Music', color=colors_pop)
ax.bar(y_positions, classical_music, bar_width, bottom=pop_music, label='Classical Music', color=colors_classical)
ax.bar(y_positions, rock_music, bar_width, bottom=[i+j for i,j in zip(pop_music, classical_music)], label='Rock Music', color=colors_rock)

for i, (p, c, r) in enumerate(zip(pop_music, classical_music, rock_music)):
    ax.text(i, p / 2, str(p), va='center', ha='center', color='white', fontsize=10)
    ax.text(i, p + c / 2, str(c), va='center', ha='center', color='white', fontsize=10)
    ax.text(i, p + c + r / 2, str(r), va='center', ha='center', color='white', fontsize=10)

ax.set_ylabel('Number of Albums Sold (Thousands)')
ax.set_title('Quarterly Sales of Music Genres Over Three Years', pad=20)
ax.set_xticks(y_positions)
ax.set_xticklabels(quarters)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()