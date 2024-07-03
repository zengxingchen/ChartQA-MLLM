
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
rainfall = [80, 70, 60, 50, 40, 30, 25, 25, 35, 50, 65, 75]
snowfall = [20, 18, 15, 10, 5, 2, 1, 1, 3, 7, 12, 18]
thunderstorms = [5, 4, 8, 12, 15, 20, 22, 22, 18, 14, 8, 6]
sunny_days = [10, 12, 15, 18, 20, 25, 28, 28, 22, 18, 15, 12]

plt.figure(figsize=(16, 8))
plt.stackplot(months, rainfall, snowfall, thunderstorms, sunny_days, 
              colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

plt.title('Monthly Weather Patterns', fontdict={'fontsize': 20}, pad=30)
plt.xlabel('Month')
plt.ylabel('Days/Amount')

peak_thunderstorms_month = months[thunderstorms.index(max(thunderstorms))]
peak_thunderstorms_value = max(thunderstorms)
plt.text(peak_thunderstorms_month, peak_thunderstorms_value, 'Peak for Thunderstorms', ha='center', va='bottom', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

plt.show()