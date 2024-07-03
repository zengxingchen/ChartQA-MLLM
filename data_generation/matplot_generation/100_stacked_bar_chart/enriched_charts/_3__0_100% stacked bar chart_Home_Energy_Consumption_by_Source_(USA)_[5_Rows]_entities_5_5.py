
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Science Fiction', 'Fantasy', 'Mystery', 'Non-Fiction', 'Romance', 'Horror', 'Historical', 'Biography']
research = [20, 15, 25, 30, 10, 20, 15, 25]
writing = [30, 35, 20, 25, 40, 25, 30, 25]
editing = [40, 25, 30, 20, 35, 30, 35, 25]
publishing = [10, 25, 25, 25, 15, 25, 20, 25]

# Convert to percentages
total = np.array(research) + np.array(writing) + np.array(editing) + np.array(publishing)
research = np.array(research) / total * 100
writing = np.array(writing) / total * 100
editing = np.array(editing) / total * 100
publishing = np.array(publishing) / total * 100

# Stack data
data = np.vstack([research, writing, editing, publishing])

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.6

y_pos = np.arange(len(categories))

for i, row in enumerate(data):
    if i == 0:
        ax.barh(y_pos, row, color=colors[i], edgecolor='white', height=bar_width)
    else:
        ax.barh(y_pos, row, left=np.sum(data[:i], axis=0), color=colors[i], edgecolor='white', height=bar_width)

# Labels and title
ax.set_yticks(y_pos)
ax.set_yticklabels(categories)
ax.set_xlabel('Percentage')
ax.set_title('Time Allocation in Different Book Genres for Writing Process')
ax.legend(['Research', 'Writing', 'Editing', 'Publishing'], loc='upper right')

plt.tight_layout()
plt.show()