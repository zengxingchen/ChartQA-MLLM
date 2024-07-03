
import matplotlib.pyplot as plt

data = [
    {'Age Group': '0-5 years', 'Monday': 0.5, 'Tuesday': 0.7, 'Wednesday': 0.9, 'Thursday': 1.0, 'Friday': 1.2},
    {'Age Group': '6-12 years', 'Monday': 1.5, 'Tuesday': 1.6, 'Wednesday': 1.7, 'Thursday': 1.8, 'Friday': 1.9},
    {'Age Group': '13-18 years', 'Monday': 3.5, 'Tuesday': 3.7, 'Wednesday': 3.9, 'Thursday': 4.1, 'Friday': 4.3},
    {'Age Group': '19-35 years', 'Monday': 2.5, 'Tuesday': 2.7, 'Wednesday': 2.9, 'Thursday': 3.0, 'Friday': 3.2},
    {'Age Group': '36-50 years', 'Monday': 1.8, 'Tuesday': 1.9, 'Wednesday': 2.0, 'Thursday': 2.1, 'Friday': 2.3},
    {'Age Group': '51-65 years', 'Monday': 0.9, 'Tuesday': 1.0, 'Wednesday': 1.1, 'Thursday': 1.2, 'Friday': 1.3},
    {'Age Group': '65+ years', 'Monday': 0.4, 'Tuesday': 0.5, 'Wednesday': 0.6, 'Thursday': 0.7, 'Friday': 0.8}
]

days = list(data[0].keys())[1:]

plt.figure(figsize=(10, 6))

markers = ['o', 's', 'D', '^', 'v', '*', 'P']
linestyles = ['-', '--', '-.', ':', '-', '--', '-.']
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974', '#64b5cd', '#8c8c8c']

for age_data, marker, linestyle, color in zip(data, markers, linestyles, colors):
    age_group = age_data['Age Group']
    values = [age_data[day] for day in days]
    
    plt.plot(days, values, marker=marker, linestyle=linestyle, color=color, label=age_group)

plt.legend(title='Age Group', loc='upper right')

plt.title('Weekly Reading Hours by Age Group')
plt.xlabel('Day of the Week')
plt.ylabel('Reading Hours')

plt.grid(True)

plt.annotate('Peak Reading', xy=('Friday', 4.3), xytext=('Wednesday', 4.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()