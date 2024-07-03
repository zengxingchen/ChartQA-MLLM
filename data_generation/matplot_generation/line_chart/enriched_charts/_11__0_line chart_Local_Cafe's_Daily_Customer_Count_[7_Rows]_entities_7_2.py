
import matplotlib.pyplot as plt
import pandas as pd

# Data points
dates = pd.date_range(start="2024-01-01", end="2024-01-31")
product_sales = [120, 150, 90, 200, 160, 170, 180, 220, 230, 190, 250, 240, 260, 270, 280, 300, 310, 290, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(dates, product_sales, marker='o', linestyle='-', color='#FF6347')

# Annotate the highest and lowest product sales points
plt.annotate('Highest\n440 units', xy=(dates[-1], 440), xytext=(dates[-5], 420),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05), color='#32CD32')
plt.annotate('Lowest\n90 units', xy=(dates[2], 90), xytext=(dates[5], 120),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05), color='#32CD32')

# Title and labels
plt.title('Daily Product Sales in January 2024')
plt.xlabel('Date')
plt.ylabel('Product Sales (units)')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()