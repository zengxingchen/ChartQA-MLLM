
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [10.5, 12.3, 15.8, 18.2, 22.1, 25.4, 28.9, 27.7, 24.4, 19.3, 14.9, 11.2]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', 
          '#c4e17f', '#76d7c4', '#f7b7a3', '#ff9999', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(10, 8))
bars = plt.barh(months, temperatures, color=colors, edgecolor='black', height=0.6)

plt.xlabel('Average Temperature (°C)')
plt.title('Monthly Average Temperatures in 2023', pad=20)
plt.xlim(5, max(temperatures) + 5)
plt.tight_layout()

plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()