
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
pollution_levels = [95, 90, 85, 80, 75, 70, 65, 60, 55, 60, 65, 70]

plt.figure(figsize=(16, 10))

plt.plot(months, pollution_levels, color='#1ABC9C', linewidth=2)

plt.annotate('Highest Pollution', xy=('January', 95), xytext=('February', 90),
             arrowprops=dict(facecolor='#E74C3C', shrink=0.05))

plt.gca().invert_yaxis()

plt.title('Monthly Air Pollution Levels in Urban Areas', pad=20)
plt.xlabel('Month')
plt.ylabel('Air Quality Index (AQI)')

plt.show()