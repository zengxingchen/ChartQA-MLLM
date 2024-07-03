
import matplotlib.pyplot as plt

# Given data
data = [
    {'Age Group': '0-8', ' Average Screen Time (hours)': 1.5},
    {'Age Group': '9-12', ' Average Screen Time (hours)': 3.0},
    {'Age Group': '13-18', ' Average Screen Time (hours)': 4.5},
    {'Age Group': '19-25', ' Average Screen Time (hours)': 6.5},
    {'Age Group': '26-35', ' Average Screen Time (hours)': 8.0}
]

# Extract age groups and screen times into separate lists
age_groups = [x['Age Group'] for x in data]
screen_times = [x[' Average Screen Time (hours)'] for x in data]

# Generate a list of unique colors, one for each age group
colors = plt.cm.jet(range(len(age_groups)))

# Generate a list of marker sizes based on screen time
# Adjust the size by a factor, e.g., 50 to make the differences more visible
sizes = [50 * t for t in screen_times]

# Plot the data using a scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(range(len(age_groups)), screen_times, s=sizes, c=colors, alpha=0.6, edgecolors='w')

# Customize the tick labels on the x-axis to represent the age groups
plt.xticks(range(len(age_groups)), age_groups)

# Add labels and title
plt.xlabel('Age Group')
plt.ylabel('Average Screen Time (hours)')
plt.title('Average Screen Time by Age Group')

# Add a legend, using a proxy artist for the sizes
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='1.5 hours', markerfacecolor='k', markersize=5),
    Line2D([0], [0], marker='o', color='w', label='3.0 hours', markerfacecolor='k', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='4.5 hours', markerfacecolor='k', markersize=15),
    Line2D([0], [0], marker='o', color='w', label='6.5 hours', markerfacecolor='k', markersize=20),
    Line2D([0], [0], marker='o', color='w', label='8.0 hours', markerfacecolor='k', markersize=25),
]
plt.legend(handles=legend_elements, title='Screen Time (sizes)', loc='upper left')

# Show the plot
plt.show()