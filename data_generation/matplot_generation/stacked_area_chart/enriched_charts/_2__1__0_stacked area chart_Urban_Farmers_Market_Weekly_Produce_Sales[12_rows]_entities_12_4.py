
import matplotlib.pyplot as plt

# Data for stacked area chart
years = range(2012, 2024)
asia = [10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000, 30000, 32000]
europe = [15000, 17000, 19000, 21000, 23000, 25000, 27000, 29000, 31000, 33000, 35000, 37000]
north_america = [8000, 9000, 10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000]
oceania = [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500]

# Plot
plt.figure(figsize=(16, 10))  # Change width and height of the chart
plt.stackplot(years, asia, europe, north_america, oceania, 
              colors=['#FFA07A', '#20B2AA', '#9370DB', '#FFD700'])

# Customize the plot
plt.title('Tourism Growth by Region from 2012 to 2023', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Tourists (in thousands)', fontsize=14)
plt.legend(['Asia', 'Europe', 'North America', 'Oceania'], loc='upper left')

# Annotation
for i, y in enumerate(years):
    plt.annotate(f'{asia[i]}', (y, asia[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
    plt.annotate(f'{europe[i]}', (y, asia[i] + europe[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
    plt.annotate(f'{north_america[i]}', (y, asia[i] + europe[i] + north_america[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
    plt.annotate(f'{oceania[i]}', (y, asia[i] + europe[i] + north_america[i] + oceania[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

plt.show()