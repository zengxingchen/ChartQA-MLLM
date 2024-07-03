
import matplotlib.pyplot as plt
import numpy as np

cities = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
    'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 
    'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte', 
    'San Francisco', 'Indianapolis', 'Seattle', 'Denver', 'Washington', 
    'Boston', 'El Paso', 'Nashville', 'Detroit', 'Oklahoma City', 
    'Las Vegas', 'Baltimore', 'Louisville', 'Milwaukee', 'Portland'
]
revenue = [
    500000, 450000, 300000, 350000, 320000, 
    280000, 330000, 290000, 310000, 270000, 
    260000, 240000, 250000, 230000, 220000, 
    400000, 210000, 380000, 290000, 370000, 
    410000, 200000, 280000, 310000, 270000, 
    360000, 300000, 250000, 240000, 340000
]
profit = [
    120000, 130000, 80000, 90000, 85000, 
    70000, 95000, 75000, 85000, 65000, 
    60000, 55000, 60000, 50000, 52000, 
    110000, 49000, 95000, 72000, 105000, 
    115000, 46000, 70000, 81000, 67000, 
    93000, 75000, 62000, 60000, 85000
]
expenses = [
    380000, 320000, 220000, 260000, 235000, 
    210000, 235000, 215000, 225000, 205000, 
    200000, 185000, 190000, 180000, 168000, 
    290000, 161000, 285000, 218000, 265000, 
    295000, 154000, 210000, 229000, 203000, 
    267000, 225000, 188000, 180000, 255000
]

total = np.array(revenue) + np.array(profit) + np.array(expenses)
revenue_perc = np.array(revenue) / total * 100
profit_perc = np.array(profit) / total * 100
expenses_perc = np.array(expenses) / total * 100

fig, ax = plt.subplots(figsize=(14, 10))

bar_width = 0.7
bar_positions = np.arange(len(cities))

ax.bar(bar_positions, revenue_perc, color='#1f77b4', edgecolor='white', width=bar_width, label='Revenue')
ax.bar(bar_positions, profit_perc, bottom=revenue_perc, color='#ff7f0e', edgecolor='white', width=bar_width, label='Profit')
ax.bar(bar_positions, expenses_perc, bottom=revenue_perc+profit_perc, color='#2ca02c', edgecolor='white', width=bar_width, label='Expenses')

ax.set_xticks(bar_positions)
ax.set_xticklabels(cities, rotation=90)
ax.set_ylabel('Percentage')
ax.set_title('Business Financial Distribution in Major US Cities')
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()