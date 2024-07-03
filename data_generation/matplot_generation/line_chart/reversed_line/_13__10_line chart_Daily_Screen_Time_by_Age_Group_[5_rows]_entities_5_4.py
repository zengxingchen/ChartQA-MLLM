
import matplotlib.pyplot as plt

data = [
    {'Age Group': '0-5 years', 'Monday': 0.5, 'Tuesday': 0.7, 'Wednesday': 0.6, 'Thursday': 0.8, 'Friday': 0.9},
    {'Age Group': '6-12 years', 'Monday': 1.0, 'Tuesday': 1.2, 'Wednesday': 1.3, 'Thursday': 1.1, 'Friday': 1.4},
    {'Age Group': '13-18 years', 'Monday': 1.5, 'Tuesday': 1.6, 'Wednesday': 1.7, 'Thursday': 1.8, 'Friday': 1.9},
    {'Age Group': '19-35 years', 'Monday': 2.0, 'Tuesday': 2.1, 'Wednesday': 2.2, 'Thursday': 2.3, 'Friday': 2.4},
    {'Age Group': '36-50 years', 'Monday': 2.5, 'Tuesday': 2.4, 'Wednesday': 2.3, 'Thursday': 2.6, 'Friday': 2.7},
    {'Age Group': '51-65 years', 'Monday': 3.0, 'Tuesday': 3.1, 'Wednesday': 3.2, 'Thursday': 3.0, 'Friday': 3.3},
    {'Age Group': '65+ years', 'Monday': 3.5, 'Tuesday': 3.4, 'Wednesday': 3.3, 'Thursday': 3.2, 'Friday': 3.1}
]

days = list(data[0].keys())[1:]

plt.figure(figsize=(14, 10))

markers = ['o', 's', 'D', '^', 'v', '*', 'P']
linestyles = ['-', '--', '-.', ':', '-', '--', '-.']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF', '#33FFF6', '#FFC133']

for age_data, marker, linestyle, color in zip(data, markers, linestyles, colors):
    age_group = age_data['Age Group']
    values = [age_data[day] for day in days]
    
    plt.plot(days, values, marker=marker, linestyle=linestyle, color=color, label=age_group)

plt.legend(title='Age Group', loc='upper right')

plt.title('Weekly Running Distance Across Different Age Groups', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Running Distance (Miles)')
plt.gca().invert_yaxis()

plt.grid(True)

plt.annotate('Highest Distance', xy=('Friday', 3.3), xytext=('Wednesday', 3.6),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()