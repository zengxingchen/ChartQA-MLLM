
import matplotlib.pyplot as plt
import numpy as np

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
categories = ['Beaches', 'Mountains', 'Forests', 'Cities', 'Deserts', 'Lakes']
data = np.array([
    [25, 20, 15, 20, 10, 10],
    [30, 15, 10, 25, 10, 10],
    [20, 25, 20, 15, 10, 10],
    [35, 10, 15, 20, 10, 10],
    [25, 20, 20, 15, 10, 10],
    [20, 30, 10, 20, 10, 10],
    [30, 15, 20, 15, 10, 10]
])

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8C33', '#33FFF3']

# Create percentage data
data_percent = data / data.sum(axis=1)[:, None] * 100

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.7
bars = np.arange(len(days))

cumulative = np.zeros(len(days))

for i, (category, color) in enumerate(zip(categories, colors)):
    ax.bar(bars, data_percent[:, i], bottom=cumulative, color=color, label=category, width=bar_width)
    cumulative += data_percent[:, i]

ax.set_xticks(bars)
ax.set_xticklabels(days)
ax.set_ylabel('Percentage')
ax.set_title('Distribution of Different Travel Activities Over a Week')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()