
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
temperature = [5, 7, 10, 15, 20, 25, 30, 28, 22, 17, 10, 6]

plt.figure(figsize=(14, 7))

plt.plot(months, temperature, color='#1E90FF', linewidth=2)

plt.annotate('Highest Temp', xy=('July', 30), xytext=('June', 28),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05))

plt.title('Average Monthly Temperatures')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')

plt.show()