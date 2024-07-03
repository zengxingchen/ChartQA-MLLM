
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
mercury = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
venus = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115]
earth = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
mars = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
jupiter = [90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]

fig, ax = plt.subplots(figsize=(16, 9))

y = np.vstack([mercury, venus, earth, mars, jupiter])

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF4500']

ax.stackplot(months, y, labels=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter'], colors=colors)

ax.annotate('Peak Jupiter Exploration', xy=('December', 145 + sum(y[:-1, -1])), xytext=('November', 155 + sum(y[:-1, -2])),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Highest Earth Study', xy=('December', 125), xytext=('November', 135),
            arrowprops=dict(facecolor='blue', shrink=0.05))

ax.set_title('Monthly Space Exploration Focus', fontsize=18)
ax.set_xlabel('Month')
ax.set_ylabel('Focus Level (Units)')

ax.legend(loc='upper left')

plt.tight_layout()
plt.show()