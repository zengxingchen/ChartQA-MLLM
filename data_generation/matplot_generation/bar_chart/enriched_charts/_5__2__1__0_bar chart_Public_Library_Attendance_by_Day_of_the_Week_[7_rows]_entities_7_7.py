
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [50, 60, 80, 100, 120, 150, 170, 160, 140, 130, 110, 90]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78']

plt.figure(figsize=(12, 6))
bars = plt.bar(months, revenue, color=colors, edgecolor='black', width=0.5)

plt.ylabel('Monthly Revenue (in thousands)')
plt.title('Monthly Revenue for a Tech Startup in 2023')
plt.ylim(40, max(revenue) + 10)
plt.tight_layout()

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()