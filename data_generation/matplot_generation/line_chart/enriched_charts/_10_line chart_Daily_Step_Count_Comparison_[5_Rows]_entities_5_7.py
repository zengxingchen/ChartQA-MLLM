
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Person A Steps': 5000, 'Person B Steps': 7000},
    {'Date': '2023-03-02', 'Person A Steps': 7500, 'Person B Steps': 10000},
    {'Date': '2023-03-03', 'Person A Steps': 8000, 'Person B Steps': 3000},
    {'Date': '2023-03-04', 'Person A Steps': 5500, 'Person B Steps': 4000},
    {'Date': '2023-03-05', 'Person A Steps': 9500, 'Person B Steps': 11000},
    {'Date': '2023-03-06', 'Person A Steps': 6000, 'Person B Steps': 8500},
    {'Date': '2023-03-07', 'Person A Steps': 4500, 'Person B Steps': 6000},
    {'Date': '2023-03-08', 'Person A Steps': 9000, 'Person B Steps': 12000},
    {'Date': '2023-03-09', 'Person A Steps': 8500, 'Person B Steps': 7000},
    {'Date': '2023-03-10', 'Person A Steps': 9500, 'Person B Steps': 10000}
]

# Parse the dates and steps
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
person_a_steps = [d['Person A Steps'] for d in data]
person_b_steps = [d['Person B Steps'] for d in data]

# Create a line plot for each person's steps
plt.figure(figsize=(12, 6))

plt.plot(dates, person_a_steps, label='Person A', color='#1f77b4', linestyle='-', marker='o', linewidth=2)
plt.plot(dates, person_b_steps, label='Person B', color='#ff7f0e', linestyle='--', marker='x', linewidth=2)

# Decorate the plot
plt.title('Daily Steps Comparison: Health & Psychology', pad=20)
plt.xlabel('Date')
plt.ylabel('Number of Steps')
plt.legend(loc='upper left')
plt.grid(True)

# Format the date on the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Rotate and align the date labels
plt.gcf().autofmt_xdate()

# Add annotations
for i, txt in enumerate(person_a_steps):
    plt.annotate(txt, (dates[i], person_a_steps[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
for i, txt in enumerate(person_b_steps):
    plt.annotate(txt, (dates[i], person_b_steps[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Show the plot
plt.show()