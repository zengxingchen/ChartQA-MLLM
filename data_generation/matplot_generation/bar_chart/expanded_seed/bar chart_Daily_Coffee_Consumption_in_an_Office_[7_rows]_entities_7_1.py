
import matplotlib.pyplot as plt
import numpy as np

# The provided data
data = [
    {'Employee': 'Alice', 'Monday': 3, 'Tuesday': 2, 'Wednesday': 4, 'Thursday': 3, 'Friday': 2},
    {'Employee': 'Bob', 'Monday': 1, 'Tuesday': 1, 'Wednesday': 1, 'Thursday': 1, 'Friday': 2},
    {'Employee': 'Carol', 'Monday': 2, 'Tuesday': 3, 'Wednesday': 2, 'Thursday': 2, 'Friday': 3},
    {'Employee': 'David', 'Monday': 0, 'Tuesday': 1, 'Wednesday': 0, 'Thursday': 1, 'Friday': 1},
    {'Employee': 'Elena', 'Monday': 4, 'Tuesday': 4, 'Wednesday': 5, 'Thursday': 4, 'Friday': 3},
    {'Employee': 'Frank', 'Monday': 3, 'Tuesday': 3, 'Wednesday': 2, 'Thursday': 2, 'Friday': 2},
    {'Employee': 'Grace', 'Monday': 2, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 2, 'Friday': 2}
]

# Extracting employees' names for the legend
employees = [entry['Employee'] for entry in data]

# Extracting the days of the week for the x-axis
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# The index for each bar group (day)
day_index = np.arange(len(days))

# The width of each bar
bar_width = 0.1

# Generate a color for each employee
colors = plt.cm.viridis(np.linspace(0, 1, len(employees)))

# Create a bar for each employee on each day
for i, employee in enumerate(employees):
    # Extracting the performance of this employee for each day
    performance = [entry[day] for entry in data if entry['Employee'] == employee][0]
    
    # Position of the bar (offset by the width of a bar times the index of the employee)
    position = day_index + (i * bar_width)
    
    # Plotting the bar
    plt.bar(position, performance, color=colors[i], width=bar_width, edgecolor='grey', label=employee)

# Setting the x-axis to show each day with a group of bars
plt.xticks(day_index + bar_width * (len(employees) - 1) / 2, days)

# Adding labels and title
plt.xlabel('Day of the Week')
plt.ylabel('Performance')
plt.title('Performance of Employees Over the Week')

# Adding a legend
plt.legend(title='Employee', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to not cut off the legend
plt.tight_layout()

# Display the plot
plt.show()