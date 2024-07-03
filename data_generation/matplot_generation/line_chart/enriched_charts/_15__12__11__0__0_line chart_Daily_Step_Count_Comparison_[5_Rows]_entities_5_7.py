
import matplotlib.pyplot as plt

# Data
months = ['2022-Jan', '2022-Feb', '2022-Mar', '2022-Apr', '2022-May', '2022-Jun', '2022-Jul', '2022-Aug', '2022-Sep', '2022-Oct', '2022-Nov', '2022-Dec']
stock_prices = [300, 310, 295, 315, 325, 335, 345, 330, 340, 350, 355, 360]

# Plotting the line chart
plt.figure(figsize=(12, 6))
plt.plot(months, stock_prices, color='#FF5733', marker='o', linestyle='--', linewidth=2)

# Annotate a specific point with the label
plt.annotate('Year End Peak', xy=('2022-Dec', 360), xytext=('2022-Aug', 330),
             arrowprops=dict(facecolor='#8E44AD', arrowstyle='->'))

# Adding a title and labels
plt.title('Monthly Stock Prices of Company X in 2022', pad=20)
plt.xlabel('Month')
plt.ylabel('Stock Price ($)')
plt.gca().invert_yaxis()  # Invert y-axis

# Show the plot
plt.show()