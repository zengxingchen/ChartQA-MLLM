
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
ticket_sales = [100, 85, 90, 95, 120, 110, 130, 125, 115, 105, 95, 100]

# Colors for each bar
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC', '#EFC050', '#5B5EA6']

# Create a horizontal bar chart
plt.figure(figsize=(10, 8))  # Change the figure size (width x height)
bar_height = 0.6  # Change the bar height
plt.barh(months, ticket_sales, color=colors, height=bar_height)

# Setting the title and labels
plt.title('Monthly Concert Ticket Sales')
plt.xlabel('Ticket Sales (in thousands)')
plt.ylabel('Month')

# Adjust the limits if necessary
plt.xlim([0, max(ticket_sales) + 10])

# Display the chart
plt.tight_layout()
plt.show()