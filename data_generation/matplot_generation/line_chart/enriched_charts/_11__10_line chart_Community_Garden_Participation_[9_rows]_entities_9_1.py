
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Stock Price ($)': 150},
    {'Month': 'February', 'Stock Price ($)': 155},
    {'Month': 'March', 'Stock Price ($)': 160},
    {'Month': 'April', 'Stock Price ($)': 145},
    {'Month': 'May', 'Stock Price ($)': 170},
    {'Month': 'June', 'Stock Price ($)': 180},
    {'Month': 'July', 'Stock Price ($)': 175},
    {'Month': 'August', 'Stock Price ($)': 185},
    {'Month': 'September', 'Stock Price ($)': 190},
    {'Month': 'October', 'Stock Price ($)': 200},
    {'Month': 'November', 'Stock Price ($)': 195},
    {'Month': 'December', 'Stock Price ($)': 210}
]

months = [entry['Month'] for entry in data]
prices = [entry['Stock Price ($)'] for entry in data]

plt.figure(figsize=(14, 8))

plt.plot(months, prices, color='#2ca02c', linestyle='--', linewidth=2, 
         marker='s', markersize=10, markerfacecolor='#e377c2', markeredgewidth=2, 
         markeredgecolor='#8c564b', label='Stock Price Over a Year')

plt.title('Monthly Stock Prices', fontsize=18, loc='center')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Stock Price ($)', fontsize=14)

plt.legend(loc='lower right')

plt.grid(True)

plt.xticks(fontsize=12, fontweight='bold', rotation=45)
plt.yticks(fontsize=12, fontweight='bold')

plt.annotate('Lowest Point', xy=('April', 145), xytext=('February', 140),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             fontsize=12, color='blue')

plt.show()