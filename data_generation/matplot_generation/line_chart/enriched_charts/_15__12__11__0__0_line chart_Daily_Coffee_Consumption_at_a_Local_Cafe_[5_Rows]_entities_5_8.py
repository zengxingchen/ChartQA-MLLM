
import matplotlib.pyplot as plt

days = [i for i in range(1, 32)]
price_stock_a = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600]
price_stock_b = [500, 495, 490, 485, 480, 475, 470, 465, 460, 455, 450, 445, 440, 435, 430, 425, 420, 415, 410, 405, 400, 395, 390, 385, 380, 375, 370, 365, 360, 355, 350]

plt.figure(figsize=(10, 6))
plt.plot(days, price_stock_a, color='#1E90FF', label='Stock A')  # DodgerBlue
plt.plot(days, price_stock_b, color='#32CD32', label='Stock B')  # LimeGreen

plt.title('Daily Stock Prices in January', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Stock Price')

plt.annotate('Stock A Peak', xy=(31, price_stock_a[-1]), xytext=(25, price_stock_a[-5]),
             arrowprops=dict(facecolor='#1E90FF', shrink=0.05))

plt.annotate('Stock B Low', xy=(31, price_stock_b[-1]), xytext=(25, price_stock_b[-5]),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05))

plt.gca().invert_yaxis()
plt.grid(True)
plt.legend(loc='upper left')
plt.show()