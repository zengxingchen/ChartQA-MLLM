
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 
          'January2', 'February2', 'March2', 'April2', 'May2', 'June2', 'July2', 'August2', 'September2', 'October2', 'November2', 'December2']
temperature = [5, 6, 8, 12, 15, 18, 22, 21, 17, 13, 9, 5, 
               6, 7, 9, 13, 16, 19, 23, 22, 18, 14, 10, 6]

# Colors for each bar
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF', 
          '#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF', 
          '#1F77B4', '#FF7F0E', '#2CA02C', '#D62728']

# Create a vertical bar chart
plt.figure(figsize=(12, 8))
plt.bar(months, temperature, color=colors, width=0.6)

# Modify the ticks, labels, and title
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Variation for Two Years', pad=20)
plt.ylim(0, 25)

# Display the plot
plt.show()