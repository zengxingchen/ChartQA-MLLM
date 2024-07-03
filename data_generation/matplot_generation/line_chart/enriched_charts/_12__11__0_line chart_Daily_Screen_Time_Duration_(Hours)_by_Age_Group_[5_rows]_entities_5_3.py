
import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
revenue = [3000, 3200, 2800, 3500, 3700, 3400, 3600, 3800, 3900, 4100, 4300, 4500]

plt.figure(figsize=(14, 7))
plt.plot(months, revenue, marker='s', color='#FF6347', label='Monthly Revenue')  

plt.annotate('Highest', xy=('December', 4500), xytext=('November', 4200),
             arrowprops=dict(facecolor='#4682B4', shrink=0.05))

plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Monthly Revenue for Online Store - 2023', pad=20)
plt.legend(loc='lower right')
plt.grid(True)

plt.show()