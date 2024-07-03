
import matplotlib.pyplot as plt

quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021',
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022',
            'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023',
            'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
physics = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000,
           23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000]
chemistry = [20000, 22000, 21000, 23000, 24000, 25000, 26000, 27000,
             28000, 29000, 30000, 31000, 32000, 33000, 34000, 35000]
biology = [25000, 23000, 26000, 27000, 28000, 29000, 30000, 31000,
           32000, 33000, 34000, 35000, 36000, 37000, 38000, 39000]

plt.figure(figsize=(12, 7))
plt.stackplot(quarters, physics, chemistry, biology,
              labels=['Physics', 'Chemistry', 'Biology'],
              colors=['#1E90FF', '#32CD32', '#FF6347'])

plt.title('Quarterly Research Funding for Science Departments', pad=20)
plt.xlabel('Quarter')
plt.ylabel('Funding (in USD)')
plt.annotate('Peak for Biology', xy=(15, 104000), xytext=(15, 120000),
             arrowprops=dict(facecolor='#8B0000', shrink=0.05))
plt.legend(loc='upper left')

plt.show()