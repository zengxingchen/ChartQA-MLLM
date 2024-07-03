
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Step Count': 4500, 'Calories Burned': 150},
    {'Date': '2023-03-02', 'Step Count': 4200, 'Calories Burned': 140},
    {'Date': '2023-03-03', 'Step Count': 4600, 'Calories Burned': 160},
    {'Date': '2023-03-04', 'Step Count': 3900, 'Calories Burned': 130},
    {'Date': '2023-03-05', 'Step Count': 3700, 'Calories Burned': 120},
    {'Date': '2023-03-06', 'Step Count': 3400, 'Calories Burned': 110},
    {'Date': '2023-03-07', 'Step Count': 3100, 'Calories Burned': 100}
]

# Extracting data for plotting
dates = [datetime.strptime(item['Date'], '%Y-%m-%d') for item in data]
step_counts = [item['Step Count'] for item in data]
calories_burned = [item['Calories Burned'] for item in data]

# Setting up the plot
plt.figure(figsize=(10, 8))

# Plotting both step counts and calories burned
plt.plot(dates, step_counts, marker='o', linestyle='-', color='#ff5733', label='Step Count')
plt.plot(dates, calories_burned, marker='s', linestyle='--', color='#33ff57', label='Calories Burned')

# Formatting the x-axis to show dates clearly
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Adding some aesthetics
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Weekly Physical Activity Tracking', pad=20)
plt.legend(loc='upper right')
plt.grid(True)

# Rotating the date labels for better readability
plt.gcf().autofmt_xdate()

# Adding annotations
for i, txt in enumerate(step_counts):
    plt.annotate(txt, (dates[i], step_counts[i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(calories_burned):
    plt.annotate(txt, (dates[i], calories_burned[i]), textcoords="offset points", xytext=(0,-15), ha='center', color='#33ff57')

# Inverting the y-axis
plt.gca().invert_yaxis()

# To show the plot
plt.show()