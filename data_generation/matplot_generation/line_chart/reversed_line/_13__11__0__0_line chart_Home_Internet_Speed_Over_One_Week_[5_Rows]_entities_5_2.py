
import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
average_high_income = [3500, 3700, 3900, 4100, 4300, 4500, 4700, 4900, 5100, 5300, 5500, 5700]
average_low_income = [2500, 2700, 2900, 3100, 3300, 3500, 3700, 3900, 4100, 4300, 4500, 4700]

# Create the plot
plt.figure(figsize=(14, 8))
plt.plot(months, average_high_income, color='#1f77b4', marker='o', label="Average High Income")
plt.plot(months, average_low_income, color='#ff7f0e', marker='o', label="Average Low Income")

# Highlight Highest and Lowest Average Incomes
highest_income = max(average_high_income)
lowest_income = min(average_low_income)
highest_month = months[average_high_income.index(highest_income)]
lowest_month = months[average_low_income.index(lowest_income)]

plt.annotate(f'Highest\n${highest_income}', xy=(highest_month, highest_income), xytext=(highest_month, highest_income+200),
             arrowprops=dict(facecolor='green', shrink=0.05), ha='center')
plt.annotate(f'Lowest\n${lowest_income}', xy=(lowest_month, lowest_income), xytext=(lowest_month, lowest_income-200),
             arrowprops=dict(facecolor='red', shrink=0.05), ha='center')

# Customize the rest of the chart
plt.title("Monthly Average Incomes in City Y", y=1.05)
plt.xlabel("Month")
plt.ylabel("Income ($)")
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()