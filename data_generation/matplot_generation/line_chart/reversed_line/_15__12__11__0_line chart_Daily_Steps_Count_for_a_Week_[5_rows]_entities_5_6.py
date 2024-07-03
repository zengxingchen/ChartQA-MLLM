
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [1000, 1200, 1100, 1300, 1500, 1700, 1600, 1800, 2000, 2200, 2100, 2300]

plt.figure(figsize=(14, 8))

plt.plot(months, sales, color='#1f77b4', linewidth=3)

plt.annotate('Sales Dip', xy=('March', 1100), xytext=('April', 1300),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

plt.title('Monthly Sales Figures in 2023', fontsize=18, loc='center')  
plt.xlabel('Month', fontsize=14)  
plt.ylabel('Sales (in USD)', fontsize=14)  
plt.gca().invert_yaxis()

plt.show()