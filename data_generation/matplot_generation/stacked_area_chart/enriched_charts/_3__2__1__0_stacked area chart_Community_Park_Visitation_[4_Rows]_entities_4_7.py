
import matplotlib.pyplot as plt

quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021',
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022',
            'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023',
            'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']

vegetables = [10500, 11200, 11800, 12700, 13500, 14200, 15000, 15800,
              16700, 17500, 18200, 19200, 20200, 21000, 21800, 22700]

fruits = [15200, 15800, 16500, 17500, 18200, 19000, 19800, 20700,
          21500, 22500, 23500, 24500, 25500, 26500, 27500, 28500]

grains = [12500, 13500, 14500, 15500, 16200, 17200, 18000, 19000,
          20000, 21000, 22000, 23000, 24200, 25200, 26200, 27200]

plt.figure(figsize=(16, 10))
plt.stackplot(quarters, vegetables, fruits, grains,
              labels=['Vegetables', 'Fruits', 'Grains'],
              colors=['#4CAF50', '#FFEB3B', '#FF5722'])

plt.title('Quarterly Sales of Food Items (2021-2024)', pad=40)
plt.xlabel('Quarter')
plt.ylabel('Sales (in USD)')
plt.annotate('Highest Sales in Q4 2024', xy=(15, 78400), xytext=(15, 85000),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.legend(loc='upper left')

plt.show()