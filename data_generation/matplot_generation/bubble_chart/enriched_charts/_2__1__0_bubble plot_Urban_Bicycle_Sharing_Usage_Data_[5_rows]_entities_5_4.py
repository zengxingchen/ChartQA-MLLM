
import matplotlib.pyplot as plt

cities = ['New York', 'Tokyo', 'Bangkok', 'Sydney', 'Dubai', 'Singapore', 'Hong Kong', 'Los Angeles', 'Barcelona', 'Istanbul', 'Amsterdam', 'Berlin', 'Cape Town', 'Toronto', 'Rio de Janeiro', 'Moscow', 'Chicago', 'Miami', 'Mexico City', 'Shanghai']
avg_rainfall = [98, 105, 150, 86, 10, 178, 156, 26, 72, 85, 66, 45, 52, 77, 101, 70, 95, 160, 95, 117]
avg_temp = [12.6, 16.2, 28.2, 18.5, 28.9, 27.8, 24.0, 18.3, 17.8, 15.2, 12.3, 10.2, 17.3, 9.1, 25.1, 5.4, 11.7, 25.5, 16.0, 18.5]
number_of_parks = [170, 100, 55, 400, 40, 50, 30, 120, 90, 35, 85, 75, 25, 60, 80, 50, 150, 200, 100, 60]

size_factor = 10
sizes = [p * size_factor for p in number_of_parks]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

plt.figure(figsize=(14,10))
plt.scatter(avg_rainfall, avg_temp, s=sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=0.5)

plt.title('Number of Parks vs. Average Temperature with Average Rainfall Bubble Sizes', pad=20)
plt.xlabel('Average Monthly Rainfall (mm)')
plt.ylabel('Average Temperature (°C)')

for i, city in enumerate(cities):
    plt.text(avg_rainfall[i], avg_temp[i], city, ha='center', va='center', fontsize=8)

plt.tight_layout()
plt.show()