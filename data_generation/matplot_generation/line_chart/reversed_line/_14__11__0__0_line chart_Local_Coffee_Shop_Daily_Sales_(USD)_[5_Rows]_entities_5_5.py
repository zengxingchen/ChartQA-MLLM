
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [12, 15, 20, 25, 30, 35, 40, 38, 33, 28, 22, 18]

# Plotting the line chart
plt.figure(figsize=(12, 6))  # Change width and height of the chart
plt.plot(months, revenue, marker='s', linestyle='--', color='#ff33cc', linewidth=2)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Revenue of Company ABC', fontsize=18)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue (in millions)', fontsize=12)

# Adding an annotation for the highest revenue
highest_revenue_index = revenue.index(max(revenue))
highest_revenue_month = months[highest_revenue_index]
plt.annotate('Peak Revenue', xy=(highest_revenue_index, max(revenue)), xytext=(highest_revenue_index, max(revenue) + 5),
             arrowprops=dict(facecolor='#33ff77', shrink=0.05))

# Invert y-axis to meet the requirement
plt.gca().invert_yaxis()

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(45, 10)
plt.show()