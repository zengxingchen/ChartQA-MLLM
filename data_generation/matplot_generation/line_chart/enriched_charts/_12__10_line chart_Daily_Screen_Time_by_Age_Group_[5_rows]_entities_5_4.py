
import matplotlib.pyplot as plt

data = [
    {'Age Group': '0-5 years', 'Monday': 1.0, 'Tuesday': 0.8, 'Wednesday': 1.2, 'Thursday': 1.0, 'Friday': 1.1, 'Saturday': 1.3, 'Sunday': 1.2},
    {'Age Group': '6-12 years', 'Monday': 2.0, 'Tuesday': 2.1, 'Wednesday': 2.2, 'Thursday': 2.3, 'Friday': 2.0, 'Saturday': 2.4, 'Sunday': 2.3},
    {'Age Group': '13-18 years', 'Monday': 4.0, 'Tuesday': 4.1, 'Wednesday': 3.8, 'Thursday': 4.0, 'Friday': 4.2, 'Saturday': 4.3, 'Sunday': 4.5},
    {'Age Group': '19-35 years', 'Monday': 3.5, 'Tuesday': 3.6, 'Wednesday': 3.7, 'Thursday': 3.8, 'Friday': 3.4, 'Saturday': 3.9, 'Sunday': 4.0},
    {'Age Group': '36-50 years', 'Monday': 2.8, 'Tuesday': 2.9, 'Wednesday': 3.0, 'Thursday': 2.9, 'Friday': 2.7, 'Saturday': 3.1, 'Sunday': 3.0},
    {'Age Group': '51-65 years', 'Monday': 1.5, 'Tuesday': 1.6, 'Wednesday': 1.7, 'Thursday': 1.8, 'Friday': 1.9, 'Saturday': 2.0, 'Sunday': 2.1},
    {'Age Group': '65+ years', 'Monday': 0.9, 'Tuesday': 0.8, 'Wednesday': 0.7, 'Thursday': 0.6, 'Friday': 0.5, 'Saturday': 0.6, 'Sunday': 0.7}
]

days = list(data[0].keys())[1:]

plt.figure(figsize=(14, 10))

markers = ['o', 's', 'D', '^', 'v', '*', 'P']
linestyles = ['-', '--', '-.', ':', '-', '--', '-.']
colors = ['#2E8B57', '#8A2BE2', '#FF4500', '#4682B4', '#DAA520', '#8B0000', '#20B2AA']

for age_data, marker, linestyle, color in zip(data, markers, linestyles, colors):
    age_group = age_data['Age Group']
    values = [age_data[day] for day in days]
    
    plt.plot(days, values, marker=marker, linestyle=linestyle, color=color, label=age_group)

plt.legend(title='Age Group', loc='upper left')

plt.title('Weekly Screen Time Across Different Age Groups')
plt.xlabel('Day of the Week')
plt.ylabel('Screen Time (Hours)')

plt.grid(True)

plt.annotate('Peak Usage', xy=('Sunday', 4.5), xytext=('Friday', 4.8),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()