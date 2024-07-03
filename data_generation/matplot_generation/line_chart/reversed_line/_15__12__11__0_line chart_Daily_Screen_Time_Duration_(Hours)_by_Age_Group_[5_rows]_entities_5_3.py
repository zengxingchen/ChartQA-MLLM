
import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
visitors = [5000, 4800, 5100, 4700, 4500, 4300, 4100, 3900, 3700, 3500, 3300, 3100]

plt.figure(figsize=(10, 5))
plt.plot(months, visitors, marker='o', color='#1E90FF', label='Monthly Visitors')  

plt.annotate('Highest', xy=('March', 5100), xytext=('February', 5300),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

plt.xlabel('Month')
plt.ylabel('Visitors')
plt.title('Monthly Visitors to the Museum - 2023', pad=20)
plt.legend(loc='upper right')
plt.grid(True)
plt.gca().invert_yaxis()

plt.show()