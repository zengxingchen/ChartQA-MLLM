
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
classical_music = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410]
rock_music = [400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620]
jazz_music = [500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720]
pop_music = [600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930]
hiphop_music = [700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810]

fig, ax = plt.subplots(figsize=(16, 10))

y = np.vstack([classical_music, rock_music, jazz_music, pop_music, hiphop_music])
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

ax.stackplot(months, y, labels=['Classical Music', 'Rock Music', 'Jazz Music', 'Pop Music', 'Hip Hop Music'], colors=colors)

ax.annotate('Peak Classical Music', xy=('December', 410), xytext=('November', 450),
            arrowprops=dict(facecolor='red', shrink=0.05))
ax.annotate('Max Hip Hop Music', xy=('December', 810), xytext=('November', 850),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.set_title('Monthly Music Genre Popularity in 2023', pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Popularity (Thousands)')

ax.legend(loc='upper left')

plt.tight_layout()
plt.show()