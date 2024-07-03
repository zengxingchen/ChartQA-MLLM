
import matplotlib.pyplot as plt
import numpy as np

# Data from your table
data = [
    {'Age Group': '0-12', 'Monday': 34, 'Tuesday': 30, 'Wednesday': 40, 'Thursday': 45, 'Friday': 20, 'Saturday': 50, 'Sunday': 60},
    {'Age Group': '13-18', 'Monday': 45, 'Tuesday': 42, 'Wednesday': 50, 'Thursday': 44, 'Friday': 35, 'Saturday': 55, 'Sunday': 45},
    {'Age Group': '19-35', 'Monday': 75, 'Tuesday': 68, 'Wednesday': 80, 'Thursday': 90, 'Friday': 60, 'Saturday': 70, 'Sunday': 55},
    {'Age Group': '36-50', 'Monday': 50, 'Tuesday': 45, 'Wednesday': 60, 'Thursday': 55, 'Friday': 40, 'Saturday': 65, 'Sunday': 35},
    {'Age Group': '51-65', 'Monday': 40, 'Tuesday': 38, 'Wednesday': 45, 'Thursday': 50, 'Friday': 30, 'Saturday': 55, 'Sunday': 25},
    {'Age Group': '66+', 'Monday': 30, 'Tuesday': 28, 'Wednesday': 35, 'Thursday': 30, 'Friday': 25, 'Saturday': 40, 'Sunday': 20}
]

# Age Groups and Days of the week
age_groups = [entry['Age Group'] for entry in data]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Initialising numpy arrays to hold the data for the bar heights
visits_per_day = {day: np.array([entry[day] for entry in data]) for day in days}

# Number of age groups
n_groups = len(age_groups)

# Create a figure and an axis
fig, ax = plt.subplots()

# The bar locations on the x-axis
ind = np.arange(n_groups)
width = 0.1  # the width of the bars

# Stacking the bars
for i, day in enumerate(days):
    if i == 0:
        ax.bar(ind, visits_per_day[day], width, label=day)
    else:
        prev_data = sum(visits_per_day[days[j]] for j in range(i))
        ax.bar(ind, visits_per_day[day], width, bottom=prev_data, label=day)

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Age Groups')
ax.set_ylabel('Number of Visitors')
ax.set_title('Number of Visitors by Age Group and Day of the Week')
ax.set_xticks(ind)
ax.set_xticklabels(age_groups)
ax.legend(title='Days', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()   # To adjust plots to fit into figure cleanly
plt.show()