
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
exercise_hours = [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 5.8, 5.2, 4.5, 3.5, 3.2]

plt.figure(figsize=(14, 7))

plt.plot(months, exercise_hours, color='#1E90FF', linewidth=2)

plt.annotate('Highest Activity', xy=('July', 6.0), xytext=('May', 5.0),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05))

plt.title('Monthly Average Exercise Hours of a Person', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Exercise Hours', fontsize=14)

plt.show()