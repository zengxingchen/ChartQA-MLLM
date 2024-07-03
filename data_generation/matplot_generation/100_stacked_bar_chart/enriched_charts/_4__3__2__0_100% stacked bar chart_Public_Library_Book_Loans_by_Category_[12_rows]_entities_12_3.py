
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2018', '2019', '2020', '2021', '2022']
movies = np.array([20, 25, 30, 20, 25])
music = np.array([25, 20, 15, 20, 15])
gaming = np.array([30, 25, 20, 25, 20])
travel = np.array([15, 20, 25, 25, 30])
reading = np.array([10, 10, 10, 10, 10])

# Calculate percentages
totals = movies + music + gaming + travel + reading
movies_percentage = movies / totals * 100
music_percentage = music / totals * 100
gaming_percentage = gaming / totals * 100
travel_percentage = travel / totals * 100
reading_percentage = reading / totals * 100

# Plot
fig, ax = plt.subplots(figsize=(12, 9))
bar_width = 0.5
categories_pos = np.arange(len(categories))

p1 = ax.bar(categories_pos, movies_percentage, color='#FF6347', edgecolor='white', width=bar_width, label='Movies')
p2 = ax.bar(categories_pos, music_percentage, bottom=movies_percentage, color='#4682B4', edgecolor='white', width=bar_width, label='Music')
p3 = ax.bar(categories_pos, gaming_percentage, bottom=movies_percentage + music_percentage, color='#32CD32', edgecolor='white', width=bar_width, label='Gaming')
p4 = ax.bar(categories_pos, travel_percentage, bottom=movies_percentage + music_percentage + gaming_percentage, color='#FFD700', edgecolor='white', width=bar_width, label='Travel')
p5 = ax.bar(categories_pos, reading_percentage, bottom=movies_percentage + music_percentage + gaming_percentage + travel_percentage, color='#8A2BE2', edgecolor='white', width=bar_width, label='Reading')

# Add labels, title, legend, and adjust layout
ax.set_ylabel('Percentage')
ax.set_title('Entertainment & Leisure Activities (2018-2022)', pad=20)
ax.set_xticks(categories_pos)
ax.set_xticklabels(categories)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()