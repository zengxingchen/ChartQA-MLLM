
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Person A Steps': 5000, 'Person B Steps': 7000},
    {'Date': '2023-03-02', 'Person A Steps': 7500, 'Person B Steps': 10000},
    {'Date': '2023-03-03', 'Person A Steps': 8000, 'Person B Steps': 3000},
    {'Date': '2023-03-04', 'Person A Steps': 5500, 'Person B Steps': 4000},
    {'Date': '2023-03-05', 'Person A Steps': 9500, 'Person B Steps': 11000}
]

# Parse the dates and steps
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
person_a_steps = [d['Person A Steps'] for d in data]
person_b_steps = [d['Person B Steps'] for d in data]

# Create a line plot for each person's steps
plt.figure(figsize=(10, 5))

plt.plot(dates, person_a_steps, label='Person A', color='blue', linestyle='-', marker='o', linewidth=2)
plt.plot(dates, person_b_steps, label='Person B', color='green', linestyle='--', marker='x', linewidth=2)

# Decorate the plot
plt.title('Daily Steps Comparison')
plt.xlabel('Date')
plt.ylabel('Number of Steps')
plt.legend()
plt.grid(True)

# Format the date on the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Rotate and align the date labels
plt.gcf().autofmt_xdate()

# Show the plot
plt.show()