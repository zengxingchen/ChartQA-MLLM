
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Age Group': '0-12', 'Day 1': 2.0, 'Day 2': 1.5, 'Day 3': 2.0, 'Day 4': 2.5, 'Day 5': 2.0},
    {'Age Group': '13-18', 'Day 1': 3.5, 'Day 2': 4.0, 'Day 3': 4.5, 'Day 4': 3.5, 'Day 5': 4.0},
    {'Age Group': '19-35', 'Day 1': 5.5, 'Day 2': 6.0, 'Day 3': 5.0, 'Day 4': 6.5, 'Day 5': 6.0},
    {'Age Group': '36-50', 'Day 1': 4.0, 'Day 2': 4.5, 'Day 3': 3.5, 'Day 4': 4.0, 'Day 5': 4.0},
    {'Age Group': '51+', 'Day 1': 3.0, 'Day 2': 2.5, 'Day 3': 3.0, 'Day 4': 3.0, 'Day 5': 2.8}
]

# Preparing data for plotting
age_groups = [d['Age Group'] for d in data]
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
plots_data = {age_group: [d[day] for day in days] for age_group in age_groups}

# Colors, markers, and line styles for each age group
colors = ['blue', 'green', 'red', 'purple', 'orange']
markers = ['o', 's', '^', 'D', 'x']
line_styles = ['-', '--', '-.', ':', '-']

# Plotting the lines for each age group
for (age_group, color, marker, line_style) in zip(age_groups, colors, markers, line_styles):
    plt.plot(days, plots_data[age_group], label=age_group, color=color, marker=marker, linestyle=line_style)

# Adding title and labels
plt.title('Attendance by Age Group Over 5 Days')
plt.xlabel('Days')
plt.ylabel('Attendance')

# Adding a legend
plt.legend(title='Age Group')

# Adjust plot to display well
plt.tight_layout()

# Show the plot
plt.show()