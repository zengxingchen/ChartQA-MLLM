
import matplotlib.pyplot as plt

chart_data = [
    {'Month': 'January', 'Net Income': 8000, 'Revenue': 25000, 'Expenses': 17000, 'Profit Margin': 32},
    {'Month': 'February', 'Net Income': 9000, 'Revenue': 26000, 'Expenses': 17000, 'Profit Margin': 35},
    {'Month': 'March', 'Net Income': 8500, 'Revenue': 25500, 'Expenses': 17000, 'Profit Margin': 33},
    {'Month': 'April', 'Net Income': 9500, 'Revenue': 27000, 'Expenses': 17500, 'Profit Margin': 35},
    {'Month': 'May', 'Net Income': 10000, 'Revenue': 28000, 'Expenses': 18000, 'Profit Margin': 36},
    {'Month': 'June', 'Net Income': 11000, 'Revenue': 29000, 'Expenses': 18000, 'Profit Margin': 38},
    {'Month': 'July', 'Net Income': 11500, 'Revenue': 30000, 'Expenses': 18500, 'Profit Margin': 38},
    {'Month': 'August', 'Net Income': 12000, 'Revenue': 31000, 'Expenses': 19000, 'Profit Margin': 39},
    {'Month': 'September', 'Net Income': 12500, 'Revenue': 32000, 'Expenses': 19500, 'Profit Margin': 39},
    {'Month': 'October', 'Net Income': 13000, 'Revenue': 33000, 'Expenses': 20000, 'Profit Margin': 39},
    {'Month': 'November', 'Net Income': 13500, 'Revenue': 34000, 'Expenses': 20500, 'Profit Margin': 40},
    {'Month': 'December', 'Net Income': 14000, 'Revenue': 35000, 'Expenses': 21000, 'Profit Margin': 40}
]

months = [entry['Month'] for entry in chart_data]
net_income = [entry['Net Income'] for entry in chart_data]
revenue = [entry['Revenue'] for entry in chart_data]
expenses = [entry['Expenses'] for entry in chart_data]
profit_margin = [entry['Profit Margin'] for entry in chart_data]

plt.figure(figsize=(18, 10))

plt.plot(months, net_income, label='Net Income', marker='o', linestyle='-', color='#1f77b4')
plt.plot(months, revenue, label='Revenue', marker='s', linestyle='--', color='#ff7f0e')
plt.plot(months, expenses, label='Expenses', marker='^', linestyle='-.', color='#2ca02c')
plt.plot(months, profit_margin, label='Profit Margin', marker='d', linestyle=':', color='#d62728')

plt.gca().invert_yaxis()

plt.title('Monthly Business Performance', fontsize=22, pad=25)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Metrics', fontsize=16)
plt.xticks(rotation=45, fontsize=14)

for i, txt in enumerate(net_income):
    plt.annotate(txt, (months[i], net_income[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.legend(loc='lower left', fontsize=14)

plt.tight_layout()
plt.show()