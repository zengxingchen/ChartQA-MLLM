
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
hours_studied = [25, 28, 30, 33, 40, 35, 20, 18, 25, 30, 32, 25]

plt.figure(figsize=(16, 9))
plt.fill_between(months, hours_studied, color='#4682B4')

plt.title('Monthly Study Hours for Academic Performance', fontsize=20, pad=30)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Average Hours Studied', fontsize=15)

highest_hours_idx = hours_studied.index(max(hours_studied))
plt.annotate('Peak Study Time', xy=(months[highest_hours_idx], hours_studied[highest_hours_idx]), 
             xytext=(months[highest_hours_idx], hours_studied[highest_hours_idx]+5),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05))

plt.xticks(rotation=45)
plt.yticks(range(0, max(hours_studied)+10, 5))
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()