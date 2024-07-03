
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
hours_spent = [2.5, 3.2, 4.0, 4.8, 5.3, 6.1, 6.7, 6.5, 5.8, 5.1, 4.3, 3.6]

# Colors for each point
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF',
    '#33FFF2', '#F2FF33', '#FF33F5', '#33FF91', '#9133FF', '#FF9133', '#33A1FF'
]

# Change width and height of the chart
plt.figure(figsize=(16, 12))

# Scatter plot
plt.scatter(months, hours_spent, c=colors)

# Title and labels
plt.title('Monthly Hours Spent on Physical Exercise', pad=20)
plt.xlabel('Month')
plt.ylabel('Hours Spent')

# Adjust x-axis to show each month
plt.xticks(months)

# Show plot
plt.show()