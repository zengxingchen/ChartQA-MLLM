
import matplotlib.pyplot as plt
import pandas as pd

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
car_sales = [30000, 32000, 34000, 36000, 38000, 40000, 42000, 44000, 46000, 48000, 50000, 52000]
bike_sales = [20000, 22000, 23000, 25000, 27000, 28000, 30000, 32000, 33000, 35000, 37000, 38000]
truck_sales = [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000]

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(months, car_sales, bike_sales, truck_sales, colors=['#FF9999', '#66B3FF', '#99FF99'])

ax.set_title('Monthly Vehicle Sales (in Units)', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Number of Units Sold', fontsize=14)

for i in range(len(months)):
    ax.text(i, car_sales[i] + bike_sales[i] + truck_sales[i], f"{car_sales[i] + bike_sales[i] + truck_sales[i]:,}", ha='center', va='bottom')

plt.tight_layout()
plt.show()