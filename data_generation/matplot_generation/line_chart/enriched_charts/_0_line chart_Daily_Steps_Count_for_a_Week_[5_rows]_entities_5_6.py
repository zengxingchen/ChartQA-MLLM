
import matplotlib.pyplot as plt

# Given the data above
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [200, 220, 210, 250, 270, 260, 300, 320, 310, 330, 340, 360]

plt.figure(figsize=(12, 6))  # Change width (12) and height (6)

# Plot the line chart with a new color scheme and trend
plt.plot(months, sales, color='#FF5733', linewidth=2)

# Annotate the peak sales value in September
plt.annotate('Peak Sales', xy=('September', 310), xytext=('October', 330),
             arrowprops=dict(facecolor='#FFC300', shrink=0.05))

plt.title('Monthly Sales Trends')  # Set a relevant title
plt.xlabel('Month')  # Label the x-axis
plt.ylabel('Sales (in USD)')  # Label the y-axis

# Display the chart
plt.show()