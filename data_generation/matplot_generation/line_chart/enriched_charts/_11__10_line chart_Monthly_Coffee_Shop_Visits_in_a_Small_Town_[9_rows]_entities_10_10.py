
import matplotlib.pyplot as plt

# Data from the provided chart table
data = [
    {'Month': 'January', 'Running': 50, 'Yoga': 80, 'Swimming': 70, 'Cycling': 60, 'Gym': 90},
    {'Month': 'February', 'Running': 55, 'Yoga': 85, 'Swimming': 65, 'Cycling': 65, 'Gym': 95},
    {'Month': 'March', 'Running': 60, 'Yoga': 90, 'Swimming': 75, 'Cycling': 70, 'Gym': 100},
    {'Month': 'April', 'Running': 65, 'Yoga': 88, 'Swimming': 80, 'Cycling': 75, 'Gym': 105},
    {'Month': 'May', 'Running': 70, 'Yoga': 95, 'Swimming': 85, 'Cycling': 80, 'Gym': 110},
    {'Month': 'June', 'Running': 75, 'Yoga': 100, 'Swimming': 90, 'Cycling': 85, 'Gym': 115},
    {'Month': 'July', 'Running': 80, 'Yoga': 105, 'Swimming': 95, 'Cycling': 90, 'Gym': 120},
    {'Month': 'August', 'Running': 85, 'Yoga': 110, 'Swimming': 100, 'Cycling': 95, 'Gym': 125},
    {'Month': 'September', 'Running': 90, 'Yoga': 115, 'Swimming': 105, 'Cycling': 100, 'Gym': 130},
    {'Month': 'October', 'Running': 95, 'Yoga': 120, 'Swimming': 110, 'Cycling': 105, 'Gym': 135},
    {'Month': 'November', 'Running': 90, 'Yoga': 115, 'Swimming': 105, 'Cycling': 100, 'Gym': 130},
    {'Month': 'December', 'Running': 85, 'Yoga': 110, 'Swimming': 100, 'Cycling': 95, 'Gym': 125}
]

# Extracting month names for the x-axis
months = [entry['Month'] for entry in data]

# Plotting each activity's trend
plt.figure(figsize=(16, 12))
activities = list(data[0].keys())[1:]  # Get activity names skipping the 'Month' key

# Line style settings and markers for each activity
line_styles = ['-', '--', '-.', ':']
markers = ['o', '^', 's', 'D', 'x']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i, activity in enumerate(activities):
    values = [entry[activity] for entry in data]
    plt.plot(months, values, label=activity, linestyle=line_styles[i % len(line_styles)], marker=markers[i % len(markers)], color=colors[i % len(colors)])
    # Adding annotation for the last data point
    plt.text(months[-1], values[-1], f'{values[-1]}', fontsize=10, color=colors[i % len(colors)])

# Adding titles and labels
plt.title('Monthly Exercise Trends in Health & Psychology', pad=20)
plt.xlabel('Month')
plt.ylabel('Participation (in thousands)')

# Adding grid for readability
plt.grid(True)

# Adding a legend to identify the lines
plt.legend(title='Activities', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()