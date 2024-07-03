
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Value': 50, 'Location': 'Mountain View'},
    {'Month': 'February', 'Value': 47, 'Location': 'Mountain View'},
    {'Month': 'March', 'Value': 44, 'Location': 'Mountain View'},
    {'Month': 'April', 'Value': 42, 'Location': 'Mountain View'},
    {'Month': 'May', 'Value': 40, 'Location': 'Mountain View'},
    {'Month': 'June', 'Value': 35, 'Location': 'Mountain View'},
    {'Month': 'July', 'Value': 30, 'Location': 'Mountain View'},
    {'Month': 'August', 'Value': 33, 'Location': 'Mountain View'},
    {'Month': 'September', 'Value': 36, 'Location': 'Mountain View'},
    {'Month': 'October', 'Value': 40, 'Location': 'Mountain View'},
    {'Month': 'November', 'Value': 45, 'Location': 'Mountain View'},
    {'Month': 'December', 'Value': 48, 'Location': 'Mountain View'}
]

months = [entry['Month'] for entry in data]
values = [entry['Value'] for entry in data]

plt.figure(figsize=(14, 8))

plt.plot(months, values, color='#ff5733', linestyle='-', linewidth=2,
         marker='o', markersize=8, markerfacecolor='#33ff57', markeredgewidth=2,
         markeredgecolor='#3357ff', label='Monthly Values at Mountain View')

plt.title('Monthly Value Trends at Mountain View', fontsize=16, loc='center')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Value', fontsize=12)

plt.legend(loc='lower right')

plt.grid(True)

plt.xticks(fontsize=10, fontweight='bold', rotation=45)
plt.yticks(fontsize=10, fontweight='bold')

plt.annotate('Lowest Point', xy=('July', 30), xytext=('May', 35),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='blue')

plt.gca().invert_yaxis()

plt.show()