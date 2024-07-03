
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
sightseeing = [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600]
adventure = [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100]
leisure = [2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600]

plt.figure(figsize=(14, 10))
plt.stackplot(months, sightseeing, adventure, leisure, 
              labels=['Sightseeing', 'Adventure', 'Leisure'],
              colors=['#4b8bbe', '#e74c3c', '#2ecc71'])

plt.title('Monthly Tourism Activities in 2023', fontsize=16, loc='right')
plt.xlabel('Month')
plt.ylabel('Number of Participants')
plt.legend(loc='upper left')
plt.xticks(rotation=45)

peak_leisure = max(leisure)
peak_month_leisure = months[leisure.index(peak_leisure)]
plt.annotate(f'Peak Leisure Activity\n{peak_leisure} Participants',
             xy=(peak_month_leisure, peak_leisure),
             xytext=(peak_month_leisure, peak_leisure + 500),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()