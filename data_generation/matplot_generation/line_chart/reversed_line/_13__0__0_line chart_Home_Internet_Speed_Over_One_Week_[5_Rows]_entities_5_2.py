
import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
production_q1 = [300, 280, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170]
production_q2 = [150, 180, 170, 190, 200, 210, 220, 230, 240, 250, 260, 270]

# Create the plot
plt.figure(figsize=(16, 10))
plt.plot(months, production_q1, color='#d62728', marker='o', label="Production Q1")
plt.plot(months, production_q2, color='#2ca02c', marker='o', label="Production Q2")

# Highlight Highest and Lowest Production
highest_prod = max(production_q1)
lowest_prod = min(production_q2)
highest_month = months[production_q1.index(highest_prod)]
lowest_month = months[production_q2.index(lowest_prod)]

plt.annotate(f'Highest\n{highest_prod}', xy=(highest_month, highest_prod), xytext=(highest_month, highest_prod+15),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Lowest\n{lowest_prod}', xy=(lowest_month, lowest_prod), xytext=(lowest_month, lowest_prod-15),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

# Customize rest of the chart
plt.title("Monthly Production Levels in Factory Z", y=1.05)
plt.xlabel("Month")
plt.ylabel("Production (units)")
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()