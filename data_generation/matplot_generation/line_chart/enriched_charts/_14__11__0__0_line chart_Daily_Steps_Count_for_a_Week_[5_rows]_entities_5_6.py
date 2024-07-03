import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
books_sold = [500, 700, 1200, 900, 1500, 1100, 1300, 800, 600, 400, 300, 200]

plt.figure(figsize=(14, 7))

plt.plot(months, books_sold, color='#1E90FF', linewidth=2)

plt.annotate('Sales Spike', xy=('May', 1500), xytext=('March', 1200),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

plt.title('Monthly Book Sales in a Local Store', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Books Sold', fontsize=14)
plt.gca().invert_yaxis()

plt.show()