
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
average_sleep_hours = [7.2, 6.8, 7.5, 7.7, 8.0, 8.5, 8.9, 8.3, 7.6, 7.0, 6.5, 6.2]

plt.figure(figsize=(10, 8))

plt.plot(months, average_sleep_hours, color='#FF4500', linewidth=2)

plt.annotate('Peak Sleep Hours', xy=('July', 8.9), xytext=('May', 8.0),
             arrowprops=dict(facecolor='#8A2BE2', shrink=0.05))

plt.title('Monthly Average Sleep Hours of a Person', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Sleep Hours', fontsize=14)
plt.gca().invert_yaxis()

plt.show()