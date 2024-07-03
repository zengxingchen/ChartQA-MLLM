
import matplotlib.pyplot as plt

# Data for each year
years = list(range(2010, 2024))
solar = [5, 7, 9, 12, 16, 20, 25, 30, 36, 43, 50, 58, 65, 72]
wind = [15, 18, 21, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
hydro = [50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76]
nuclear = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]

plt.figure(figsize=(16, 9))
plt.stackplot(years, solar, wind, hydro, nuclear, colors=['#FFA07A', '#20B2AA', '#778899', '#8A2BE2'])

plt.title('Energy Production by Source (2010-2023)', fontsize=18, pad=30)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Energy Production (GW)', fontsize=14)

plt.legend(['Solar', 'Wind', 'Hydro', 'Nuclear'], loc='upper left')

plt.annotate(f'{nuclear[-1]} GW', 
             (years[-1], sum([solar[-1], wind[-1], hydro[-1], nuclear[-1]])), 
             textcoords="offset points", 
             xytext=(0, 10), 
             ha='center', 
             fontsize=12, 
             color='#8A2BE2')

plt.show()