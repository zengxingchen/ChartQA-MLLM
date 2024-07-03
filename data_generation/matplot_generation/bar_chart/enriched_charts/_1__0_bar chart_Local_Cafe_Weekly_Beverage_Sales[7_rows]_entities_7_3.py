
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
average_temperature = [30, 32, 45, 55, 65, 75, 80, 78, 70, 58, 45, 35]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#9edae5', '#f7b6d2']

plt.figure(figsize=(10, 12))
plt.bar(months, average_temperature, color=colors, edgecolor='black', width=0.5)

plt.ylabel('Average Temperature (°F)', fontsize=12)
plt.xlabel('Month', fontsize=12)
plt.title('Monthly Average Temperature in 2021', fontsize=16)
plt.ylim(0, 100)

plt.tight_layout()
plt.show()