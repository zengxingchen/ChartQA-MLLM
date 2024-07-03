
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
visitors = [450, 520, 610, 710, 860, 950, 1100, 1080, 900, 750, 620, 480]

plt.figure(figsize=(12, 8))
plt.fill_between(months, visitors, color='#4682B4')

plt.title('Monthly Visitors to Adventure Park', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Visitors', fontsize=12)

highest_visitor_idx = visitors.index(max(visitors))
plt.annotate('Peak Season', xy=(months[highest_visitor_idx], visitors[highest_visitor_idx]), 
             xytext=(months[highest_visitor_idx], visitors[highest_visitor_idx]+100),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

plt.xticks(rotation=45)
plt.yticks(range(0, max(visitors)+200, 200))
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()