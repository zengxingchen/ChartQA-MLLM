
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Children': 42, 'Teens': 35, 'Adults': 87},
    {'Date': '2023-03-02', 'Children': 38, 'Teens': 40, 'Adults': 82},
    {'Date': '2023-03-03', 'Children': 47, 'Teens': 32, 'Adults': 90},
    {'Date': '2023-03-04', 'Children': 53, 'Teens': 48, 'Adults': 103},
    {'Date': '2023-03-05', 'Children': 60, 'Teens': 55, 'Adults': 110},
    {'Date': '2023-03-06', 'Children': 35, 'Teens': 30, 'Adults': 85},
    {'Date': '2023-03-07', 'Children': 45, 'Teens': 38, 'Adults': 89},
    {'Date': '2023-03-08', 'Children': 50, 'Teens': 42, 'Adults': 92},
    {'Date': '2023-03-09', 'Children': 55, 'Teens': 37, 'Adults': 88}
]

# Preprocessing the data for plotting
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
children_counts = [d['Children'] for d in data]
teens_counts = [d['Teens'] for d in data]
adults_counts = [d['Adults'] for d in data]

# Setting up the plot
plt.figure(figsize=(10, 6))

# Children line
plt.plot(dates, children_counts, label='Children', color='skyblue', linewidth=2, linestyle='-', marker='o')

# Teens line
plt.plot(dates, teens_counts, label='Teens', color='coral', linewidth=2, linestyle='--', marker='^')

# Adults line
plt.plot(dates, adults_counts, label='Adults', color='olivedrab', linewidth=2, linestyle=':', marker='s')

# Format the x-axis to show date labels
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.gcf().autofmt_xdate()  # Rotation

# Adding legend, title, labels and grid
plt.legend()
plt.title('Daily Visitors by Age Group')
plt.xlabel('Date')
plt.ylabel('Number of Visitors')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()