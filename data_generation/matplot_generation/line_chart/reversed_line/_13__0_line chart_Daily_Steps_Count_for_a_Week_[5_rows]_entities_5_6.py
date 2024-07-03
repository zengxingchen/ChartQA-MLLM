
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
attendance = [500, 480, 460, 470, 450, 440, 430, 420, 410, 400, 390, 380]

plt.figure(figsize=(10, 5))

plt.plot(months, attendance, color='#1f77b4', linewidth=2)

plt.gca().invert_yaxis()

plt.annotate('Lowest Attendance', xy=('December', 380), xytext=('November', 400),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

plt.title('Monthly Gym Attendance Trends', pad=20)
plt.xlabel('Month')
plt.ylabel('Attendance')

plt.show()