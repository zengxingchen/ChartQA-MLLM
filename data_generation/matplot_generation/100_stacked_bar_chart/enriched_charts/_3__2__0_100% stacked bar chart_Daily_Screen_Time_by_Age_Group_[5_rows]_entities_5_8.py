
import matplotlib.pyplot as plt
import numpy as np

# Data
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
walking = [20, 25, 15, 20, 18, 10, 12]
running = [10, 5, 15, 10, 12, 5, 8]
exercise = [30, 25, 20, 25, 28, 35, 30]
resting = [30, 35, 40, 35, 32, 40, 40]
other = [10, 10, 10, 10, 10, 10, 10]

# Normalize data to sum to 100%
data = np.array([walking, running, exercise, resting, other])
data_percentage = data / data.sum(axis=0) * 100

# Colors
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1']

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.4
indices = np.arange(len(days))

bottoms = np.zeros(len(days))
for i in range(len(data)):
    ax.barh(indices, data_percentage[i], left=bottoms, height=bar_width, color=colors[i])
    bottoms += data_percentage[i]

# Labels and title
ax.set_xlabel('Percentage')
ax.set_title('Daily Physical Activity Distribution', pad=20)
ax.set_yticks(indices)
ax.set_yticklabels(days)
ax.legend(['Walking', 'Running', 'Exercise', 'Resting', 'Other'], bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()