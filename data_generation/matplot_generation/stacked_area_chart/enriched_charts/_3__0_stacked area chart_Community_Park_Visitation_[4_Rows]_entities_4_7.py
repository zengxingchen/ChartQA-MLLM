
import matplotlib.pyplot as plt

quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022',
            'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023']
product_a = [12000, 18000, 14000, 15000, 16000, 17000, 18000, 19000,
             20000, 21000, 22000, 23000]
product_b = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000,
             23000, 24000, 25000, 26000]
product_c = [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000,
             18000, 19000, 20000, 21000]

plt.figure(figsize=(12, 8))
plt.stackplot(quarters, product_a, product_b, product_c, 
              labels=['Product A', 'Product B', 'Product C'],
              colors=['#FF6347', '#4682B4', '#32CD32'])

plt.title('Quarterly Revenue Growth for Products A, B, and C', pad=20)
plt.xlabel('Quarter')
plt.ylabel('Revenue (in USD)')

plt.annotate('Peak for Product B', xy=(11, 71000), xytext=(10, 75000),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.legend(loc='upper left')

plt.show()