
import matplotlib.pyplot as plt

days = [i for i in range(1, 32)]
stock_company_a = [150, 152, 148, 151, 153, 149, 155, 157, 159, 161, 158, 160, 163, 165, 168, 170, 173, 175, 178, 180, 183, 185, 188, 190, 192, 195, 197, 200, 202, 205, 207]
stock_company_b = [200, 198, 202, 195, 193, 190, 188, 185, 182, 179, 177, 175, 173, 171, 169, 166, 163, 161, 159, 156, 153, 151, 148, 146, 143, 141, 138, 135, 132, 130, 128]

plt.figure(figsize=(16, 10))
plt.plot(days, stock_company_a, color='#FF5733', label='Company A')  # Orange-Red
plt.plot(days, stock_company_b, color='#33C1FF', label='Company B')  # Light Blue

plt.title('Daily Stock Prices in January')
plt.xlabel('Day of the Month')
plt.ylabel('Stock Price ($)')
plt.gca().invert_yaxis()

plt.annotate('Company A Peak', xy=(31, stock_company_a[-1]), xytext=(25, stock_company_a[-5]),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05))

plt.annotate('Company B Low', xy=(31, stock_company_b[-1]), xytext=(25, stock_company_b[-5]),
             arrowprops=dict(facecolor='#33C1FF', shrink=0.05))

plt.grid(True)
plt.legend()
plt.show()