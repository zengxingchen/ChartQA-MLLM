
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Step Count': 5500, 'Calories Burned': 200},
    {'Date': '2023-03-02', 'Step Count': 6200, 'Calories Burned': 220},
    {'Date': '2023-03-03', 'Step Count': 4800, 'Calories Burned': 180},
    {'Date': '2023-03-04', 'Step Count': 7100, 'Calories Burned': 260},
    {'Date': '2023-03-05', 'Step Count': 5400, 'Calories Burned': 210},
    {'Date': '2023-03-06', 'Step Count': 6700, 'Calories Burned': 230},
    {'Date': '2023-03-07', 'Step Count': 5900, 'Calories Burned': 220}
]

# Extracting data for plotting
dates = [datetime.strptime(item['Date'], '%Y-%m-%d') for item in data]
step_counts = [item['Step Count'] for item in data]
calories_burned = [item['Calories Burned'] for item in data]

# Setting up the plot
plt.figure(figsize=(12, 6))

# Plotting both step counts and calories burned
plt.plot(dates, step_counts, marker='o', linestyle='-', color='#1f77b4', label='Step Count')
plt.plot(dates, calories_burned, marker='s', linestyle='--', color='#ff7f0e', label='Calories Burned')

# Formatting the x-axis to show dates clearly
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Adding some aesthetics
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Daily Step Count and Calories Burned Over a Week')
plt.legend(loc='upper left')
plt.grid(True)

# Rotating the date labels for better readability
plt.gcf().autofmt_xdate()

# Adding annotations
for i, txt in enumerate(step_counts):
    plt.annotate(txt, (dates[i], step_counts[i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(calories_burned):
    plt.annotate(txt, (dates[i], calories_burned[i]), textcoords="offset points", xytext=(0,-15), ha='center', color='#ff7f0e')

# To show the plot
plt.show()