import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [18.3, 19.2, 21.4, 23.7, 26.1, 28.4, 29.8, 31.2, 30.7, 27.5, 24.3, 22.1]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF', '#FF8C33',
          '#33FFF3', '#F3FF33', '#FF3333', '#3333FF', '#33FF8C', '#A8FF33']

plt.figure(figsize=(10, 8))
bars = plt.barh(months, revenue, color=colors, edgecolor='black', height=0.6)

plt.xlabel('Monthly Revenue (Million $)')
plt.title('Monthly Revenue of DEF Inc. in 2023')
plt.xlim(0, max(revenue) + 5)
plt.tight_layout()

plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()