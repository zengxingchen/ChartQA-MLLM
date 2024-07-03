
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
hours_spent = [3.2, 4.1, 5.5, 6.8, 7.2, 8.1, 7.9, 7.4, 6.2, 5.9, 4.7, 3.9]

# Colors for each point
colors = [
    '#4B0082', '#FF1493', '#00FF00', '#FFD700', '#FF4500',
    '#00CED1', '#8A2BE2', '#FF69B4', '#556B2F', '#00FA9A', '#7FFF00', '#DC143C'
]

# Change width and height of the chart
plt.figure(figsize=(14, 10))

# Scatter plot
plt.scatter(months, hours_spent, c=colors)

# Title and labels
plt.title('Monthly Hours Spent on Mental Health Activities', pad=20)
plt.xlabel('Month')
plt.ylabel('Hours Spent')

# Adjust x-axis to show each month
plt.xticks(months)

# Show plot
plt.show()