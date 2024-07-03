
import matplotlib.pyplot as plt

# Data for the area chart
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [150, 180, 210, 250, 280, 320, 360, 340, 300, 260, 220, 200]

# Create the area chart
plt.figure(figsize=(12, 7))  # Modify the width and height of the chart
plt.fill_between(months, sales, color='#1E90FF')  # Use a specific color code

# Adding a title and labels
plt.title('Monthly Sales Figures for XYZ Corp.', fontsize=16)  # Change the headline and topic
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales (in thousands)', fontsize=14)

# Annotate the highest sales
highest_sales_idx = sales.index(max(sales))
plt.annotate('Peak Sales', xy=(months[highest_sales_idx], sales[highest_sales_idx]), 
             xytext=(months[highest_sales_idx], sales[highest_sales_idx]+20),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))  # Specific color code for annotation

# Customize ticks and grid
plt.xticks(rotation=45)
plt.yticks(range(0, max(sales)+50, 50))
plt.grid(True, linestyle='--', alpha=0.7)

# Display the chart
plt.tight_layout()
plt.show()