
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
groceries = [500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720]
restaurants = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520]
snacks = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]

plt.figure(figsize=(16, 10))
plt.stackplot(months, groceries, restaurants, snacks, 
              labels=['Groceries', 'Restaurants', 'Snacks'],
              colors=['#FF6347', '#4682B4', '#32CD32'])

plt.title('Monthly Food Expenditure', y=1.02)
plt.xlabel('Month')
plt.ylabel('Expenditure (USD)')
plt.legend(loc='upper left')
plt.xticks(rotation=45)

peak_groceries_expenditure = max(groceries)
peak_month = months[groceries.index(peak_groceries_expenditure)]
plt.annotate(f'Peak Groceries Expenditure\n{peak_groceries_expenditure} USD',
             xy=(peak_month, peak_groceries_expenditure),
             xytext=(peak_month, peak_groceries_expenditure + 100),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()