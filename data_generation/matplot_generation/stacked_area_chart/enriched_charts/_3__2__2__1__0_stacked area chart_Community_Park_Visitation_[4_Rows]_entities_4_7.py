
import matplotlib.pyplot as plt

quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021',
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022',
            'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023',
            'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
tech = [1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600,
        3900, 4200, 4500, 4800, 5100, 5400, 5700, 6000]
health = [1600, 1900, 2200, 2500, 2800, 3100, 3400, 3700,
          4000, 4300, 4600, 4900, 5200, 5500, 5800, 6100]
finance = [1700, 2000, 2300, 2600, 2900, 3200, 3500, 3800,
           4100, 4400, 4700, 5000, 5300, 5600, 5900, 6200]

plt.figure(figsize=(14, 8))
plt.stackplot(quarters, tech, health, finance,
              labels=['Tech', 'Health', 'Finance'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

plt.title('Quarterly Growth in Different Sectors', pad=20)
plt.xlabel('Quarter')
plt.ylabel('Growth (in Millions)')
plt.annotate('Notable Increase in Health Sector', xy=(12, 15500), xytext=(12, 17000),
             arrowprops=dict(facecolor='#000000', shrink=0.05))
plt.legend(loc='upper right')

plt.show()