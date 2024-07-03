
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Average Heart Rate (bpm)': 75},
    {'Month': 'February', 'Average Heart Rate (bpm)': 78},
    {'Month': 'March', 'Average Heart Rate (bpm)': 76},
    {'Month': 'April', 'Average Heart Rate (bpm)': 80},
    {'Month': 'May', 'Average Heart Rate (bpm)': 77},
    {'Month': 'June', 'Average Heart Rate (bpm)': 79},
    {'Month': 'July', 'Average Heart Rate (bpm)': 82},
    {'Month': 'August', 'Average Heart Rate (bpm)': 85},
    {'Month': 'September', 'Average Heart Rate (bpm)': 83},
    {'Month': 'October', 'Average Heart Rate (bpm)': 86},
    {'Month': 'November', 'Average Heart Rate (bpm)': 84},
    {'Month': 'December', 'Average Heart Rate (bpm)': 88}
]

months = [entry['Month'] for entry in data]
heart_rates = [entry['Average Heart Rate (bpm)'] for entry in data]

plt.figure(figsize=(16, 9))

plt.plot(months, heart_rates, color='#1f77b4', linestyle='-', linewidth=2, 
         marker='o', markersize=8, markerfacecolor='#ff7f0e', markeredgewidth=2, 
         markeredgecolor='#2ca02c', label='Average Heart Rate Over a Year')

plt.title('Monthly Average Heart Rate (bpm)', fontsize=20, loc='center')
plt.xlabel('Month', fontsize=16)
plt.ylabel('Average Heart Rate (bpm)', fontsize=16)

plt.legend(loc='upper left')

plt.grid(True)

plt.xticks(fontsize=12, fontweight='bold', rotation=45)
plt.yticks(fontsize=12, fontweight='bold')

plt.annotate('Peak Heart Rate', xy=('December', 88), xytext=('October', 89),
             arrowprops=dict(facecolor='purple', arrowstyle='->'),
             fontsize=12, color='red')

plt.show()