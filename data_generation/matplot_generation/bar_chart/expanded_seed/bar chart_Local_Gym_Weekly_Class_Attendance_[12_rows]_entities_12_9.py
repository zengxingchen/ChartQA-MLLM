
import matplotlib.pyplot as plt
import numpy as np

# Provided data
data = [
    {'Class Name': 'Yoga', 'Monday': 20, 'Tuesday': 22, 'Wednesday': 25, 'Thursday': 30, 'Friday': 18, 'Saturday': 35, 'Sunday': 40},
    {'Class Name': 'Pilates', 'Monday': 15, 'Tuesday': 20, 'Wednesday': 18, 'Thursday': 22, 'Friday': 15, 'Saturday': 28, 'Sunday': 30},
    {'Class Name': 'Zumba', 'Monday': 25, 'Tuesday': 30, 'Wednesday': 35, 'Thursday': 40, 'Friday': 33, 'Saturday': 45, 'Sunday': 50},
    # ... include all other class data here
    {'Class Name': 'Boxing', 'Monday': 20, 'Tuesday': 24, 'Wednesday': 25, 'Thursday': 27, 'Friday': 23, 'Saturday': 30, 'Sunday': 32}
]

# Extracting class names and the days of the week
class_names = [d["Class Name"] for d in data]
days_of_week = list(data[0].keys())[1:]  # Assuming all data points have the same structure

# Number of classes and days for plotting purposes
num_classes = len(class_names)
num_days = len(days_of_week)

# Assigning an index and width to each bar
indices = np.arange(num_days)
bar_width = 1 / (num_classes + 2)  # Space for separation between groups

# Creating a color map for visual distinction
colors = plt.cm.tab20(np.linspace(0, 1, num_classes))

# Plotting the data
fig, ax = plt.subplots()

for i, class_data in enumerate(data):
    attendance_values = [class_data[day] for day in days_of_week]
    ax.bar(indices + i * bar_width, attendance_values, bar_width, label=class_data["Class Name"], color=colors[i])

# Formatting the chart
ax.set_xlabel('Days of the Week')
ax.set_ylabel('Number of Attendees')
ax.set_title('Class Attendance through the Week')
ax.set_xticks(indices + bar_width * (num_classes / 2) - bar_width / 2)
ax.set_xticklabels(days_of_week)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Place the legend outside the plot area

# Display the plot
plt.show()