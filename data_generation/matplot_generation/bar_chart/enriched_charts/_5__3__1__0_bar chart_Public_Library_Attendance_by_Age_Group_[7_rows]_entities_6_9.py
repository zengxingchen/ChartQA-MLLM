
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
tourist_visits = [2000, 1800, 1900, 2100, 2300, 2500, 2700, 2600, 2400, 2200, 2000, 2100]

# Colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#FFB833', '#33FFD7', '#D733FF', '#33FF57', '#FF5733', '#33A6FF', '#A6FF33']

# Create a vertical bar chart
plt.figure(figsize=(12, 7))  # Change the figure size (width x height)
bar_width = 0.5  # Change the bar width
plt.bar(months, tourist_visits, color=colors, width=bar_width)

# Setting the title and labels
plt.title('Monthly Tourist Visits', pad=20)
plt.xlabel('Month')
plt.ylabel('Visits (in thousands)')

# Adjust the limits if necessary
plt.ylim([1500, max(tourist_visits) + 500])

# Display the chart
plt.tight_layout()
plt.show()