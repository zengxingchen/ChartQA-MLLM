
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
gold_prices = [1800, 1850, 1780, 1900, 1950, 2000, 2100, 2050, 1980, 1900, 1880, 1850]

plt.figure(figsize=(16, 10))  # Adjust width and height of the chart
plt.plot(months, gold_prices, marker='s', linestyle='--', color='#8e44ad')  # Specific hex color

# Annotation for the highest gold price
plt.annotate('Peak Price', xy=('July', 2100), xytext=('September', 2150),
             arrowprops=dict(facecolor='#e67e22', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Gold Prices (USD/oz)')
plt.title('Monthly Gold Prices in 2023')

# Invert the y-axis
plt.gca().invert_yaxis()

# Showing the plot
plt.show()