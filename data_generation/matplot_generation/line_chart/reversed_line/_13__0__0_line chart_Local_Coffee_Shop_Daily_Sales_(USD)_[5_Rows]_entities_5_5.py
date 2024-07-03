
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
page_views = [1000, 1200, 1100, 1500, 1800, 1700, 1600, 1900, 2100, 2300, 2500, 2400]

# Plotting the line chart
plt.figure(figsize=(16, 8))  # Change width and height of the chart
plt.plot(months, page_views, marker='o', linestyle='-', color='#1f77b4', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Website Page Views', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Page Views', fontsize=12)

# Adding an annotation for the highest page views
highest_views_index = page_views.index(max(page_views))
highest_views_month = months[highest_views_index]
plt.annotate('Peak Page Views', xy=(highest_views_index, max(page_views)), xytext=(highest_views_index, max(page_views) + 200),
             arrowprops=dict(facecolor='#ff4500', shrink=0.05))

# Adding a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(900, 2600)
plt.gca().invert_yaxis()  # Invert the y-axis
plt.show()