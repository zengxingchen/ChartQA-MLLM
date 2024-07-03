
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [120, 130, 110, 140, 150, 160, 170, 180, 190, 200, 210, 220]
expenses = [80, 90, 70, 85, 95, 100, 110, 120, 130, 140, 150, 160]
profit = [40, 50, 40, 55, 55, 60, 60, 60, 60, 60, 60, 60]
investments = [20, 30, 25, 35, 40, 45, 50, 55, 60, 65, 70, 75]

plt.figure(figsize=(10, 12))
bar_height = 0.6

plt.barh(months, revenue, color='#4CAF50', edgecolor='white', height=bar_height, label='Revenue (in Thousands)')
plt.barh(months, expenses, left=revenue, color='#F44336', edgecolor='white', height=bar_height, label='Expenses (in Thousands)')
plt.barh(months, profit, left=[i+j for i,j in zip(revenue, expenses)], color='#2196F3', edgecolor='white', height=bar_height, label='Profit (in Thousands)')
plt.barh(months, investments, left=[i+j+k for i,j,k in zip(revenue, expenses, profit)], color='#FFC107', edgecolor='white', height=bar_height, label='Investments (in Thousands)')

for i, (r, e, p, inv) in enumerate(zip(revenue, expenses, profit, investments)):
    plt.text(r/2, i, str(r), ha='center', va='center', color='white', fontweight='bold')
    plt.text(r+e/2, i, str(e), ha='center', va='center', color='white', fontweight='bold')
    plt.text(r+e+p/2, i, str(p), ha='center', va='center', color='white', fontweight='bold')
    plt.text(r+e+p+inv/2, i, str(inv), ha='center', va='center', color='white', fontweight='bold')

plt.xlabel('Financial Metrics (in Thousands)')
plt.title('Monthly Financial Metrics', pad=20)
plt.legend(loc='lower right')

plt.show()