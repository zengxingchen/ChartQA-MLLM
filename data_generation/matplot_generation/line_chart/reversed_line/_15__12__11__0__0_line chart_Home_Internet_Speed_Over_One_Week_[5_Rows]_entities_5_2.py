
import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
average_revenue = [1000, 1500, 1800, 1600, 2000, 2200, 2500, 2300, 2700, 2600, 2400, 2800]
average_expenses = [700, 800, 1200, 1100, 1500, 1600, 1900, 1800, 2100, 2000, 1900, 2300]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(months, average_revenue, color='#2ca02c', marker='o', label="Average Revenue")
plt.plot(months, average_expenses, color='#d62728', marker='o', label="Average Expenses")

# Highlight Highest and Lowest Points
highest_revenue = max(average_revenue)
lowest_expenses = min(average_expenses)
highest_month_revenue = months[average_revenue.index(highest_revenue)]
lowest_month_expenses = months[average_expenses.index(lowest_expenses)]

plt.annotate(f'Highest Revenue\n{highest_revenue}', xy=(highest_month_revenue, highest_revenue), xytext=(highest_month_revenue, highest_revenue+200),
             arrowprops=dict(facecolor='green', shrink=0.05), ha='center')
plt.annotate(f'Lowest Expenses\n{lowest_expenses}', xy=(lowest_month_expenses, lowest_expenses), xytext=(lowest_month_expenses, lowest_expenses-200),
             arrowprops=dict(facecolor='red', shrink=0.05), ha='center')

# Customize the rest of the chart
plt.title("Monthly Revenue and Expenses in 2023", y=1.05)
plt.xlabel("Month")
plt.ylabel("Amount (in USD)")
plt.legend(loc='upper right')
plt.grid(True)
plt.gca().invert_yaxis()
plt.tight_layout()

# Show the plot
plt.show()