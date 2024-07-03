
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [15.2, 16.7, 19.5, 22.4, 25.3, 28.9, 30.2, 31.6, 27.8, 24.1, 21.5, 18.3]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1a55b4', '#ff8c00']

plt.figure(figsize=(12, 6))
bars = plt.bar(months, revenue, color=colors, edgecolor='black', width=0.5)

plt.ylabel('Monthly Revenue (Million $)')
plt.title('Monthly Revenue of ABC Corp in 2023')
plt.ylim(0, max(revenue) + 5)
plt.tight_layout()

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()