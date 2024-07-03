
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]
revenue = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
profit = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

# Plot setup
fig, ax = plt.subplots(figsize=(14, 8))

# Create bar chart
bar_height = 0.3
bar_locations_sales = range(len(sales))
bar_locations_revenue = [x + bar_height for x in bar_locations_sales]
bar_locations_profit = [x + bar_height for x in bar_locations_revenue]

bars1 = ax.barh(bar_locations_sales, sales, bar_height, label='Sales (units)', color='#1f77b4')
bars2 = ax.barh(bar_locations_revenue, revenue, bar_height, label='Revenue (USD)', color='#ff7f0e')
bars3 = ax.barh(bar_locations_profit, profit, bar_height, label='Profit (USD)', color='#2ca02c')

# Set the position of the y ticks
ax.set_yticks([r + bar_height for r in range(len(sales))])
ax.set_yticklabels(months)

# Set y-axis limits
ax.set_ylim(5, 14)

# Adding labels and title
plt.xlabel('Measurements')
plt.title('Monthly Business Performance', pad=20)
ax.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()