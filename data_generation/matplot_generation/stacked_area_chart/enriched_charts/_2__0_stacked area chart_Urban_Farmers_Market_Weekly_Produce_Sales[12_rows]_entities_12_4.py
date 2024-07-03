
import matplotlib.pyplot as plt

# Data for stacked area chart
years = range(2012, 2023)
electric_bicycles = [3000, 4500, 6000, 7500, 9000, 11000, 13000, 15000, 17000, 19000, 21000]
hybrid_bicycles = [8000, 8500, 9000, 10000, 12000, 14000, 16000, 18000, 20000, 22000, 25000]
mountain_bikes = [60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000, 105000, 110000]
road_bikes = [90000, 85000, 80000, 75000, 70000, 65000, 60000, 55000, 50000, 45000, 40000]

# Plot
plt.figure(figsize=(14, 10))  # Change width and height of the chart
plt.stackplot(years, electric_bicycles, hybrid_bicycles, mountain_bikes, road_bikes, 
              colors=['#4B0082', '#FFD700', '#228B22', '#FF4500'])

# Customize the plot
plt.title('Bicycle Sales by Type from 2012 to 2022', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Bicycles Sold', fontsize=14)
plt.legend(['Electric Bicycles', 'Hybrid Bicycles', 'Mountain Bikes', 'Road Bikes'], loc='upper left')

# Annotation
for i, y in enumerate(years):
    plt.annotate(f'{electric_bicycles[i]}', (y, electric_bicycles[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()