
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
streaming_services = [700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920]
social_media = [600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710]
online_shopping = [550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660]
education_platforms = [500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610]
gaming = [450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560]

fig, ax = plt.subplots(figsize=(16, 10))

y = np.vstack([streaming_services, social_media, online_shopping, education_platforms, gaming])
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#EE82EE']

ax.stackplot(months, y, labels=['Streaming Services', 'Social Media', 'Online Shopping', 'Education Platforms', 'Gaming'], colors=colors)

ax.annotate('Peak Streaming', xy=('December', 920), xytext=('November', 940),
            arrowprops=dict(facecolor='red', shrink=0.05))
ax.annotate('Peak Gaming', xy=('December', 560 + sum(y[:-1, -1])), xytext=('November', 560 + sum(y[:-1, -2])),
            arrowprops=dict(facecolor='purple', shrink=0.05))

ax.set_title('Monthly Internet Usage Breakdown in 2023', pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Usage (Million Hours)')

ax.legend(loc='upper left')

plt.tight_layout()
plt.show()