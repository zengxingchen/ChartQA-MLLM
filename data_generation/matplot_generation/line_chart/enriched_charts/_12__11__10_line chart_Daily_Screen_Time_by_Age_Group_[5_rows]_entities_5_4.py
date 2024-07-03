
import matplotlib.pyplot as plt

data = [
    {'Age Group': '0-5 years', 'Monday': 1.2, 'Tuesday': 1.4, 'Wednesday': 1.1, 'Thursday': 1.3, 'Friday': 1.5},
    {'Age Group': '6-12 years', 'Monday': 2.5, 'Tuesday': 2.7, 'Wednesday': 2.9, 'Thursday': 3.0, 'Friday': 3.2},
    {'Age Group': '13-18 years', 'Monday': 4.1, 'Tuesday': 4.2, 'Wednesday': 4.4, 'Thursday': 4.6, 'Friday': 4.8},
    {'Age Group': '19-35 years', 'Monday': 3.0, 'Tuesday': 3.2, 'Wednesday': 3.4, 'Thursday': 3.5, 'Friday': 3.7},
    {'Age Group': '36-50 years', 'Monday': 2.1, 'Tuesday': 2.2, 'Wednesday': 2.3, 'Thursday': 2.4, 'Friday': 2.5},
    {'Age Group': '51-65 years', 'Monday': 1.4, 'Tuesday': 1.6, 'Wednesday': 1.7, 'Thursday': 1.8, 'Friday': 1.9},
    {'Age Group': '65+ years', 'Monday': 0.8, 'Tuesday': 0.9, 'Wednesday': 1.0, 'Thursday': 1.1, 'Friday': 1.2}
]

days = list(data[0].keys())[1:]

plt.figure(figsize=(12, 8))

markers = ['o', 's', 'D', '^', 'v', '*', 'P']
linestyles = ['-', '--', '-.', ':', '-', '--', '-.']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFF6', '#FF8C33']

for age_data, marker, linestyle, color in zip(data, markers, linestyles, colors):
    age_group = age_data['Age Group']
    values = [age_data[day] for day in days]
    
    plt.plot(days, values, marker=marker, linestyle=linestyle, color=color, label=age_group)

plt.legend(title='Age Group', loc='upper left')

plt.title('Weekly Exercise Hours by Age Group')
plt.xlabel('Day of the Week')
plt.ylabel('Exercise Hours')

plt.grid(True)

plt.annotate('Peak Exercise', xy=('Friday', 4.8), xytext=('Wednesday', 4.9),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()