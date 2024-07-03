
import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
revenue = [5000, 5200, 4900, 4700, 4600, 4800, 5300, 5500, 5100, 4950, 4800, 5700]

plt.figure(figsize=(12, 6))
plt.plot(months, revenue, marker='o', color='#4CAF50', label='Monthly Sales')  

plt.annotate('Highest', xy=('December', 5700), xytext=('November', 5400),
             arrowprops=dict(facecolor='#FF5722', shrink=0.05))

plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales for Online Store - 2023')
plt.legend(loc='upper left')
plt.grid(True)

plt.show()