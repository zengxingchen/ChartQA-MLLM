
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
visitor_counts = [300, 280, 310, 290, 320, 330, 340, 350, 360, 370, 365, 355]

plt.figure(figsize=(12, 7))

plt.plot(months, visitor_counts, color='#2ECC71', linewidth=2)
plt.gca().invert_yaxis()

plt.annotate('Peak Visitors', xy=('October', 370), xytext=('September', 380),
             arrowprops=dict(facecolor='#E74C3C', shrink=0.05))

plt.title('Monthly Visitor Count at the Museum')
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

plt.show()