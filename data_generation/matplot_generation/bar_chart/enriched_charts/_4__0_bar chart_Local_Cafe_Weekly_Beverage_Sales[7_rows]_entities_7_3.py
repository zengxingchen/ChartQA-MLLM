
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [30000, 31000, 28500, 32300, 34000, 32500,
           31500, 33000, 32000, 33500, 32500, 34500]

# Colors for each bar
colors = ['#FF5733', '#FF8D1A', '#FFC300', '#DAF7A6', '#33FF57',
          '#33FF8D', '#1AFFC3', '#33FFDA', '#33A6FF', '#338DFF',
          '#5733FF', '#FF33A6']

# Creating vertical bar chart
plt.figure(figsize=(16, 9)) # changing the width and height of the chart
plt.bar(months, revenue, color=colors, edgecolor='black', width=0.5) # changed direction, color, and bar width

# Customizing the chart
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue in USD', fontsize=12)
plt.title('Monthly Revenue for ABC Food & Nutrition Corp in 2023', fontsize=16)
plt.ylim(27000, 36000) # Setting the y-axis limits to start from a specific value

# Display the chart
plt.tight_layout()
plt.show()