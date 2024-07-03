
import matplotlib.pyplot as plt

# Data for stacked area chart
years = range(2012, 2023)
electric_cars = [5000, 7000, 10000, 15000, 25000, 35000, 50000, 70000, 90000, 120000, 150000]
hybrid_cars = [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000]
diesel_cars = [120000, 115000, 110000, 105000, 95000, 90000, 85000, 80000, 75000, 65000, 55000]
petrol_cars = [200000, 195000, 185000, 180000, 170000, 160000, 150000, 140000, 130000, 120000, 110000]

# Plot
plt.figure(figsize=(12, 8))  # Change width and height of the chart
plt.stackplot(years, electric_cars, hybrid_cars, diesel_cars, petrol_cars, 
              colors=['#1f77b4', '#2ca02c', '#d62728', '#ff7f0e'])

# Customize the plot
plt.title('Car Sales by Type from 2012 to 2022')
plt.xlabel('Year')
plt.ylabel('Number of Cars Sold')
plt.legend(['Electric Cars', 'Hybrid Cars', 'Diesel Cars', 'Petrol Cars'], loc='upper left')

# Annotation
for i, y in enumerate(years):
    plt.annotate(f'{electric_cars[i]}', (y, electric_cars[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()