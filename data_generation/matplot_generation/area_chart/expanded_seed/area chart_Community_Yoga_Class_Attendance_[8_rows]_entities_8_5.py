
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given chart table data
data = [
    {'Week': '2023-01-02', 'Attendance': 25},
    {'Week': '2023-01-09', 'Attendance': 30},
    {'Week': '2023-01-16', 'Attendance': 27},
    {'Week': '2023-01-23', 'Attendance': 32},
    {'Week': '2023-01-30', 'Attendance': 29},
    {'Week': '2023-02-06', 'Attendance': 35},
    {'Week': '2023-02-13', 'Attendance': 33},
    {'Week': '2023-02-20', 'Attendance': 38}
]

# Extracting 'Week' and 'Attendance' values
weeks = [datetime.strptime(point['Week'], '%Y-%m-%d') for point in data]
attendance = [point['Attendance'] for point in data]

# Create the area chart
plt.figure(figsize=(10, 6))
plt.fill_between(weeks, attendance, color='skyblue', alpha=0.5)
plt.plot(weeks, attendance, color='Slateblue', alpha=0.6, linewidth=2)

# Format the date on the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))

# Set the labels and title
plt.xlabel('Week', fontsize=12)
plt.ylabel('Attendance', fontsize=12)
plt.title('Weekly Attendance Over Time', fontsize=16)

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Adding a grid for better readability of the chart
plt.grid(True)

# Shows data points on the graph
for i, txt in enumerate(attendance):
    plt.annotate(txt, (mdates.date2num(weeks[i]), attendance[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Optimize layout and display the plot
plt.tight_layout()
plt.show()