
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
food_sales = [5000, 5500, 6000, 5800, 6100, 6300, 6500, 6700, 6900, 7100, 7300, 7500]
clothing_sales = [7000, 6800, 7200, 7100, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000]
electronics_sales = [3000, 3200, 3400, 3300, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200]

plt.figure(figsize=(14, 9))
plt.stackplot(months, food_sales, clothing_sales, electronics_sales, 
              labels=['Food', 'Clothing', 'Electronics'],
              colors=['#ff9999', '#66b3ff', '#99ff99'])

plt.title('Monthly Expenditure Data for Household', y=1.05)
plt.xlabel('Month')
plt.ylabel('Expenditure (USD)')
plt.legend(loc='upper right')
plt.xticks(rotation=45)

peak_clothing_sales = max(clothing_sales)
peak_month = months[clothing_sales.index(peak_clothing_sales)]
plt.annotate(f'Peak Clothing Expenditure\n{peak_clothing_sales} USD',
             xy=(peak_month, peak_clothing_sales),
             xytext=(peak_month, peak_clothing_sales + 1000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()