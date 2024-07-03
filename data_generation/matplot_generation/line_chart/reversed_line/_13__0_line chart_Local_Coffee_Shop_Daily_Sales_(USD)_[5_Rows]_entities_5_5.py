
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [12, 15, 10, 8, 18, 22, 25, 23, 19, 14, 11, 9]

# Plotting the line chart
plt.figure(figsize=(10, 5))  # Change width and height of the chart
plt.plot(months, revenue, marker='o', linestyle='-', color='#ff5733', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Revenue in Company ABC (in $1000)', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue (in $1000)', fontsize=12)

# Adding an annotation for the highest revenue
highest_revenue_index = revenue.index(max(revenue))
highest_revenue_month = months[highest_revenue_index]
plt.annotate('Highest', xy=(highest_revenue_index, max(revenue)), xytext=(highest_revenue_index, max(revenue) + 3),
             arrowprops=dict(facecolor='#007acc', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(5, 30)
plt.gca().invert_yaxis()  # Invert y-axis
plt.show()