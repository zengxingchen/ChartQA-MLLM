
import matplotlib.pyplot as plt

data = [
    {'Age Group': '0-5 years', 'Monday': 1.0, 'Tuesday': 0.8, 'Wednesday': 0.7, 'Thursday': 0.6, 'Friday': 0.5},
    {'Age Group': '6-12 years', 'Monday': 1.9, 'Tuesday': 1.8, 'Wednesday': 1.7, 'Thursday': 1.6, 'Friday': 1.5},
    {'Age Group': '13-18 years', 'Monday': 4.5, 'Tuesday': 4.2, 'Wednesday': 4.0, 'Thursday': 3.8, 'Friday': 3.5},
    {'Age Group': '19-35 years', 'Monday': 3.3, 'Tuesday': 3.1, 'Wednesday': 3.0, 'Thursday': 2.8, 'Friday': 2.5},
    {'Age Group': '36-50 years', 'Monday': 2.4, 'Tuesday': 2.3, 'Wednesday': 2.1, 'Thursday': 2.0, 'Friday': 1.8},
    {'Age Group': '51-65 years', 'Monday': 1.5, 'Tuesday': 1.4, 'Wednesday': 1.3, 'Thursday': 1.1, 'Friday': 0.9},
    {'Age Group': '65+ years', 'Monday': 1.0, 'Tuesday': 0.9, 'Wednesday': 0.8, 'Thursday': 0.6, 'Friday': 0.4}
]

days = list(data[0].keys())[1:]

plt.figure(figsize=(12, 8))

markers = ['o', 's', 'D', '^', 'v', '*', 'P']
linestyles = ['-', '--', '-.', ':', '-', '--', '-.']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

for age_data, marker, linestyle, color in zip(data, markers, linestyles, colors):
    age_group = age_data['Age Group']
    values = [age_data[day] for day in days]
    
    plt.plot(days, values, marker=marker, linestyle=linestyle, color=color, label=age_group)

plt.legend(title='Age Group', loc='upper right')

plt.title('Daily Water Consumption by Age Group (liters)')
plt.xlabel('Day of the Week')
plt.ylabel('Water Consumption (liters)')
plt.gca().invert_yaxis()

plt.grid(True)

plt.annotate('Highest Consumption', xy=('Monday', 4.5), xytext=('Wednesday', 4.7),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()