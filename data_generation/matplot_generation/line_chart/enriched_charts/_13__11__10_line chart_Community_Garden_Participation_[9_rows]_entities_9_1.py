
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Tourist Visits': 1800},
    {'Month': 'February', 'Tourist Visits': 1900},
    {'Month': 'March', 'Tourist Visits': 2100},
    {'Month': 'April', 'Tourist Visits': 2000},
    {'Month': 'May', 'Tourist Visits': 2300},
    {'Month': 'June', 'Tourist Visits': 2400},
    {'Month': 'July', 'Tourist Visits': 2500},
    {'Month': 'August', 'Tourist Visits': 2600},
    {'Month': 'September', 'Tourist Visits': 2700},
    {'Month': 'October', 'Tourist Visits': 2900},
    {'Month': 'November', 'Tourist Visits': 2800},
    {'Month': 'December', 'Tourist Visits': 3000}
]

months = [entry['Month'] for entry in data]
visits = [entry['Tourist Visits'] for entry in data]

plt.figure(figsize=(16, 9))

plt.plot(months, visits, color='#1f77b4', linestyle='-', linewidth=2, 
         marker='o', markersize=8, markerfacecolor='#ff7f0e', markeredgewidth=1, 
         markeredgecolor='#d62728', label='Monthly Tourist Visits')

plt.title('Monthly Tourist Visits Over a Year', fontsize=20, loc='center')
plt.xlabel('Month', fontsize=16)
plt.ylabel('Tourist Visits', fontsize=16)

plt.legend(loc='upper left')

plt.grid(True)

plt.xticks(fontsize=14, fontweight='bold', rotation=45)
plt.yticks(fontsize=14, fontweight='bold')

plt.annotate('Highest Point', xy=('December', 3000), xytext=('October', 3100),
             arrowprops=dict(facecolor='green', arrowstyle='->'),
             fontsize=12, color='purple')

plt.show()