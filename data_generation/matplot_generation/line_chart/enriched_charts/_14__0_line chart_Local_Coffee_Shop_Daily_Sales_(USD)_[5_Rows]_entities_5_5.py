
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [5, 6, 8, 7, 9, 11, 13, 12, 10, 8, 7, 6]

# Plotting the line chart
plt.figure(figsize=(14, 7))  # Change width and height of the chart
plt.plot(months, revenue, marker='o', linestyle='-', color='#ff5733', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Revenue in 2023 for Business XYZ', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($M)', fontsize=12)

# Adding an annotation for the highest revenue
highest_revenue_index = revenue.index(max(revenue))
highest_revenue_month = months[highest_revenue_index]
plt.annotate('Peak Revenue', xy=(highest_revenue_index, max(revenue)), xytext=(highest_revenue_index, max(revenue) + 1),
             arrowprops=dict(facecolor='#2ca02c', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(14, 4)
plt.gca().invert_yaxis()
plt.show()