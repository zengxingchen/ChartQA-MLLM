
import matplotlib.pyplot as plt

data = [
    {'Age Group': '0-5 years', 'Monday': 1.0, 'Tuesday': 0.9, 'Wednesday': 1.1, 'Thursday': 1.0, 'Friday': 0.8},
    {'Age Group': '6-12 years', 'Monday': 2.0, 'Tuesday': 1.9, 'Wednesday': 2.2, 'Thursday': 2.1, 'Friday': 2.3},
    {'Age Group': '13-18 years', 'Monday': 3.0, 'Tuesday': 3.2, 'Wednesday': 3.1, 'Thursday': 3.4, 'Friday': 3.3},
    {'Age Group': '19-35 years', 'Monday': 3.5, 'Tuesday': 3.4, 'Wednesday': 3.6, 'Thursday': 3.5, 'Friday': 3.7},
    {'Age Group': '36-50 years', 'Monday': 4.0, 'Tuesday': 4.2, 'Wednesday': 4.1, 'Thursday': 4.3, 'Friday': 4.4},
    {'Age Group': '51-65 years', 'Monday': 4.5, 'Tuesday': 4.4, 'Wednesday': 4.6, 'Thursday': 4.7, 'Friday': 4.8},
    {'Age Group': '65+ years', 'Monday': 5.0, 'Tuesday': 5.1, 'Wednesday': 5.2, 'Thursday': 5.3, 'Friday': 5.4}
]

days = list(data[0].keys())[1:]

plt.figure(figsize=(14, 10))

markers = ['o', 's', 'D', '^', 'v', '*', 'P']
linestyles = ['-', '--', '-.', ':', '-', '--', '-.']
colors = ['#00429d', '#73a2c6', '#d2e5f0', '#f6c141', '#e36a18', '#be2829', '#67001f']

for age_data, marker, linestyle, color in zip(data, markers, linestyles, colors):
    age_group = age_data['Age Group']
    values = [age_data[day] for day in days]
    
    plt.plot(days, values, marker=marker, linestyle=linestyle, color=color, label=age_group)

plt.legend(title='Age Group', loc='upper left')

plt.title('Mental Stimulation Levels Across Different Age Groups', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Stimulation Level (Hours)')
plt.grid(True)

plt.annotate('Peak Stimulation', xy=('Friday', 5.4), xytext=('Wednesday', 5.7),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.gca().invert_yaxis()
plt.show()