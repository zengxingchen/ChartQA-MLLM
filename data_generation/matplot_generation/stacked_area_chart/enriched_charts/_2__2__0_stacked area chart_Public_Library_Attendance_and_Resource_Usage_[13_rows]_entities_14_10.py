
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Category': ['2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4', '2023-Q1', '2023-Q2', '2023-Q3', '2023-Q4', '2024-Q1', '2024-Q2', '2024-Q3', '2024-Q4'],
    'Flights': [1100, 1200, 1150, 1300, 1400, 1550, 1450, 1600, 1700, 1650, 1800, 1900, 2000, 2100, 2200, 2300],
    'Hotels': [950, 1100, 1000, 1250, 1300, 1400, 1350, 1500, 1550, 1500, 1600, 1700, 1800, 1850, 1900, 2000],
    'Car Rentals': [700, 850, 780, 900, 920, 1050, 950, 1100, 1150, 1200, 1300, 1350, 1400, 1450, 1500, 1550]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(df['Category'], df['Flights'], df['Hotels'], df['Car Rentals'],
             labels=['Flights', 'Hotels', 'Car Rentals'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

plt.title('Quarterly Travel Trends', pad=20, fontsize=16)
plt.xlabel('Quarter')
plt.ylabel('Bookings')
plt.legend(loc='upper left')

for i, (category, flights, hotels, car_rentals) in enumerate(zip(df['Category'], df['Flights'], df['Hotels'], df['Car Rentals'])):
    total_bookings = flights + hotels + car_rentals
    ax.annotate(f'Total: {total_bookings}', (category, total_bookings), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

plt.tight_layout()
plt.show()