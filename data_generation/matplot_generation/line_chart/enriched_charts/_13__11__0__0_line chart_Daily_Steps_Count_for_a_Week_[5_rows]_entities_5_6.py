
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
visitor_count = [5000, 4800, 4500, 4200, 4000, 3500, 3000, 2800, 2600, 2200, 2000, 1800]

plt.figure(figsize=(14, 10))

plt.plot(months, visitor_count, color='#1E90FF', linewidth=3)

plt.annotate('Off-Peak Season', xy=('December', 1800), xytext=('October', 2500),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05))

plt.title('Monthly Visitor Count to an Art Gallery', fontsize=18)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Visitor Count', fontsize=15)

plt.show()