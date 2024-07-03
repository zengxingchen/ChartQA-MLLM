
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Week': 'Week 1', 'Ages 0-12': 150, 'Ages 13-18': 90, 'Ages 19-30': 120, 'Ages 31-50': 130, 'Ages 51+': 80},
    {'Week': 'Week 2', 'Ages 0-12': 135, 'Ages 13-18': 95, 'Ages 19-30': 110, 'Ages 31-50': 140, 'Ages 51+': 85},
    {'Week': 'Week 3', 'Ages 0-12': 160, 'Ages 13-18': 100, 'Ages 19-30': 130, 'Ages 31-50': 120, 'Ages 51+': 75},
    {'Week': 'Week 4', 'Ages 0-12': 145, 'Ages 13-18': 85, 'Ages 19-30': 125, 'Ages 31-50': 115, 'Ages 51+': 90},
    {'Week': 'Week 5', 'Ages 0-12': 155, 'Ages 13-18': 95, 'Ages 19-30': 135, 'Ages 31-50': 125, 'Ages 51+': 85},
    {'Week': 'Week 6', 'Ages 0-12': 140, 'Ages 13-18': 90, 'Ages 19-30': 120, 'Ages 31-50': 130, 'Ages 51+': 80},
    {'Week': 'Week 7', 'Ages 0-12': 150, 'Ages 13-18': 100, 'Ages 19-30': 140, 'Ages 31-50': 135, 'Ages 51+': 78},
    {'Week': 'Week 8', 'Ages 0-12': 160, 'Ages 13-18': 110, 'Ages 19-30': 150, 'Ages 31-50': 125, 'Ages 51+': 82}
]

# Prepare data for plotting
weeks = [entry['Week'] for entry in data]
ages_0_12 = [entry['Ages 0-12'] for entry in data]
ages_13_18 = [entry['Ages 13-18'] for entry in data]
ages_19_30 = [entry['Ages 19-30'] for entry in data]
ages_31_50 = [entry['Ages 31-50'] for entry in data]
ages_51_plus = [entry['Ages 51+'] for entry in data]

# Setup the figure and axes
fig, ax = plt.subplots(figsize=(10, 7))

# Plot stacked bars
ax.bar(weeks, ages_0_12, label='Ages 0-12', color='#1f77b4')
ax.bar(weeks, ages_13_18, bottom=ages_0_12, label='Ages 13-18', color='#ff7f0e')
ax.bar(weeks, ages_19_30, bottom=[i + j for i, j in zip(ages_0_12, ages_13_18)], label='Ages 19-30', color='#2ca02c')
ax.bar(weeks, ages_31_50, bottom=[i + j + k for i, j, k in zip(ages_0_12, ages_13_18, ages_19_30)], label='Ages 31-50', color='#d62728')
ax.bar(weeks, ages_51_plus, bottom=[i + j + k + l for i, j, k, l in zip(ages_0_12, ages_13_18, ages_19_30, ages_31_50)], label='Ages 51+', color='#9467bd')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Week')
ax.set_ylabel('Number of People')
ax.set_title('Number of People by Age Group and Week')
ax.set_xticks(range(len(weeks)))
ax.set_xticklabels(weeks)
ax.legend()

# Show the plot
plt.show()