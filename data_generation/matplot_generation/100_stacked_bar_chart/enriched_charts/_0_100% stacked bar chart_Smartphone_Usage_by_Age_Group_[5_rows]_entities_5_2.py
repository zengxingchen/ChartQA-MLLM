
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
electric_cars = np.array([5, 7, 10, 10, 12, 15, 18, 20])
hybrid_cars = np.array([15, 18, 20, 25, 27, 30, 32, 35])
gasoline_cars = np.array([55, 53, 50, 45, 40, 35, 30, 25])
diesel_cars = np.array([25, 22, 20, 20, 21, 20, 20, 20])

# Normalize the data to sum up to 1 (100%)
total = electric_cars + hybrid_cars + gasoline_cars + diesel_cars
electric_cars_percent = electric_cars / total * 100
hybrid_cars_percent = hybrid_cars / total * 100
gasoline_cars_percent = gasoline_cars / total * 100
diesel_cars_percent = diesel_cars / total * 100

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(years, electric_cars_percent, color='#1f77b4', edgecolor='white', height=0.8)
ax.barh(years, hybrid_cars_percent, left=electric_cars_percent, color='#ff7f0e', edgecolor='white', height=0.8)
ax.barh(years, gasoline_cars_percent, left=electric_cars_percent + hybrid_cars_percent, color='#2ca02c', edgecolor='white', height=0.8)
ax.barh(years, diesel_cars_percent, left=electric_cars_percent + hybrid_cars_percent + gasoline_cars_percent, color='#d62728', edgecolor='white', height=0.8)

# Add some text for labels and custom x-axis tick labels
ax.set_xlabel('Percentage')
ax.set_title('Market Share of Car Types from 2015 to 2022')
ax.set_yticks(range(len(years)))
ax.set_yticklabels(years)
ax.set_xlim(0, 100)

# Adding legend
ax.legend(['Electric Cars', 'Hybrid Cars', 'Gasoline Cars', 'Diesel Cars'], loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=4)

# Show the percentages on the bars
for i in range(len(years)):
    ax.text(electric_cars_percent[i]/2, i, f'{electric_cars_percent[i]:.1f}%', va='center', ha='center', color='white')
    ax.text(electric_cars_percent[i] + hybrid_cars_percent[i]/2, i, f'{hybrid_cars_percent[i]:.1f}%', va='center', ha='center', color='white')
    ax.text(electric_cars_percent[i] + hybrid_cars_percent[i] + gasoline_cars_percent[i]/2, i, f'{gasoline_cars_percent[i]:.1f}%', va='center', ha='center', color='white')
    ax.text(electric_cars_percent[i] + hybrid_cars_percent[i] + gasoline_cars_percent[i] + diesel_cars_percent[i]/2, i, f'{diesel_cars_percent[i]:.1f}%', va='center', ha='center', color='white')

# Display the plot
plt.tight_layout()
plt.show()