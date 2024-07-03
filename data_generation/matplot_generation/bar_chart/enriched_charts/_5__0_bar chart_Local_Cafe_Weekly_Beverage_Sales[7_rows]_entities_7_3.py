
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
fruit_sales = [18000, 19500, 20000, 21000, 22500, 24000, 26000, 23000, 24500, 25500, 22000, 25000]

# Colors for each bar
colors = ['#FF5733', '#FFBD33', '#75FF33', '#33FF57', '#33FFBD', 
          '#33A1FF', '#3375FF', '#5733FF', '#BD33FF', '#FF33BD', 
          '#FF3375', '#FF3333']

# Creating vertical bar chart
plt.figure(figsize=(10, 12))  # changing the width and height of the chart
plt.bar(months, fruit_sales, color=colors, edgecolor='black', width=0.4)  # changed direction, color, and band width

# Customizing the chart
plt.xlabel('Month', fontsize=12)
plt.ylabel('Fruit Sales in USD', fontsize=12)
plt.title('Monthly Sales of Different Fruits in 2023', fontsize=16)
plt.ylim(15000, 27000)  # Set the y-axis limits

# Display the chart
plt.tight_layout()
plt.show()