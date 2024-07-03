
import matplotlib.pyplot as plt

# Data from the provided chart table
data = [
    {'Month': 'January', 'Children': 30, 'Teens': 50, 'Adults': 70, 'Seniors': 40},
    {'Month': 'February', 'Children': 35, 'Teens': 55, 'Adults': 65, 'Seniors': 45},
    {'Month': 'March', 'Children': 40, 'Teens': 60, 'Adults': 75, 'Seniors': 50},
    {'Month': 'April', 'Children': 45, 'Teens': 65, 'Adults': 80, 'Seniors': 55},
    {'Month': 'May', 'Children': 50, 'Teens': 70, 'Adults': 85, 'Seniors': 60},
    {'Month': 'June', 'Children': 55, 'Teens': 75, 'Adults': 90, 'Seniors': 65},
    {'Month': 'July', 'Children': 60, 'Teens': 80, 'Adults': 95, 'Seniors': 70},
    {'Month': 'August', 'Children': 65, 'Teens': 85, 'Adults': 100, 'Seniors': 75},
    {'Month': 'September', 'Children': 70, 'Teens': 90, 'Adults': 105, 'Seniors': 80},
    {'Month': 'October', 'Children': 75, 'Teens': 95, 'Adults': 110, 'Seniors': 85},
    {'Month': 'November', 'Children': 80, 'Teens': 100, 'Adults': 115, 'Seniors': 90},
    {'Month': 'December', 'Children': 85, 'Teens': 105, 'Adults': 120, 'Seniors': 95},
]

# Extracting month names for the x-axis
months = [entry['Month'] for entry in data]

# Plotting each age group's trend
plt.figure(figsize=(16, 12))
age_groups = list(data[0].keys())[1:]  # Get age group names skipping the 'Month' key

# Line style settings and markers for each age group
line_styles = ['-', '--', '-.', ':']
markers = ['o', '^', 's', 'D']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

for i, group in enumerate(age_groups):
    values = [entry[group] for entry in data]
    plt.plot(months, values, label=group, linestyle=line_styles[i % len(line_styles)], marker=markers[i % len(markers)], color=colors[i % len(colors)])
    # Adding annotation for the last data point
    plt.text(months[-1], values[-1], f'{values[-1]}', fontsize=10, color=colors[i % len(colors)])

# Adding titles and labels
plt.title('Monthly Exercise Trends by Age Group', pad=20, fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Exercise Hours per Week', fontsize=14)

# Adding grid for readability
plt.grid(True)

# Adding a legend to identify the lines
plt.legend(title='Age Groups', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()