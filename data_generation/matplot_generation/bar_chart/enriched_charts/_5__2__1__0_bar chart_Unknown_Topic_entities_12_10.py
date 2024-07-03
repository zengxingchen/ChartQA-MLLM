
import matplotlib.pyplot as plt

cities = ['Paris', 'New York', 'Tokyo', 'Sydney', 'Berlin', 'London', 'Moscow', 'Rio de Janeiro', 'Toronto', 'Rome', 'Dubai', 'Beijing']
temperatures = [16.5, 13.2, 15.6, 18.2, 11.5, 12.4, 6.7, 23.0, 8.9, 17.3, 29.5, 14.1]
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6', '#33FFF6', '#F633FF', '#F6FF33', '#33A6FF', '#A6FF33', '#FF8C33', '#33FFA6']

plt.figure(figsize=(12, 9))
plt.bar(cities, temperatures, color=colors, width=0.7)
plt.ylabel('Average Temperature (°C)')
plt.title('Average Annual Temperature by City', pad=20)
plt.ylim(5, max(temperatures) + 5)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.show()