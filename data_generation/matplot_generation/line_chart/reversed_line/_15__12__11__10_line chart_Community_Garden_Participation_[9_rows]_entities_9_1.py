
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Average Study Time (hours)': 6},
    {'Month': 'February', 'Average Study Time (hours)': 5.5},
    {'Month': 'March', 'Average Study Time (hours)': 6.5},
    {'Month': 'April', 'Average Study Time (hours)': 5},
    {'Month': 'May', 'Average Study Time (hours)': 5.8},
    {'Month': 'June', 'Average Study Time (hours)': 4.5},
    {'Month': 'July', 'Average Study Time (hours)': 6},
    {'Month': 'August', 'Average Study Time (hours)': 5.2},
    {'Month': 'September', 'Average Study Time (hours)': 5.5},
    {'Month': 'October', 'Average Study Time (hours)': 4.8},
    {'Month': 'November', 'Average Study Time (hours)': 6.2},
    {'Month': 'December', 'Average Study Time (hours)': 4}
]

months = [entry['Month'] for entry in data]
study_times = [entry['Average Study Time (hours)'] for entry in data]

plt.figure(figsize=(12, 7))

plt.plot(months, study_times, color='#00A86B', linestyle='-', linewidth=2, 
         marker='o', markersize=8, markerfacecolor='#FF4500', markeredgewidth=2, 
         markeredgecolor='#4682B4', label='Average Study Time Over a Year')

plt.title('Monthly Average Study Time (hours)', fontsize=20, loc='center')
plt.xlabel('Month', fontsize=16)
plt.ylabel('Average Study Time (hours)', fontsize=16)
plt.gca().invert_yaxis()

plt.legend(loc='lower right')

plt.grid(True)

plt.xticks(fontsize=12, fontweight='bold', rotation=45)
plt.yticks(fontsize=12, fontweight='bold')

plt.annotate('Lowest Study Time', xy=('December', 4), xytext=('October', 4.5),
             arrowprops=dict(facecolor='blue', arrowstyle='->'),
             fontsize=12, color='red')

plt.show()