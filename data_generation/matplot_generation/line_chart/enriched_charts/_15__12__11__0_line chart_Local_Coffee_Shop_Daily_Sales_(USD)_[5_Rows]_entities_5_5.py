
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [120, 130, 125, 140, 150, 160, 155, 165, 160, 170, 175, 180]

# Plotting the line chart
plt.figure(figsize=(14, 7))
plt.plot(months, revenue, marker='o', linestyle='-', color='#2ca02c', linewidth=3)

# Adding title and labels
plt.title('Monthly Revenue for Company ABC in 2023', fontsize=18, pad=15)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Revenue (in $1000s)', fontsize=14)

# Adding an annotation for the highest revenue
highest_revenue_index = revenue.index(max(revenue))
highest_revenue_month = months[highest_revenue_index]
plt.annotate('Highest Revenue', xy=(highest_revenue_index, max(revenue)), xytext=(highest_revenue_index, max(revenue) - 10),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

# Add a grid, invert y-axis, and show the plot
plt.grid(True)
plt.gca().invert_yaxis()
plt.ylim(180, 110)
plt.show()