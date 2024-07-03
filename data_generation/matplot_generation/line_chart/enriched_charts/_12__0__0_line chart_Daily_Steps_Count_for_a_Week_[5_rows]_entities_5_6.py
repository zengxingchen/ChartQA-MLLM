
import matplotlib.pyplot as plt

days = list(range(1, 31))
attendance = [150, 160, 180, 170, 175, 190, 200, 210, 220, 230, 225, 215, 210, 200, 195, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275]

plt.figure(figsize=(16, 8))

plt.plot(days, attendance, color='#FF5733', linewidth=3)

plt.annotate('Peak Attendance', xy=(30, 275), xytext=(25, 260),
             arrowprops=dict(facecolor='#FFD700', shrink=0.05))

plt.title('Daily Attendance in January', pad=20)
plt.xlabel('Day')
plt.ylabel('Attendance')

plt.show()