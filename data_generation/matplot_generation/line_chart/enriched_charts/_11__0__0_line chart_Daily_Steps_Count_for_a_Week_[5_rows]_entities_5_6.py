
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
visitor_count = [1500, 1800, 2500, 3200, 4500, 5800, 6200, 6000, 5200, 4000, 2800, 1700]

plt.figure(figsize=(16, 8))

plt.plot(months, visitor_count, color='#FF6347', linewidth=2)

plt.annotate('Peak Season', xy=('July', 6200), xytext=('May', 5000),
             arrowprops=dict(facecolor='#FFD700', shrink=0.05))

plt.title('Monthly Visitor Count to a National Park', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Visitor Count', fontsize=14)

plt.show()