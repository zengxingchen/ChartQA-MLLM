
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
rainfall = [78.5, 52.3, 61.8, 83.2, 95.1, 110.4, 121.9, 99.7, 87.4, 76.3, 65.9, 54.2]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff9896', '#98df8a']

plt.figure(figsize=(12, 6))
bars = plt.bar(months, rainfall, color=colors, edgecolor='black', width=0.5)

plt.ylabel('Average Rainfall (mm)')
plt.title('Monthly Average Rainfall in 2023', pad=20)
plt.ylim(0, max(rainfall) + 20)
plt.tight_layout()

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()