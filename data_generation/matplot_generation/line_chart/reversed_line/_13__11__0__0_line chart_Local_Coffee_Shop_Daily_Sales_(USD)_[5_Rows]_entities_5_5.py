
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [200, 180, 220, 260, 300, 350, 370, 330, 290, 240, 210, 190]

# Plotting the line chart
plt.figure(figsize=(18, 9))  # Change width and height of the chart
plt.plot(months, sales, marker='o', linestyle='-', color='#D62728', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Sales of Product X', fontsize=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales (Units)', fontsize=14)

# Adding an annotation for the highest sales
highest_sales_index = sales.index(max(sales))
highest_sales_month = months[highest_sales_index]
plt.annotate('Peak Sales', xy=(highest_sales_index, max(sales)), xytext=(highest_sales_index, max(sales) + 30),
             arrowprops=dict(facecolor='#1f77b4', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(400, 150)  # Inverted y-axis
plt.show()