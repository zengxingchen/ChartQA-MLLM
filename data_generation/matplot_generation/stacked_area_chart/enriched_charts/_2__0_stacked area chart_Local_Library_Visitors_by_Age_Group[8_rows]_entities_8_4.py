
import matplotlib.pyplot as plt

quarters = [
    'Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 
    'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
    'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'
]
north_america = [50000, 60000, 75000, 85000, 90000, 95000, 100000, 105000, 110000, 115000, 120000, 125000]
europe = [70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000]
asia_pacific = [30000, 40000, 50000, 60000, 70000, 75000, 80000, 85000, 90000, 95000, 100000, 105000]

plt.figure(figsize=(12, 8))

plt.stackplot(quarters, north_america, europe, asia_pacific,
              colors=['#FF5733', '#33FF57', '#3357FF'],
              labels=['North America', 'Europe', 'Asia-Pacific'])

plt.legend(loc='upper left')

plt.title('Quarterly Tourist Arrivals by Region', pad=20)
plt.xlabel('Quarter')
plt.ylabel('Tourist Arrivals')

for i, na in enumerate(north_america):
    total_arrivals = na + europe[i] + asia_pacific[i]
    plt.text(quarters[i], total_arrivals, f'{total_arrivals}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()