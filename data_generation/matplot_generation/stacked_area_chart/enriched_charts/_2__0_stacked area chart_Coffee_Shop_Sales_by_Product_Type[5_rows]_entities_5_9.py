
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
fruit_sales = [11000, 15000, 17000, 19000, 21000, 23000, 25000, 27000, 29000, 31000, 33000, 35000]
vegetable_sales = [14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000, 30000, 32000, 34000, 36000]
dairy_sales = [8000, 8500, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000]

plt.figure(figsize=(14, 10))
plt.stackplot(months, fruit_sales, vegetable_sales, dairy_sales, 
              labels=['Fruit', 'Vegetable', 'Dairy'],
              colors=['#FF6347', '#32CD32', '#4682B4'])

plt.title('Monthly Sales Data for Food Products', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales (USD)', fontsize=14)
plt.legend(loc='upper left')
plt.xticks(rotation=45)

peak_fruit_sales = max(fruit_sales)
peak_month_fruit = months[fruit_sales.index(peak_fruit_sales)]
plt.annotate(f'Peak Fruit Sales\n{peak_fruit_sales} USD',
             xy=(peak_month_fruit, peak_fruit_sales),
             xytext=(peak_month_fruit, peak_fruit_sales + 5000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

peak_vegetable_sales = max(vegetable_sales)
peak_month_vegetable = months[vegetable_sales.index(peak_vegetable_sales)]
plt.annotate(f'Peak Vegetable Sales\n{peak_vegetable_sales} USD',
             xy=(peak_month_vegetable, peak_vegetable_sales),
             xytext=(peak_month_vegetable, peak_vegetable_sales + 5000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()