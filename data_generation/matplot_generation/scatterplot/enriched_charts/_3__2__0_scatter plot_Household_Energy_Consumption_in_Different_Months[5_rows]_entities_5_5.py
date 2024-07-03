
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
daily_revenue = [1200, 1350, 1100, 1400, 1380, 1420, 1430, 1390, 1410, 1450, 1460, 1440, 1370, 1360, 1340, 1330, 1310, 1290, 1320, 1410, 1370, 1390, 1430, 1450, 1480, 1490, 1510, 1450, 1430, 1400]
daily_expenses = [800, 850, 750, 900, 870, 890, 920, 860, 880, 910, 930, 920, 850, 840, 820, 810, 790, 770, 800, 880, 850, 870, 920, 940, 960, 970, 980, 940, 920, 890]

# Create a scatterplot
plt.figure(figsize=(16, 10))
plt.scatter(days, daily_revenue, c="#2ca02c", label="Daily Revenue")
plt.scatter(days, daily_expenses, c="#d62728", label="Daily Expenses")

# Customize the chart
plt.title("Daily Business Performance", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Amount ($)")
plt.legend(loc='upper left')
plt.grid(True)

# Show the scatterplot
plt.show()