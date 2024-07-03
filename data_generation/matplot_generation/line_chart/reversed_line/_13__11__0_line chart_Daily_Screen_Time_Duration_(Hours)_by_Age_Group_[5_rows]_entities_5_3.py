
import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
subscribers = [100, 150, 120, 170, 160, 180, 190, 200, 210, 220, 230, 240]

plt.figure(figsize=(14, 7))
plt.plot(months, subscribers, marker='o', color='#FF6347', label='Monthly Subscribers')  

plt.annotate('Peak', xy=('December', 240), xytext=('November', 230),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

plt.xlabel('Month')
plt.ylabel('Subscribers')
plt.title('Monthly Subscribers for Online Magazine - 2023')
plt.legend(loc='lower right')
plt.grid(True)
plt.gca().invert_yaxis()

plt.show()