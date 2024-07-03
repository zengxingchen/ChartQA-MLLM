
import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 32)]
stock_a = [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180]
stock_b = [155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 130, 129, 128, 127, 126, 125]

# Creating plot
plt.figure(figsize=(12, 8))
plt.plot(days, stock_a, color='#1F77B4', label='Stock A')  # blue
plt.plot(days, stock_b, color='#FF7F0E', label='Stock B')  # orange

# Adding a title and labels to the axes
plt.title('Stock Prices in July')
plt.xlabel('Day of the Month')
plt.ylabel('Stock Price ($)')

# Add annotations for maximum and minimum prices of both stocks
plt.annotate('Stock A Highest', xy=(31, stock_a[-1]), xytext=(25, stock_a[-5]),
             arrowprops=dict(facecolor='#1F77B4', shrink=0.05))

plt.annotate('Stock B Lowest', xy=(31, stock_b[-1]), xytext=(25, stock_b[-5]),
             arrowprops=dict(facecolor='#FF7F0E', shrink=0.05))

# Show grid and legend
plt.grid(True)
plt.legend(loc='upper left')

# Show the plot
plt.show()