
import matplotlib.pyplot as plt
import numpy as np

# Given data
data = [
    {'Family Member': 'Alex', ' Cooking': 10, ' Cleaning': 20, ' Laundry': 30, ' Gardening': 5, ' Shopping': 15, ' Maintenance': 20},
    {'Family Member': 'Jamie', ' Cooking': 15, ' Cleaning': 20, ' Laundry': 10, ' Gardening': 10, ' Shopping': 20, ' Maintenance': 25},
    {'Family Member': 'Sam', ' Cooking': 20, ' Cleaning': 15, ' Laundry': 25, ' Gardening': 10, ' Shopping': 10, ' Maintenance': 20},
    {'Family Member': 'Jordan', ' Cooking': 30, ' Cleaning': 25, ' Laundry': 10, ' Gardening': 15, ' Shopping': 10, ' Maintenance': 10},
    {'Family Member': 'Charlie', ' Cooking': 10, ' Cleaning': 5, ' Laundry': 5, ' Gardening': 25, ' Shopping': 20, ' Maintenance': 35},
    {'Family Member': 'Taylor', ' Cooking': 20, ' Cleaning': 25, ' Laundry': 10, ' Gardening': 10, ' Shopping': 15, ' Maintenance': 20},
    {'Family Member': 'Casey', ' Cooking': 15, ' Cleaning': 30, ' Laundry': 5, ' Gardening': 10, ' Shopping': 30, ' Maintenance': 10},
    {'Family Member': 'Riley', ' Cooking': 25, ' Cleaning': 15, ' Laundry': 20, ' Gardening': 20, ' Shopping': 5, ' Maintenance': 15}
]

# List for family member names and colors for each activity
family_members = [item['Family Member'] for item in data]
activities = ['Cooking', 'Cleaning', 'Laundry', 'Gardening', 'Shopping', 'Maintenance']
colors = plt.get_cmap('viridis')(np.linspace(0, 1, len(activities)))

# Transform data into percentages
percentages = {activity: [] for activity in activities}
for item in data:
    total = sum([item[activity] for activity in activities if activity in item])
    for activity in activities:
        if activity in item:
            percentages[activity].append((item[activity] / total) * 100)

# Plot stacked bar chart
fig, ax = plt.subplots()

bar_width = 0.5
r = np.arange(len(family_members))

# Keep track of the bottom positions for each stack
bar_bottoms = np.zeros(len(family_members))

for activity, color in zip(activities, colors):
    ax.bar(
        r,
        percentages[activity],
        bottom=bar_bottoms,
        color=color,
        edgecolor='white',
        width=bar_width,
        label=activity
    )
    bar_bottoms += np.array(percentages[activity])

# Customizations
ax.set_xlabel('Family Member', fontweight='bold')
ax.set_ylabel('Percentage of Activities (%)', fontweight='bold')
ax.set_title('100% Stacked Bar Chart of Family Activities')
ax.set_xticks(r)
ax.set_xticklabels(family_members, rotation=45, ha='right')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Activities')

# Show the plot
plt.tight_layout()
plt.show()