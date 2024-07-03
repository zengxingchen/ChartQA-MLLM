
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
electric_cars_sales = [2000, 2100, 2500, 3000, 3200, 3500, 3700, 4000, 4200, 4500, 4700, 5000]
hybrid_cars_sales = [3500, 3600, 3700, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600]
gasoline_cars_sales = [8000, 8200, 8500, 8800, 9000, 9300, 9500, 9700, 9900, 10000, 10200, 10400]

plt.figure(figsize=(16, 12))
plt.stackplot(months, electric_cars_sales, hybrid_cars_sales, gasoline_cars_sales, 
              labels=['Electric Cars', 'Hybrid Cars', 'Gasoline Cars'],
              colors=['#1E90FF', '#FFD700', '#FF4500'])

plt.title('Monthly Sales Data for Different Types of Cars', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales (Units)', fontsize=14)
plt.legend(loc='upper left')
plt.xticks(rotation=45)

peak_electric_sales = max(electric_cars_sales)
peak_month_electric = months[electric_cars_sales.index(peak_electric_sales)]
plt.annotate(f'Peak Electric Car Sales\n{peak_electric_sales} Units',
             xy=(peak_month_electric, peak_electric_sales),
             xytext=(peak_month_electric, peak_electric_sales + 1000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

peak_hybrid_sales = max(hybrid_cars_sales)
peak_month_hybrid = months[hybrid_cars_sales.index(peak_hybrid_sales)]
plt.annotate(f'Peak Hybrid Car Sales\n{peak_hybrid_sales} Units',
             xy=(peak_month_hybrid, peak_hybrid_sales),
             xytext=(peak_month_hybrid, peak_hybrid_sales + 1000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()