
import matplotlib.pyplot as plt

days = [i for i in range(1, 32)]
viewers_series_a = [500, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810]
viewers_series_b = [800, 790, 780, 770, 760, 750, 740, 730, 720, 710, 700, 690, 680, 670, 660, 650, 640, 630, 620, 610, 600, 590, 580, 570, 560, 550, 540, 530, 520, 510, 500]

plt.figure(figsize=(14, 8))
plt.plot(days, viewers_series_a, color='#8B0000', label='Series A')  # DarkRed
plt.plot(days, viewers_series_b, color='#4682B4', label='Series B')  # SteelBlue

plt.title('Daily Viewers of TV Series in January', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Number of Viewers')

plt.annotate('Series A Peak', xy=(31, viewers_series_a[-1]), xytext=(25, viewers_series_a[-5]),
             arrowprops=dict(facecolor='#8B0000', shrink=0.05))

plt.annotate('Series B Low', xy=(31, viewers_series_b[-1]), xytext=(25, viewers_series_b[-5]),
             arrowprops=dict(facecolor='#4682B4', shrink=0.05))

plt.gca().invert_yaxis()
plt.grid(True)
plt.legend(loc='upper left')
plt.show()