
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
sleep = [220, 210, 225, 230, 235, 240, 245, 250, 240, 230, 220, 210]
exercise = [15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30]
screen_time = [180, 175, 170, 160, 150, 140, 135, 130, 135, 140, 150, 160]
meditation = [10, 12, 15, 18, 20, 22, 25, 28, 25, 22, 20, 18]

plt.figure(figsize=(16, 10))
plt.stackplot(months, sleep, exercise, screen_time, meditation, 
              colors=['#4B0082', '#FF4500', '#2E8B57', '#FFD700'])

plt.title('Monthly Hours of Sleep, Exercise, and Screen Time', fontsize=20, pad=30)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Hours', fontsize=14)

peak_sleep_month = months[sleep.index(max(sleep))]
peak_sleep_value = max(sleep)
plt.text(peak_sleep_month, peak_sleep_value, 'Peak Sleep', ha='center', va='bottom', fontsize=12, color='black')

plt.legend(['Sleep', 'Exercise', 'Screen Time', 'Meditation'], loc='upper left', fontsize=12)
plt.show()