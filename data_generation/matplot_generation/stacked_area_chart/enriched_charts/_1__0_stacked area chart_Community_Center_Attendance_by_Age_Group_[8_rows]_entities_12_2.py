
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
renewable_energy = [500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720]
healthcare = [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560]
education = [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510]
transportation = [350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460]
defense = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410]

fig, ax = plt.subplots(figsize=(14, 8))

y = np.vstack([renewable_energy, healthcare, education, transportation, defense])
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF']

ax.stackplot(months, y, labels=['Renewable Energy', 'Healthcare', 'Education', 'Transportation', 'Defense'], colors=colors)

ax.annotate('Max Renewable Energy', xy=('December', 720), xytext=('November', 750),
            arrowprops=dict(facecolor='blue', shrink=0.05))
ax.annotate('Highest Defense', xy=('December', 410 + sum(y[:-1, -1])), xytext=('November', 410 + sum(y[:-1, -2])),
            arrowprops=dict(facecolor='purple', shrink=0.05))

ax.set_title('Monthly Government Spending Breakdown in 2023', pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Spending (Million USD)')

ax.legend(loc='upper left')

plt.tight_layout()
plt.show()