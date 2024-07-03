
import matplotlib.pyplot as plt
import numpy as np

data = {
    '18-25': [40, 35, 15, 10],
    '26-35': [30, 40, 20, 10],
    '36-45': [25, 35, 25, 15],
    '46-55': [20, 30, 30, 20],
    '56-65': [15, 25, 35, 25],
    '66+': [10, 20, 40, 30]
}

categories = ['Cardio', 'Strength Training', 'Flexibility', 'Other']
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
age_groups = list(data.keys())
values = np.array(list(data.values()))
values_cum = values.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars
for i, col in enumerate(categories):
    widths = values[:, i]
    starts = values_cum[:, i] - widths
    ax.barh(age_groups, widths, left=starts, height=0.7, label=col, color=colors[i])

# Add labels
ax.set_xlabel('Percentage')
ax.set_ylabel('Age Group')
ax.set_title('Percentage Distribution of Workout Types Among Age Groups')
ax.legend(ncol=len(categories), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.show()