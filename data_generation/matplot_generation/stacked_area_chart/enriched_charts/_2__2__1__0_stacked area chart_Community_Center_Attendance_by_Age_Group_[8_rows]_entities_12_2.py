
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
tech = [1000, 1020, 1050, 1080, 1100, 1120, 1150, 1180, 1200, 1230, 1250, 1280]
education = [700, 710, 730, 750, 770, 790, 810, 830, 850, 870, 890, 910]
health = [600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820]
food = [500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610]
tourism = [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510]

fig, ax = plt.subplots(figsize=(18, 12))

y = np.vstack([tech, education, health, food, tourism])
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

ax.stackplot(months, y, labels=['Tech', 'Education', 'Health', 'Food', 'Tourism'], colors=colors)

ax.annotate('Peak Tech Sales', xy=('December', 1280), xytext=('November', 1300),
            arrowprops=dict(facecolor='blue', shrink=0.05))
ax.annotate('Highest Tourism Sales', xy=('December', 510 + sum(y[:-1, -1])), xytext=('November', 510 + sum(y[:-1, -2])),
            arrowprops=dict(facecolor='purple', shrink=0.05))

ax.set_title('Monthly Tech and Related Services Sales in 2023', pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Sales (Thousand USD)')

ax.legend(loc='upper left')

plt.tight_layout()
plt.show()