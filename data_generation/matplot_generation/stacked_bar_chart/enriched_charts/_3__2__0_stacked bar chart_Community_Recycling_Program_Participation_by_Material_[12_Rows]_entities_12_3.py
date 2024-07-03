
import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
salaries = [3000, 3200, 3100, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200]
investments = [550, 650, 600, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100]
savings = [1200, 1300, 1100, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800]
expenses = [1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900]

bars_investments = np.add(salaries, savings).tolist()

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

fig, ax = plt.subplots(figsize=(14, 7))

ax.barh(months, salaries, color=colors[0], edgecolor='white', height=0.5, label='Salaries')
ax.barh(months, investments, left=salaries, color=colors[1], edgecolor='white', height=0.5, label='Investments')
ax.barh(months, savings, left=bars_investments, color=colors[2], edgecolor='white', height=0.5, label='Savings')
ax.barh(months, expenses, left=np.add(bars_investments, investments).tolist(), color=colors[3], edgecolor='white', height=0.5, label='Expenses')

for i in range(len(months)):
    plt.text(salaries[i] / 2, i, str(salaries[i]), ha='center', va='center', color='black')
    plt.text(salaries[i] + investments[i] / 2, i, str(investments[i]), ha='center', va='center', color='black')
    plt.text(salaries[i] + investments[i] + savings[i] / 2, i, str(savings[i]), ha='center', va='center', color='black')
    plt.text(salaries[i] + investments[i] + savings[i] + expenses[i] / 2, i, str(expenses[i]), ha='center', va='center', color='black')

plt.title('Monthly Financial Distribution', pad=20)
plt.xlabel('Amount in USD')
plt.ylabel('Month')
plt.legend(loc='lower right')
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()