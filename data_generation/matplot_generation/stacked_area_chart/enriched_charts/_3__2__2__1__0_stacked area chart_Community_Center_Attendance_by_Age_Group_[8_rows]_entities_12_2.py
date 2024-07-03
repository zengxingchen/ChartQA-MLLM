
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
books = [500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720]
movies = [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350]
music = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520]
gaming = [450, 470, 490, 510, 530, 550, 570, 590, 610, 630, 650, 670]
art = [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420]

fig, ax = plt.subplots(figsize=(16, 10))

y = np.vstack([books, movies, music, gaming, art])
colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']

ax.stackplot(months, y, labels=['Books', 'Movies', 'Music', 'Gaming', 'Art'], colors=colors)

ax.annotate('Peak Movie Sales', xy=('December', 1350), xytext=('November', 1400),
            arrowprops=dict(facecolor='purple', shrink=0.05))
ax.annotate('Rising Music Sales', xy=('December', 520 + sum(y[:-1, -1])), xytext=('November', 540 + sum(y[:-1, -2])),
            arrowprops=dict(facecolor='green', shrink=0.05))

ax.set_title('Monthly Sales in Entertainment & Leisure in 2023', pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Sales (Thousand USD)')

ax.legend(loc='upper left')

plt.tight_layout()
plt.show()