
import matplotlib.pyplot as plt

days = [i for i in range(1, 32)]
steps_individual_a = [5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 9200, 9400, 9600, 9800, 10000, 10200, 10400, 10600, 10800, 11000]
steps_individual_b = [7500, 7400, 7300, 7200, 7100, 7000, 6900, 6800, 6700, 6600, 6500, 6400, 6300, 6200, 6100, 6000, 5900, 5800, 5700, 5600, 5500, 5400, 5300, 5200, 5100, 5000, 4900, 4800, 4700, 4600, 4500]

plt.figure(figsize=(14, 8))
plt.plot(days, steps_individual_a, color='#2E8B57', label='Individual A')  # SeaGreen
plt.plot(days, steps_individual_b, color='#8A2BE2', label='Individual B')  # BlueViolet

plt.title('Daily Steps Count in January', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Steps Count')

plt.annotate('Individual A Peak', xy=(31, steps_individual_a[-1]), xytext=(25, steps_individual_a[-5]),
             arrowprops=dict(facecolor='#2E8B57', shrink=0.05))

plt.annotate('Individual B Low', xy=(31, steps_individual_b[-1]), xytext=(25, steps_individual_b[-5]),
             arrowprops=dict(facecolor='#8A2BE2', shrink=0.05))

plt.grid(True)
plt.legend(loc='upper left')
plt.show()