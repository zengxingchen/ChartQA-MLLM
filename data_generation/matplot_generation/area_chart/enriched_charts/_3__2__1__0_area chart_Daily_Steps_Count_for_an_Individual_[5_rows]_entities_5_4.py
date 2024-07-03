
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', 
             '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', 
             '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', 
             '24:00'],
    'Viewership': [50, 45, 40, 35, 30, 25, 28, 35, 45, 55, 60, 65, 70, 75, 80, 85, 90, 
                   95, 100, 105, 110, 120, 115, 110, 105]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
plt.fill_between(df['Time'], df['Viewership'], color='#1f77b4', alpha=0.6)

plt.title('Viewership Over a Day', fontsize=20, loc='center')
plt.xlabel('Time', fontsize=14)
plt.ylabel('Viewership (in thousands)', fontsize=14)

plt.annotate('Peak Viewership', xy=('21:00', 120), xytext=('17:00', 125),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='black')

plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()