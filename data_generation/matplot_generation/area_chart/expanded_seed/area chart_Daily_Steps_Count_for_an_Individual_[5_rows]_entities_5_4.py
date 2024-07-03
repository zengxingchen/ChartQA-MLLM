
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-04-01', 'Steps': 4562},
    {'Date': '2023-04-02', 'Steps': 5930},
    {'Date': '2023-04-03', 'Steps': 6710},
    {'Date': '2023-04-04', 'Steps': 7021},
    {'Date': '2023-04-05', 'Steps': 4873}
]

# Extracting dates and steps
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
steps = [d['Steps'] for d in data]

# Creating the plot
fig, ax = plt.subplots()

# Plotting the area chart with diversified visual encoding
ax.fill_between(dates, steps, color="skyblue", alpha=0.4)
ax.plot(dates, steps, color="Slateblue", alpha=0.6, linewidth=2)

# Formatting the dates on the x-axis
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# Adding a grid for better readability
plt.grid(color='grey', linestyle='--', linewidth=0.5)

# Adding titles and labels
plt.title('Steps Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Steps', fontsize=12)

# Highlighting the date with the most steps with a red circle
max_steps_index = steps.index(max(steps))
max_steps_date = dates[max_steps_index]
plt.scatter([max_steps_date], [max(steps)], color='red', s=40, label='Max Steps')

# Annotate the maximum point
plt.annotate('Max Steps', xy=(max_steps_date, max(steps)), xytext=(10, 3),
             textcoords='offset points', ha='center',
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='red', facecolor='white'))

# Adding a legend
plt.legend()

# Rotating the x-axis labels for better readability
plt.xticks(rotation=45)

# Adjusting the plot to fit the date labels properly
plt.tight_layout()

# Show the plot
plt.show()