
import matplotlib.pyplot as plt

# Data
months = ['Q1', 'Q2', 'Q3', 'Q4']
revenue = [500, 600, 550, 650]
profit = [150, 200, 180, 220]

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(months, revenue, color='#28B463', marker='o', label="Revenue")
plt.plot(months, profit, color='#C70039', marker='o', label="Profit")

# Highlight Highest and Lowest Revenue and Profit
highest_revenue = max(revenue)
lowest_revenue = min(revenue)
highest_profit = max(profit)
lowest_profit = min(profit)

highest_revenue_month = months[revenue.index(highest_revenue)]
lowest_revenue_month = months[revenue.index(lowest_revenue)]
highest_profit_month = months[profit.index(highest_profit)]
lowest_profit_month = months[profit.index(lowest_profit)]

plt.annotate(f'Highest Revenue\n${highest_revenue}K', xy=(highest_revenue_month, highest_revenue), xytext=(highest_revenue_month, highest_revenue+30),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Lowest Revenue\n${lowest_revenue}K', xy=(lowest_revenue_month, lowest_revenue), xytext=(lowest_revenue_month, lowest_revenue-30),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Highest Profit\n${highest_profit}K', xy=(highest_profit_month, highest_profit), xytext=(highest_profit_month, highest_profit+20),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Lowest Profit\n${lowest_profit}K', xy=(lowest_profit_month, lowest_profit), xytext=(lowest_profit_month, lowest_profit-20),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

# Customize rest of the chart
plt.title("Quarterly Revenue and Profit for Company X", pad=20)
plt.xlabel("Quarter")
plt.ylabel("Amount (in K $)")
plt.gca().invert_yaxis()
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()