
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 
          'January2', 'February2', 'March2', 'April2', 'May2', 'June2', 'July2', 'August2', 'September2', 'October2', 'November2', 'December2']
revenue = [15000, 18000, 17000, 22000, 21000, 25000, 24000, 26000, 23000, 20000, 21000, 22000, 
           16000, 19000, 18000, 23000, 22000, 26000, 25000, 27000, 24000, 21000, 22000, 23000]

# Colors for each bar
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC', '#EFC050', '#5B5EA6',
          '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC', '#EFC050', '#5B5EA6']

# Create a horizontal bar chart
plt.figure(figsize=(14, 10))
plt.barh(months, revenue, color=colors, height=0.4)

# Modify the ticks, labels, and title
plt.xlabel('Revenue ($)')
plt.title('Monthly Revenue for Two Years', pad=20)
plt.xlim(10000, 30000)

# Display the plot
plt.show()