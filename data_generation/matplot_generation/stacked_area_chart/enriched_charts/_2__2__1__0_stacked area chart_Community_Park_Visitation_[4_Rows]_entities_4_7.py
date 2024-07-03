
import matplotlib.pyplot as plt

quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021',
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022',
            'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023',
            'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
pop = [3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400,
       4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000]
jazz = [4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400,
        5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000]
rock = [3500, 3700, 3900, 4100, 4300, 4500, 4700, 4900,
        5100, 5300, 5500, 5700, 5900, 6100, 6300, 6500]

plt.figure(figsize=(16, 10))
plt.stackplot(quarters, pop, jazz, rock,
              labels=['Pop', 'Jazz', 'Rock'],
              colors=['#FF6347', '#4682B4', '#32CD32'])

plt.title('Quarterly Revenue from Different Music Genres', pad=40)
plt.xlabel('Quarter')
plt.ylabel('Revenue (in Thousands)')
plt.annotate('Significant Rise in Rock Revenue', xy=(15, 18200), xytext=(15, 21000),
             arrowprops=dict(facecolor='#000000', shrink=0.05))
plt.legend(loc='upper left')

plt.show()