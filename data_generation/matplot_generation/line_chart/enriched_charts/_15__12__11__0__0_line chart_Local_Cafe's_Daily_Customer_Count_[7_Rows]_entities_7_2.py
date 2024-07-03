
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
investment_amounts = [5000, 4500, 4700, 5200, 5300, 4800, 5500, 5900, 5700, 6000, 6200, 6100]

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(months, investment_amounts, marker='o', linestyle='-', color='#1E90FF')

# Annotate the highest and lowest investment amount points
plt.annotate('Highest\n6200', xy=('November', 6200), xytext=('December', 6300),
             arrowprops=dict(facecolor='#FFD700', shrink=0.05), color='#FFD700')
plt.annotate('Lowest\n4500', xy=('February', 4500), xytext=('March', 4400),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')

# Title and labels
plt.title('Monthly Investment Amounts in 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Investment Amount (USD)')
plt.gca().invert_yaxis()

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.7)

# Show the plot
plt.show()