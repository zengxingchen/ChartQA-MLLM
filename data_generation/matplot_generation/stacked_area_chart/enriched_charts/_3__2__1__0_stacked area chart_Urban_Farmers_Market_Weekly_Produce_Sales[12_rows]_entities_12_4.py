
import matplotlib.pyplot as plt

years = range(2010, 2023)
asia = [150, 180, 210, 250, 290, 330, 380, 430, 490, 550, 610, 670, 740]
europe = [200, 220, 240, 270, 300, 340, 380, 420, 470, 520, 570, 630, 700]
north_america = [100, 130, 160, 190, 230, 270, 310, 350, 400, 450, 500, 560, 620]
oceania = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]

plt.figure(figsize=(18, 12))
plt.stackplot(years, asia, europe, north_america, oceania, 
              colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A1'])

plt.title('Electric Vehicle Adoption by Region from 2010 to 2022', fontsize=20, pad=25)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Number of Electric Vehicles (in thousands)', fontsize=16)
plt.legend(['Asia', 'Europe', 'North America', 'Oceania'], loc='upper left')

for i, y in enumerate(years):
    plt.annotate(f'{asia[i]}', (y, asia[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=10)
    plt.annotate(f'{europe[i]}', (y, asia[i] + europe[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=10)
    plt.annotate(f'{north_america[i]}', (y, asia[i] + europe[i] + north_america[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=10)
    plt.annotate(f'{oceania[i]}', (y, asia[i] + europe[i] + north_america[i] + oceania[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=10)

plt.show()