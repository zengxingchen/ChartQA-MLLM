
import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
revenue = [6500, 6200, 6300, 6100, 6000, 5900, 5700, 5800, 5600, 5400, 5300, 5200]

plt.figure(figsize=(10, 5))
plt.plot(months, revenue, marker='o', color='#1E88E5', label='Monthly Revenue')

plt.annotate('Peak', xy=('January', 6500), xytext=('February', 6300),
             arrowprops=dict(facecolor='#D32F2F', shrink=0.05))

plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Monthly Revenue for Art & Design Studio - 2023', loc='center')
plt.legend(loc='upper right')
plt.grid(True)
plt.gca().invert_yaxis()

plt.show()