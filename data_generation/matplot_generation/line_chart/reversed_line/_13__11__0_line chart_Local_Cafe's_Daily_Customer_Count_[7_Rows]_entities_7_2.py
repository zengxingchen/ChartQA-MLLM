
import matplotlib.pyplot as plt
import pandas as pd

# Data points
dates = pd.date_range(start="2024-01-01", end="2024-01-31")
product_sales = [120, 150, 180, 170, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450]

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(dates, product_sales, marker='o', linestyle='-', color='#4682B4')

# Annotate the highest and lowest product sales points
plt.annotate('Highest\n450 units', xy=(dates[-1], 450), xytext=(dates[-5], 430),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')
plt.annotate('Lowest\n120 units', xy=(dates[0], 120), xytext=(dates[5], 140),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')

# Title and labels
plt.title('Daily Product Sales Trend in January 2024', pad=20)
plt.xlabel('Date')
plt.ylabel('Product Sales (units)')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Invert y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()