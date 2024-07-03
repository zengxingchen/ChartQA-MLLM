
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
electric_cars = [12000, 15000, 18000, 21000, 26000, 32000, 38000]
hybrid_cars = [18000, 22000, 26000, 32000, 38000, 43500, 49500]
diesel_cars = [32000, 31000, 29500, 27000, 24000, 21000, 18000]

# Bottom data for stacking
hybrid_bottom = [i + j for i, j in zip(electric_cars, hybrid_cars)]
electric_bottom = electric_cars

# Figure and Axes
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height of the chart

# Stacked Horizontal Bars
ax.barh(years, electric_cars, color='#1f77b4', edgecolor='white', height=0.5)  # Electric cars with blue color
ax.barh(years, hybrid_cars, left=electric_bottom, color='#2ca02c', edgecolor='white', height=0.5)  # Hybrid cars with green color
ax.barh(years, diesel_cars, left=hybrid_bottom, color='#d62728', edgecolor='white', height=0.5)  # Diesel cars with red color

# Labels and Title
ax.set_xlabel('Number of Cars Sold')
ax.set_ylabel('Year')
ax.set_title('Car Sales by Type from 2015 to 2021')

# Display the plot
plt.show()