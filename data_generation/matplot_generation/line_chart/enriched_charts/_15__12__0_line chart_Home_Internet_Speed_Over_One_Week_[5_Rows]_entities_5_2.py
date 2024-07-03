
import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
average_high_sales = [5000, 4500, 4000, 3800, 3500, 3300, 3100, 2900, 2700, 2500, 2300, 2100]
average_low_sales = [2000, 2200, 2500, 2700, 3000, 3200, 3300, 3400, 3500, 3600, 3700, 3800]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(months, average_high_sales, color='#FF5733', marker='o', label="Average High Sales")
plt.plot(months, average_low_sales, color='#33C1FF', marker='o', label="Average Low Sales")

# Highlight Highest and Lowest Average Sales
highest_sales = max(average_high_sales)
lowest_sales = min(average_low_sales)
highest_month = months[average_high_sales.index(highest_sales)]
lowest_month = months[average_low_sales.index(lowest_sales)]

plt.annotate(f'Highest\n{highest_sales} units', xy=(highest_month, highest_sales), xytext=(highest_month, highest_sales+500),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Lowest\n{lowest_sales} units', xy=(lowest_month, lowest_sales), xytext=(lowest_month, lowest_sales-500),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

# Customize rest of the chart
plt.title("Average Monthly Sales in 2023", pad=20)
plt.xlabel("Month")
plt.ylabel("Sales (units)")
plt.legend(loc='upper right')
plt.grid(True)
plt.gca().invert_yaxis()
plt.tight_layout()

# Show the plot
plt.show()