
import matplotlib.pyplot as plt

data = [
    {'Age Group': '0-5 years', 'Monday': 0.5, 'Tuesday': 0.7, 'Wednesday': 0.9, 'Thursday': 1.0, 'Friday': 1.2},
    {'Age Group': '6-12 years', 'Monday': 1.6, 'Tuesday': 1.7, 'Wednesday': 1.8, 'Thursday': 1.9, 'Friday': 2.0},
    {'Age Group': '13-18 years', 'Monday': 3.8, 'Tuesday': 4.0, 'Wednesday': 4.2, 'Thursday': 4.3, 'Friday': 4.5},
    {'Age Group': '19-35 years', 'Monday': 2.6, 'Tuesday': 2.8, 'Wednesday': 3.0, 'Thursday': 3.1, 'Friday': 3.3},
    {'Age Group': '36-50 years', 'Monday': 1.9, 'Tuesday': 2.0, 'Wednesday': 2.2, 'Thursday': 2.3, 'Friday': 2.5},
    {'Age Group': '51-65 years', 'Monday': 1.0, 'Tuesday': 1.1, 'Wednesday': 1.2, 'Thursday': 1.3, 'Friday': 1.4},
    {'Age Group': '65+ years', 'Monday': 0.6, 'Tuesday': 0.7, 'Wednesday': 0.8, 'Thursday': 0.9, 'Friday': 1.0}
]

days = list(data[0].keys())[1:]

plt.figure(figsize=(12, 8))

markers = ['o', 's', 'D', '^', 'v', '*', 'P']
linestyles = ['-', '--', '-.', ':', '-', '--', '-.']
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF1493', '#A52A2A']

for age_data, marker, linestyle, color in zip(data, markers, linestyles, colors):
    age_group = age_data['Age Group']
    values = [age_data[day] for day in days]
    
    plt.plot(days, values, marker=marker, linestyle=linestyle, color=color, label=age_group)

plt.legend(title='Age Group', loc='lower right')

plt.title('Weekly Exercise Hours by Age Group')
plt.xlabel('Day of the Week')
plt.ylabel('Exercise Hours')

plt.grid(True)

plt.annotate('Peak Exercise', xy=('Friday', 4.5), xytext=('Wednesday', 4.7),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()