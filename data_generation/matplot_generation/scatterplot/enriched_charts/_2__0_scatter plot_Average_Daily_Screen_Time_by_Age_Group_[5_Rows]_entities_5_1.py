
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
funding = [5.2, 7.1, 8.5, 10.2, 12.7, 15.3, 14.8, 13.6, 11.4, 9.8, 7.9, 6.4]

# Colors for each point
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78'
]

# Change width and height of the chart
plt.figure(figsize=(12, 8))

# Scatter plot
plt.scatter(months, funding, c=colors)

# Title and labels
plt.title('Monthly Startup Fundings', pad=20)
plt.xlabel('Month')
plt.ylabel('Funding (in millions)')

# Adjust x-axis to show each month
plt.xticks(months)

# Show plot
plt.show()