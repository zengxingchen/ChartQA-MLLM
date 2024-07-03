
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
average_daylight = [7.8, 9, 11, 13, 14.8, 15.5, 15, 13.8, 12, 10.5, 8.6, 7.7]

# Colors for each point
colors = [
    '#FF7373', '#FFA07A', '#FFD700', '#98FB98', '#00FF7F',
    '#90EE90', '#3CB371', '#20B2AA', '#1E90FF', '#7B68EE', '#DDA0DD', '#FFB6C1'
]

# Change width and height of the chart
plt.figure(figsize=(10, 6))

# Scatter plot
plt.scatter(months, average_daylight, c=colors)

# Title and labels
plt.title('Average Hours of Daylight by Month')
plt.xlabel('Month')
plt.ylabel('Average Hours of Daylight')

# Adjust x-axis to show each month
plt.xticks(months)

# Show plot
plt.show()