
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', 
             '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', 
             '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', 
             '24:00'],
    'Heart_Rate': [60, 62, 65, 67, 64, 63, 68, 70, 72, 74, 76, 78, 80, 82, 85, 87, 89, 
                   91, 93, 95, 97, 99, 100, 98, 96]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 9))
plt.fill_between(df['Time'], df['Heart_Rate'], color='#ff7f0e', alpha=0.6)

plt.title('Heart Rate Over 24 Hours', fontsize=18, loc='left')
plt.xlabel('Time', fontsize=14)
plt.ylabel('Heart Rate (BPM)', fontsize=14)

plt.annotate('Maximum Heart Rate', xy=('22:00', 100), xytext=('18:00', 105),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='black')

plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()