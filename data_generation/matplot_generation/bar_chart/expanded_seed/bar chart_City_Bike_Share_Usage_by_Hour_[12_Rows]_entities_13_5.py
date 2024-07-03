
import matplotlib.pyplot as plt
import numpy as np

# Given chart table data
data = [
    {'Hour': '00:00', 'Weekday Rentals': 15, 'Weekend Rentals': 40},
    {'Hour': '01:00', 'Weekday Rentals': 10, 'Weekend Rentals': 35},
    {'Hour': '02:00', 'Weekday Rentals': 5,  'Weekend Rentals': 20},
    {'Hour': '03:00', 'Weekday Rentals': 4,  'Weekend Rentals': 15},
    {'Hour': '04:00', 'Weekday Rentals': 20, 'Weekend Rentals': 10},
    {'Hour': '05:00', 'Weekday Rentals': 60, 'Weekend Rentals': 12},
    {'Hour': '06:00', 'Weekday Rentals': 150,'Weekend Rentals': 25},
    {'Hour': '07:00', 'Weekday Rentals': 300,'Weekend Rentals': 30},
    {'Hour': '08:00', 'Weekday Rentals': 275,'Weekend Rentals': 45},
    {'Hour': '09:00', 'Weekday Rentals': 130,'Weekend Rentals': 55},
    {'Hour': '10:00', 'Weekday Rentals': 110,'Weekend Rentals': 200},
    {'Hour': '11:00', 'Weekday Rentals': 90, 'Weekend Rentals': 250},
    {'Hour': '12:00', 'Weekday Rentals': 100,'Weekend Rentals': 300}
]

# Extracting hours, weekday rentals and weekend rentals into separate lists
hours = [item['Hour'] for item in data]
weekday_rentals = [item['Weekday Rentals'] for item in data]
weekend_rentals = [item['Weekend Rentals'] for item in data]

# Setting the positions and width for the bars
positions = np.arange(len(hours))
bar_width = 0.35

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Creating bar plots
weekday_bars = ax.bar(positions - bar_width/2, weekday_rentals, bar_width, label='Weekday Rentals', color='blue', edgecolor='black')
weekend_bars = ax.bar(positions + bar_width/2, weekend_rentals, bar_width, label='Weekend Rentals', color='orange', edgecolor='black')

# Adding text for labels, title and custom x-axis tick labels
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Number of Rentals')
ax.set_title('Bicycle Rentals per Hour - Weekday vs Weekend')
ax.set_xticks(positions)
ax.set_xticklabels(hours)

# Adding a legend
ax.legend()

# Adding bar labels
def add_bar_labels(bars):
    """Attach a text label above each bar displaying its height."""
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_bar_labels(weekday_bars)
add_bar_labels(weekend_bars)

# Displaying the plot
plt.tight_layout()
plt.show()