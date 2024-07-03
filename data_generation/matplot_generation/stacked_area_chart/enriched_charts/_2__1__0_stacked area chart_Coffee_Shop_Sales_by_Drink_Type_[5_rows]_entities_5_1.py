
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [20000, 22000, 24000, 26000, 28000, 30000, 32000, 34000, 36000, 38000, 40000, 42000]
marketing = [10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000, 30000, 32000]
rnd = [8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500]
customer_service = [6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500]

plt.figure(figsize=(16, 10))
plt.stackplot(months, sales, marketing, rnd, customer_service, 
              colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

plt.title('Monthly Company Department Expenses', fontdict={'fontsize': 20}, loc='left')
plt.xlabel('Month')
plt.ylabel('Expenses ($)')
plt.legend(['Sales', 'Marketing', 'R&D', 'Customer Service'], loc='upper left')

peak_sales_month = months[sales.index(max(sales))]
peak_sales_value = max(sales)
plt.text(peak_sales_month, peak_sales_value, 'Peak Sales', ha='center', va='bottom')

plt.show()