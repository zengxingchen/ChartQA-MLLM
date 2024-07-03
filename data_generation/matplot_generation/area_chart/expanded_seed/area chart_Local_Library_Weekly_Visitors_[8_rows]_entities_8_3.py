
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Week': '2023-03-01 to 2023-03-07', 'Visitors': 1200},
    {'Week': '2023-03-08 to 2023-03-14', 'Visitors': 1350},
    {'Week': '2023-03-15 to 2023-03-21', 'Visitors': 1500},
    {'Week': '2023-03-22 to 2023-03-28', 'Visitors': 1100},
    {'Week': '2023-03-29 to 2023-04-04', 'Visitors': 1250},
    {'Week': '2023-04-05 to 2023-04-11', 'Visitors': 1300},
    {'Week': '2023-04-12 to 2023-04-18', 'Visitors': 1450},
    {'Week': '2023-04-19 to 2023-04-25', 'Visitors': 1550}
]

# Extract 'Week' start dates and 'Visitors' as separate lists
weeks = [datetime.strptime(week.split(' to ')[0], "%Y-%m-%d") for week in [d['Week'] for d in data]]
visitors = [d['Visitors'] for d in data]

# Create figure and axis
plt.figure(figsize=(10,6))

# Plot area chart with 'weeks' on x-axis and 'visitors' on y-axis
plt.fill_between(weeks, visitors, color="skyblue", alpha=0.4)
plt.plot(weeks, visitors, color="Slateblue", alpha=0.6)

# Setting the x-axis to display the dates properly
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))

# Adding grid, title, labels, and annotations
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Weekly Visitors', fontsize=16)
plt.xlabel('Week (Starting from)')
plt.ylabel('Number of Visitors')

# Annotating each data point
for i, txt in enumerate(visitors):
    plt.annotate(txt, (mdates.date2num(weeks[i]), visitors[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Highlight peak visitor number.
peak_visitors = max(visitors)
peak_week = weeks[visitors.index(peak_visitors)]
plt.annotate(f'Peak\n{peak_visitors}', xy=(mdates.date2num(peak_week), peak_visitors), 
             xytext=(15,15), textcoords='offset points', arrowprops=dict(arrowstyle="->", color='red'))

# Rotate date labels
plt.xticks(rotation=45)

# Show plot with tight layout
plt.tight_layout()
plt.show()