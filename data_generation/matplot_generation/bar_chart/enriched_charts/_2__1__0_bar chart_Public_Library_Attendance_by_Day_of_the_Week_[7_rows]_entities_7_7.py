
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
temperature = [5.2, 6.1, 10.5, 14.4, 18.3, 22.9, 25.2, 24.6, 20.8, 15.1, 9.5, 6.3]
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', '#e67e22',
          '#1abc9c', '#34495e', '#d35400', '#2980b9', '#8e44ad', '#c0392b']

plt.figure(figsize=(10, 8))
bars = plt.barh(months, temperature, color=colors, edgecolor='black', height=0.6)

plt.xlabel('Average Temperature (°C)')
plt.title('Monthly Average Temperature in 2023')
plt.xlim(0, max(temperature) + 5)
plt.tight_layout()

plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()