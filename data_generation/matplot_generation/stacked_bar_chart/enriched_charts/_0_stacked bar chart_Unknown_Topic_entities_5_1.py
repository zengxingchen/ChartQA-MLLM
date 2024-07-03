
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
apples = [50, 60, 70, 75, 80, 90, 95, 100, 85, 78, 65, 55]
bananas = [85, 95, 68, 82, 73, 60, 90, 80, 70, 100, 80, 75]
oranges = [65, 80, 90, 95, 100, 85, 110, 120, 100, 90, 85, 80]
grapes = [30, 35, 38, 37, 40, 45, 50, 55, 60, 50, 45, 40]

# Stacked Bar Chart
plt.figure(figsize=(14, 8))  # Change width and height of the chart
bar_width = 0.5  # Change width of bars

# Creating a horizontal bar chart by using `barh` instead of `bar`
plt.barh(months, apples, color='#FF0000', edgecolor='white', height=bar_width, label='Apples')
plt.barh(months, bananas, left=apples, color='#FFFF00', edgecolor='white', height=bar_width, label='Bananas')
plt.barh(months, oranges, left=[i+j for i,j in zip(apples, bananas)], color='#FFA500', edgecolor='white', height=bar_width, label='Oranges')
plt.barh(months, grapes, left=[i+j+k for i,j,k in zip(apples, bananas, oranges)], color='#6F2DA8', edgecolor='white', height=bar_width, label='Grapes')

plt.xlabel('Production in Tons')  # Note the switch from ylabel to xlabel
plt.title('Monthly Fruit Production by Type')  # Change the headline
plt.yticks(months)  # Appropriately adjusting for horizontal chart
plt.legend(loc='lower right')

# Display the plot
plt.show()