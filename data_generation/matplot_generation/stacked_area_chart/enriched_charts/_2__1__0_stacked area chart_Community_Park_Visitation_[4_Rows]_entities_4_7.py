
import matplotlib.pyplot as plt

quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021',
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022',
            'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023',
            'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']

ad_revenue = [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000,
              18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000]

subscription_revenue = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000,
                        23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000]

merchandise_revenue = [12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000,
                       20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000]

plt.figure(figsize=(14, 8))
plt.stackplot(quarters, ad_revenue, subscription_revenue, merchandise_revenue,
              labels=['Ad Revenue', 'Subscription Revenue', 'Merchandise Revenue'],
              colors=['#FF5733', '#33FF57', '#3357FF'])

plt.title('Quarterly Revenue Streams for a Media Company', pad=20)
plt.xlabel('Quarter')
plt.ylabel('Revenue (in USD)')
plt.annotate('Peak in Q4 2024', xy=(15, 82000), xytext=(15, 90000),
             arrowprops=dict(facecolor='#8B0000', shrink=0.05))
plt.legend(loc='upper right')

plt.show()