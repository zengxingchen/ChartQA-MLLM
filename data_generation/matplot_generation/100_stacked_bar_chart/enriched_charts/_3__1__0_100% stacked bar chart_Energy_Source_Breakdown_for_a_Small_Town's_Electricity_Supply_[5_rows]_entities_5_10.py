
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Week 1': [20, 25, 30, 15, 10],
    'Week 2': [18, 30, 28, 12, 12],
    'Week 3': [22, 22, 32, 14, 10],
    'Week 4': [25, 20, 25, 20, 10],
    'Week 5': [20, 28, 30, 12, 10],
    'Week 6': [15, 30, 28, 17, 10],
    'Week 7': [18, 25, 30, 17, 10],
    'Week 8': [22, 20, 30, 18, 10],
    'Week 9': [20, 25, 25, 20, 10],
    'Week 10': [25, 20, 25, 20, 10],
    'Week 11': [20, 28, 22, 20, 10],
    'Week 12': [18, 30, 25, 17, 10],
}

categories = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga']
weeks = list(data.keys())
values = np.array(list(data.values()))

# Normalize data to 100%
values_percentage = values / values.sum(axis=1, keepdims=True) * 100

# Colors for each category
colors = ['#FF6347', '#FFD700', '#4682B4', '#32CD32', '#FF69B4']

# Create a horizontal stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(weeks))

for i, (cat, color) in enumerate(zip(categories, colors)):
    ax.barh(weeks, values_percentage[:, i], left=bottom, color=color, label=cat)
    bottom += values_percentage[:, i]

ax.set_xlabel('Percentage')
ax.set_title('Weekly Distribution of Fitness Activities')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)

plt.tight_layout()
plt.show()