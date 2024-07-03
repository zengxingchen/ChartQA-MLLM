
import matplotlib.pyplot as plt

days = [i for i in range(1, 32)]
stock_company_a = [100, 102, 104, 103, 105, 108, 110, 115, 120, 125, 123, 127, 130, 128, 133, 135, 137, 140, 142, 145, 147, 149, 151, 152, 154, 156, 158, 160, 162, 165, 167]
stock_company_b = [200, 198, 196, 195, 193, 192, 190, 188, 185, 182, 180, 178, 175, 173, 170, 168, 165, 163, 160, 158, 155, 153, 150, 148, 145, 143, 140, 138, 135, 133, 130]

plt.figure(figsize=(12, 6))
plt.plot(days, stock_company_a, color='#FF4500', label='Company A')  # OrangeRed
plt.plot(days, stock_company_b, color='#1E90FF', label='Company B')  # DodgerBlue

plt.title('Monthly Stock Prices in January', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Stock Price')

plt.annotate('Company A Peak', xy=(31, stock_company_a[-1]), xytext=(25, stock_company_a[-5]),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

plt.annotate('Company B Low', xy=(31, stock_company_b[-1]), xytext=(25, stock_company_b[-5]),
             arrowprops=dict(facecolor='#1E90FF', shrink=0.05))

plt.grid(True)
plt.legend(loc='upper right')
plt.show()