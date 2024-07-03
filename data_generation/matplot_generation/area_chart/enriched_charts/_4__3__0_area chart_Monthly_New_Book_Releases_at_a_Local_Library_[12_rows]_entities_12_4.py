
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
attendance = [500, 550, 620, 720, 800, 900, 950, 940, 880, 700, 600, 550]

plt.figure(figsize=(14, 9))
plt.fill_between(months, attendance, color='#FF6347')

plt.title('Monthly Attendance at Art & Design Workshops', fontsize=18, pad=25)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Attendees', fontsize=14)

highest_attendance_idx = attendance.index(max(attendance))
plt.annotate('Peak Attendance', xy=(months[highest_attendance_idx], attendance[highest_attendance_idx]), 
             xytext=(months[highest_attendance_idx], attendance[highest_attendance_idx]+100),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

plt.xticks(rotation=45)
plt.yticks(range(0, max(attendance)+200, 100))
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()