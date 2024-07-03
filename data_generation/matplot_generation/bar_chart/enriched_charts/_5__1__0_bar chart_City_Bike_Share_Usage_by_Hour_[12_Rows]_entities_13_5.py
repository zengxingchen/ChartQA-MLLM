
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [450, 470, 510, 590, 650, 700, 720, 750, 680, 620, 570, 500]

# Colors for each bar
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#20B2AA', '#FF69B4', '#8A2BE2', '#FF4500', '#DA70D6', '#32CD32', '#4682B4', '#6A5ACD', '#7FFF00']

# Plotting the bar chart horizontally
plt.figure(figsize=(12, 8))  # Change width and height of the chart
plt.barh(months, sales, color=colors, edgecolor='black', height=0.5)  # Change height for bars and apply color scheme

# Chart title and labels
plt.title('Monthly Sales Performance', fontsize=18)
plt.xlabel('Sales (Units)', fontsize=14)

# Setting the ylim to provide better clarity for sales values
plt.xlim(min(sales) - 50, max(sales) + 50)

# Display the chart
plt.tight_layout()
plt.show()