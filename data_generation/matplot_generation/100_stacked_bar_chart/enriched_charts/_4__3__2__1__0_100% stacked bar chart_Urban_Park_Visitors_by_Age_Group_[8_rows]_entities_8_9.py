
import matplotlib.pyplot as plt
import numpy as np

# Data
metrics = ['Sleep Quality', 'Physical Activity', 'Mental Wellness', 'Diet', 'Stress Levels']
data = [
    [22, 25, 18, 25, 10],  # Person 1
    [18, 20, 22, 30, 10],  # Person 2
    [20, 30, 25, 20, 5],   # Person 3
    [25, 20, 15, 25, 15],  # Person 4
    [17, 22, 30, 20, 11],  # Person 5
    [20, 25, 20, 25, 10],  # Person 6
    [22, 18, 25, 20, 15],  # Person 7
    [18, 20, 22, 30, 10],  # Person 8
    [25, 22, 20, 18, 15],  # Person 9
    [20, 25, 25, 20, 10]   # Person 10
]

data = np.array(data)
data_cum = data.cumsum(axis=0)
person_labels = ['Person 1', 'Person 2', 'Person 3', 'Person 4', 'Person 5', 'Person 6', 'Person 7', 'Person 8', 'Person 9', 'Person 10']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#F0FF33']
fig, ax = plt.subplots(figsize=(12, 9))

# Plot
for i, (metric, color) in enumerate(zip(metrics, colors)):
    heights = data[:, i]
    starts = data_cum[:, i] - heights
    ax.bar(person_labels, heights, bottom=starts, width=0.8, label=metric, color=color)

# Formatting
ax.set_ylabel('Percentage')
ax.set_xlabel('Individuals')
ax.set_title('Health Metrics Distribution Among Individuals')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()